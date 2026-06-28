#!/usr/bin/env python3
"""Append pages 75-163, inject cropped diagram images, embed base64."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from crop_all_diagrams import main as run_crops
from pages_121_163 import PAGES_121_163
from pages_75_120 import PAGES_75_120

HTML = ROOT / "output" / "dandap_manual.html"
CROPS = ROOT / "assets/images/manual/crops"

# placeholder id -> (filename, css class, style)
IMG: dict[str, tuple[str, str, str]] = {
    "p060_diag126": ("p060_diag126.png", "diag", "max-height:200px"),
    "p061_diag128": ("p061_diag128.png", "diag", "max-height:200px"),
    "p071_diag162": ("p071_diag162.png", "diag", "max-height:120px"),
    "p073_sym168": ("p073_sym168.png", "sym", "max-height:52px;width:auto;display:inline-block;vertical-align:middle"),
    "p074_diag170": ("p074_diag170.png", "diag", "max-height:240px"),
    "p080_diag182": ("p080_diag182.png", "diag", "max-height:200px"),
    "p088_diag208_1": ("p088_diag208_1.png", "diag", "max-height:160px"),
    "p088_diag208_2": ("p088_diag208_2.png", "diag", "max-height:160px"),
    "p096_diag224": ("p096_diag224.png", "diag", "max-height:180px"),
    "p097_diag228": ("p097_diag228.png", "diag", "max-height:180px"),
    "p108_cubicle_l": ("p108_cubicle_l.png", "diag", "max-height:200px;width:48%;display:inline-block"),
    "p108_cubicle_r": ("p108_cubicle_r.png", "diag", "max-height:200px;width:48%;display:inline-block"),
    "p109_q258_diag": ("p109_q258_diag.png", "diag", "max-height:200px"),
    "p114_diag268": ("p114_diag268.png", "diag", "max-height:200px"),
    "p115_diag270": ("p115_diag270.png", "diag", "max-height:320px"),
    "p118_diag282": ("p118_diag282.png", "diag", "max-height:90px"),
    "p125_diag299": ("p125_diag299.png", "diag", "max-height:200px"),
    "p126_diag300": ("p126_diag300.png", "diag", "max-height:240px"),
    "p128_diag303": ("p128_diag303.png", "diag", "max-height:200px"),
    "p135_sys_gnd": ("p135_sys_gnd.png", "diag", "max-height:140px"),
    "p135_eq_gnd": ("p135_eq_gnd.png", "diag", "max-height:140px"),
    "p139_line_gnd": ("p139_line_gnd.png", "diag", "max-height:260px;width:48%;display:inline-block"),
    "p139_portable_gnd": ("p139_portable_gnd.png", "diag", "max-height:260px;width:48%;display:inline-block"),
    "p140_diag331": ("p140_diag331.png", "diag", "max-height:260px"),
    "p146_fig1": ("p146_fig1.png", "diag", "max-height:150px;width:48%;display:inline-block"),
    "p146_fig2": ("p146_fig2.png", "diag", "max-height:150px;width:48%;display:inline-block"),
    "p147_wenner": ("p147_wenner.png", "diag", "max-height:110px"),
    "p148_earth_tester": ("p148_earth_tester.png", "diag", "max-height:200px"),
    "p149_timed_contact": ("p149_timed_contact.png", "sym", "max-height:22px;width:auto;display:inline-block;vertical-align:middle"),
    "p153_relay8": ("p153_relay8.png", "diag", "max-height:300px"),
    "p158_sym_sw": ("p158_sym_sw.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_2p": ("p158_sym_2p.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_4w": ("p158_sym_4w.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_outdoor": ("p158_sym_outdoor.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_h400": ("p158_sym_h400.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_m400": ("p158_sym_m400.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_n400": ("p158_sym_n400.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_outlet": ("p158_sym_outlet.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_ceiling": ("p158_sym_ceiling.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_floor": ("p158_sym_floor.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_2gang": ("p158_sym_2gang.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p158_sym_3p_out": ("p158_sym_3p_out.png", "sym", "height:14px;width:auto;display:inline-block;vertical-align:middle"),
    "p159_outlet_table": ("p159_outlet_table.png", "diag", "max-height:120px"),
    "p159_switch_sym": ("p159_switch_sym.png", "diag", "max-height:100px"),
    "p159_duct_syms": ("p159_duct_syms.png", "diag", "max-height:70px"),
    "p160_breaker_syms": ("p160_breaker_syms.png", "diag", "max-height:80px"),
    "p161_tr_syms": ("p161_tr_syms.png", "diag", "max-height:120px"),
}


def patch_css(html: str) -> str:
    if "img.sym" not in html:
        html = html.replace(
            "    img.diag { width: 100%; object-fit: contain; margin: 8px 0; }",
            "    img.diag { width: 100%; object-fit: contain; margin: 8px 0; }\n"
            "    img.sym { object-fit: contain; margin: 0 2px; }",
        )
    html = html.replace(
        '<span id="pg-info">p.1–74 (DAY1~6 진행중) · 직접 전사</span>',
        '<span id="pg-info">p.1–163 완료 · 직접 전사</span>',
    )
    return html


def inject_placeholders(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        if key not in IMG:
            print(f"warn: missing IMG map for {key}")
            return ""
        fname, cls, style = IMG[key]
        return (
            f'<img class="{cls}" src="../assets/images/manual/crops/{fname}" '
            f'style="{style};" alt="">'
        )

    return re.sub(r"<!--IMG:([\w]+)-->", repl, html)


def append_pages(html: str) -> str:
    marker = "\n</div>\n\n<script defer src="
    if 'id="page-075"' in html:
        print("pages 75+ already present")
        return html
    block = PAGES_75_120 + PAGES_121_163
    return html.replace(marker, block + marker, 1)


def main() -> None:
    print("Cropping diagrams...")
    run_crops()

    html = HTML.read_text(encoding="utf-8")
    html = patch_css(html)
    html = append_pages(html)
    html = inject_placeholders(html)
    HTML.write_text(html, encoding="utf-8")

    print("Embedding...")
    subprocess.run([sys.executable, str(ROOT / "scripts/embed_manual_assets.py")], check=True)

    final = HTML.read_text(encoding="utf-8")
    assert final.rstrip().endswith("</html>")
    n_img = len(re.findall(r"data:image/png;base64,", final))
    n_pages = len(re.findall(r'id="page-\d+"', final))
    missing = re.findall(r"<!--IMG:", final)
    print(f"Done: {HTML.stat().st_size // 1024}KB, {n_pages} pages, {n_img} images")
    if missing:
        print("WARN leftover placeholders:", len(missing))


if __name__ == "__main__":
    main()
