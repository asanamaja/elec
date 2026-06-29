#!/usr/bin/env python3
"""Rebuild symbol pages (p.158-161, p.170-171) with user crops and HTML tables."""
from __future__ import annotations

import base64
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from pages_121_163 import PAGES_121_163
from pages_164_175 import PAGES_164_175

HTML = ROOT / "output/dandap_manual.html"
USER = ROOT / "assets/images/manual/user"

SYM_IMG: dict[str, tuple[str, str, str]] = {
    "sym_sw": ("sym_sw.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_2p": ("sym_2p.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_4w": ("sym_4w.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_outdoor": ("sym_outdoor.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_h400": ("sym_h400.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_m400": ("sym_m400.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_n400": ("sym_n400.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_outlet": ("sym_outlet.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_ceiling": ("sym_ceiling.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_floor": ("sym_floor.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_2gang": ("sym_2gang.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_3p_out": ("sym_3p_out.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_lk": ("sym_lk.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_et": ("sym_et.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_el": ("sym_el.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_e_outlet": ("sym_e_outlet.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_t_outlet": ("sym_t_outlet.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_wp": ("sym_wp.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_h_outlet": ("sym_h_outlet.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_switch_368": ("sym_switch_368.png", "diag", "max-height:72px;width:100%;object-fit:contain;margin:4px 0"),
    "sym_md": ("sym_md.png", "sym", "max-height:36px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_ld": ("sym_ld.png", "sym", "max-height:36px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_f7": ("sym_f7.png", "sym", "max-height:36px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_breaker_e": ("sym_breaker_e.png", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_b": ("sym_breaker_b.png", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_ec": ("sym_breaker_ec.png", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_s": ("sym_breaker_s.png", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_breaker_g": ("sym_breaker_g.png", "sym", "max-height:34px;width:auto;display:block;margin:0 auto"),
    "sym_tr_tb": ("sym_tr_tb.png", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_tr": ("sym_tr_tr.png", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_tn": ("sym_tr_tn.png", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_tf": ("sym_tr_tf.png", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
    "sym_tr_th": ("sym_tr_th.png", "sym", "max-height:30px;width:auto;display:inline-block;vertical-align:middle"),
}

EXTRA_CSS = """
    .content { overflow: hidden; max-height: calc(842px - 172px); }
    .content.compact { font-size: 9.2pt; line-height: 1.42; }
    .content.compact .q { margin-bottom: 10px; }
    table.tbl.sym-table { font-size: 9pt; margin-top: 6px; }
    table.tbl.sym-table td, table.tbl.sym-table th { padding: 4px 5px; text-align: center; }
    table.tbl.compact-table { font-size: 8.8pt; margin-top: 6px; }
    table.tbl.compact-table th, table.tbl.compact-table td { padding: 4px 5px; line-height: 1.35; }
    table.tbl.inspect-table td:first-child { width: 12%; }
    table.tbl.breaker-syms td { width: 20%; }
    table.tbl.duct-row td { width: 33%; }
    .sym-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 6px 12px; margin: 6px 0; align-items: center; }
    .sym-grid img.sym { max-height: 30px; }
    img.sym { max-height: 28px; width: auto; display: inline-block; vertical-align: middle; object-fit: contain; }
"""


def extract_page(block: str, page_id: str) -> str:
    pat = re.compile(
        rf'(<div class="page" id="{page_id}">.*?</div>\n</div>)',
        re.DOTALL,
    )
    m = pat.search(block)
    if not m:
        raise ValueError(f"page {page_id} not found")
    return m.group(1)


def inject_syms(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        if key not in SYM_IMG:
            raise KeyError(key)
        fname, cls, style = SYM_IMG[key]
        return (
            f'<img class="{cls}" src="../assets/images/manual/user/{fname}" '
            f'style="{style};" alt="" data-sym="{fname}">'
        )

    return re.sub(r"<!--IMG:([\w]+)-->", repl, text)


def replace_page(html: str, page_id: str, new_block: str) -> str:
    pat = re.compile(
        rf'<div class="page" id="{page_id}">.*?</div>\n</div>',
        re.DOTALL,
    )
    if not pat.search(html):
        raise ValueError(f"{page_id} missing in HTML")
    return pat.sub(new_block, html, count=1)


def patch_css(html: str) -> str:
    if ".sym-grid" not in html:
        html = html.replace("    @media print {", EXTRA_CSS + "\n    @media print {")
    if "overflow: hidden; max-height" not in html:
        html = html.replace(
            ".content { position: absolute; left: 72px; right: 52px; top: 118px; padding-bottom: 54px; }",
            ".content { position: absolute; left: 72px; right: 52px; top: 118px; padding-bottom: 54px; overflow: hidden; max-height: calc(842px - 172px); }",
        )
    return html


def embed_user_images(html: str) -> str:
    cache: dict[str, str] = {}

    def to_uri(name: str) -> str:
        if name not in cache:
            data = base64.b64encode((USER / name).read_bytes()).decode("ascii")
            cache[name] = f"data:image/png;base64,{data}"
        return cache[name]

    def repl(m: re.Match[str]) -> str:
        prefix, name, tail = m.group(1), m.group(2), m.group(3)
        return f'{prefix}{to_uri(name)}" data-sym="{name}"{tail}'

    html = re.sub(
        r'(src=")(?:\.\./assets/images/manual/user/|data:image/png;base64,[^"]+)([^"]+)(")([^>]*data-sym="[^"]+")?',
        lambda m: repl(re.Match(re.compile(""), 0, 0)) if False else None,
        html,
    )
    # simpler: replace user paths
    for name in {v[0] for v in SYM_IMG.values()}:
        path = f'../assets/images/manual/user/{name}'
        if path in html:
            html = html.replace(f'src="{path}"', f'src="{to_uri(name)}"')
    return html


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/crop_user_symbols.py")], check=True)

    pages_158_161 = {
        "page-159": extract_page(PAGES_121_163, "page-159"),
        "page-160": extract_page(PAGES_121_163, "page-160"),
        "page-161": extract_page(PAGES_121_163, "page-161"),
    }
    pages_170_171 = {
        "page-170": extract_page(PAGES_164_175, "page-170"),
        "page-171": extract_page(PAGES_164_175, "page-171"),
    }

    html = HTML.read_text(encoding="utf-8")
    html = patch_css(html)

    for pid, block in {**pages_158_161, **pages_170_171}.items():
        html = replace_page(html, pid, inject_syms(block))

    # embed user symbol images
    cache: dict[str, str] = {}
    for name in {v[0] for v in SYM_IMG.values()}:
        rel = f'../assets/images/manual/user/{name}'
        if rel in html:
            data = base64.b64encode((USER / name).read_bytes()).decode("ascii")
            cache[name] = f"data:image/png;base64,{data}"
            html = html.replace(f'src="{rel}"', f'src="{cache[name]}" data-sym="{name}"')

    HTML.write_text(html, encoding="utf-8")

    # stats
    import re as _re

    n_sym = len(_re.findall(r'data-sym="sym_', html))
    n_table = len(_re.findall(r'class="tbl sym-table', html))
    print(f"Rebuilt symbol pages: {n_sym} user symbols, {n_table} sym tables")


if __name__ == "__main__":
    main()
