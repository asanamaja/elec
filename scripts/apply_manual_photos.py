#!/usr/bin/env python3
"""Apply manual/ JPG photos directly to dandap_manual.html — no base64, no cropping."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from manual_photo_registry import (
    EARLY_DIAG_ORDER,
    MID_DIAG_ORDER,
    PHOTO_SLOTS,
    SYM_ORDER,
    photo_img_tag,
    validate_registry,
)
from manual_svgs import SVG_SLOTS
from pages_121_163 import PAGES_121_163
from pages_164_175 import PAGES_164_175

HTML = ROOT / "output/dandap_manual.html"

EXTRA_CSS = """
    table.tbl.sym-table { font-size: 9pt; margin-top: 6px; }
    table.tbl.sym-table td, table.tbl.sym-table th { padding: 4px 5px; text-align: center; }
    table.tbl.compact-table { font-size: 8.8pt; margin-top: 6px; }
    table.tbl.compact-table th, table.tbl.compact-table td { padding: 4px 5px; line-height: 1.35; }
    table.tbl.inspect-table td:first-child { width: 12%; }
    table.tbl.breaker-syms td { width: 20%; }
    table.tbl.duct-row td { width: 33%; }
    table.tbl.manual-table { font-size: 8.5pt; }
    .sym-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin: 6px 0; align-items: center; }
    .sym-grid img.sym { max-height: 30px; }
    img.sym { max-height: 28px; width: auto; display: inline-block; vertical-align: middle; object-fit: contain; }
"""

IMG_TAG = re.compile(r"<img\b[^>]*>", re.DOTALL)


def extract_page(block: str, page_id: str) -> str:
    pat = re.compile(rf'(<div class="page" id="{page_id}">.*?</div>\n</div>)', re.DOTALL)
    m = pat.search(block)
    if not m:
        raise ValueError(f"page {page_id} not found")
    return m.group(1)


def inject_syms(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        if key not in PHOTO_SLOTS:
            raise KeyError(f"unknown symbol slot {key}")
        return photo_img_tag(key)

    return re.sub(r"<!--IMG:([\w]+)-->", repl, text)


def replace_page(html: str, page_id: str, new_block: str) -> str:
    pat = re.compile(rf'<div class="page" id="{page_id}">.*?</div>\n</div>', re.DOTALL)
    if not pat.search(html):
        raise ValueError(f"{page_id} missing in HTML")
    return pat.sub(new_block, html, count=1)


def patch_css(html: str) -> str:
    if ".sym-grid" not in html:
        html = html.replace("    @media print {", EXTRA_CSS + "\n    @media print {")
    return html


def replace_imgs_in_block(block: str, slots: list[str], svg: list[str] | None = None) -> str:
    svg = svg or []
    slot_i = 0
    svg_i = 0

    def repl(_: re.Match[str]) -> str:
        nonlocal slot_i, svg_i
        if svg_i < len(svg):
            out = svg[svg_i]
            svg_i += 1
            return out
        if slot_i < len(slots):
            tag = photo_img_tag(slots[slot_i])
            slot_i += 1
            return tag
        return ""

    return IMG_TAG.sub(repl, block)


def rebuild_symbol_pages(html: str) -> str:
    pages = {
        "page-159": extract_page(PAGES_121_163, "page-159"),
        "page-160": extract_page(PAGES_121_163, "page-160"),
        "page-161": extract_page(PAGES_121_163, "page-161"),
        "page-170": extract_page(PAGES_164_175, "page-170"),
        "page-171": extract_page(PAGES_164_175, "page-171"),
    }
    for pid, block in pages.items():
        html = replace_page(html, pid, inject_syms(block))
    return html


def apply_early_diagrams(html: str) -> str:
    early_pages = {
        "page-018": ["p018_diag036"],
        "page-019": ["p019_diag037"],
        "page-021": ["p021_fig1", "p021_fig2"],
        "page-022": ["p022_fig1", "p022_fig2"],
        "page-032": ["p032_diag059"],
        "page-035": ["p035_diag065"],
        "page-049": ["p049_diag099"],
    }
    for pid, slots in early_pages.items():
        pat = re.compile(rf'(<div class="page" id="{pid}">.*?</div>\n</div>)', re.DOTALL)
        m = pat.search(html)
        if not m:
            raise ValueError(f"{pid} not found")
        svg = SVG_SLOTS.get(pid)
        new_block = replace_imgs_in_block(m.group(1), slots, svg)
        html = pat.sub(lambda _: new_block, html, count=1)
    return html


def apply_mid_diagrams(html: str) -> str:
    pat = re.compile(r'<div class="page" id="(page-\d+)">(.*?)</div>\n</div>', re.DOTALL)
    slot_i = 0

    def page_repl(m: re.Match[str]) -> str:
        nonlocal slot_i
        pid = m.group(1)
        body = m.group(2)
        page_num = int(pid.split("-")[1])
        if page_num < 60 or page_num >= 159:
            return m.group(0)
        if pid in SVG_SLOTS:
            return m.group(0)
        slots_needed = len(IMG_TAG.findall(body))
        if slots_needed == 0:
            return m.group(0)
        chunk = MID_DIAG_ORDER[slot_i : slot_i + slots_needed]
        if len(chunk) != slots_needed:
            raise ValueError(f"{pid} needs {slots_needed} slots, have {len(chunk)} left")
        slot_i += slots_needed
        new_body = replace_imgs_in_block(body, chunk)
        return f'<div class="page" id="{pid}">{new_body}</div>\n</div>'

    html = pat.sub(page_repl, html)
    if slot_i != len(MID_DIAG_ORDER):
        raise ValueError(f"mid diagram slots: used {slot_i} of {len(MID_DIAG_ORDER)}")
    return html


def apply_svg_pages(html: str) -> str:
    for pid, svgs in SVG_SLOTS.items():
        pat = re.compile(rf'(<div class="page" id="{pid}">.*?</div>\n</div>)', re.DOTALL)
        m = pat.search(html)
        if not m:
            raise ValueError(f"{pid} not found for SVG")
        new_block = replace_imgs_in_block(m.group(1), [], svgs)
        html = pat.sub(lambda _: new_block, html, count=1)
    return html


def strip_remaining_base64(html: str) -> str:
    """Remove any leftover base64-embedded images only."""
    return re.sub(r'<img\b[^>]*\bsrc="data:image[^"]*"[^>]*>', "", html, flags=re.DOTALL)


def update_build_stamp(html: str) -> str:
    stamp = '사진반영 20260629-direct'
    if "사진반영" in html:
        html = re.sub(r"사진반영 [^<\"]+", stamp, html, count=1)
    return html


def main() -> None:
    validate_registry()

    html = HTML.read_text(encoding="utf-8")
    html = patch_css(html)
    html = rebuild_symbol_pages(html)
    html = apply_svg_pages(html)
    html = apply_early_diagrams(html)
    html = apply_mid_diagrams(html)
    html = strip_remaining_base64(html)
    html = update_build_stamp(html)

    n_b64 = html.count("data:image")
    n_manual = len(re.findall(r'data-manual="', html))
    n_img = len(re.findall(r"<img\b", html))
    if n_b64:
        raise SystemExit(f"Still {n_b64} base64 images remaining")

    HTML.write_text(html, encoding="utf-8")
    print(f"Applied {n_manual} manual photos, {n_img} img tags, 0 base64")

    subprocess.run([sys.executable, str(ROOT / "scripts/build_symbols_view.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/fit_page_layout.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/export_manual_pdf.py")], check=True)
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/render_pdf_qa.py"), "21", "60", "74", "159", "160", "161"],
        check=True,
    )


if __name__ == "__main__":
    main()
