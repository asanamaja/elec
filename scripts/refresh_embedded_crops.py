#!/usr/bin/env python3
"""Re-embed crop PNGs into dandap_manual.html after coordinate fixes.

Only updates images on pages 60+ (manual crop set). Earlier pages keep their
existing embedded images. Adds data-crop="filename.png" for future refreshes.
"""
from __future__ import annotations

import base64
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"
CROPS = ROOT / "assets/images/manual/crops"

CROP_ORDER: list[str] = [
    "p060_diag126.png",
    "p061_diag128.png",
    "p071_diag162.png",
    "p073_sym168.png",
    "p074_diag170.png",
    "p080_diag182.png",
    "p088_diag208_1.png",
    "p088_diag208_2.png",
    "p096_diag224.png",
    "p097_diag228.png",
    "p108_cubicle_l.png",
    "p108_cubicle_r.png",
    "p109_q258_diag.png",
    "p114_diag268.png",
    "p115_diag270.png",
    "p118_diag282.png",
    "p125_diag299.png",
    "p126_diag300.png",
    "p128_diag303.png",
    "p135_sys_gnd.png",
    "p135_eq_gnd.png",
    "p139_line_gnd.png",
    "p139_portable_gnd.png",
    "p140_diag331.png",
    "p146_fig1.png",
    "p146_fig2.png",
    "p147_wenner.png",
    "p148_earth_tester.png",
    "p149_timed_contact.png",
    "p153_relay8.png",
    "p158_sym_sw.png",
    "p158_sym_2p.png",
    "p158_sym_4w.png",
    "p158_sym_outdoor.png",
    "p158_sym_h400.png",
    "p158_sym_m400.png",
    "p158_sym_n400.png",
    "p158_sym_outlet.png",
    "p158_sym_ceiling.png",
    "p158_sym_floor.png",
    "p158_sym_2gang.png",
    "p158_sym_3p_out.png",
    "p159_outlet_table.png",
    "p159_switch_sym.png",
    "p159_duct_syms.png",
    "p160_breaker_syms.png",
    "p161_tr_syms.png",
    "p170_table385.png",
    "p171_table387.png",
]


def to_data_uri(path: Path) -> str:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{data}"


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/crop_all_diagrams.py")], check=True)

    html = HTML.read_text(encoding="utf-8")
    cache: dict[str, str] = {name: to_data_uri(CROPS / name) for name in CROP_ORDER}

    page_pat = re.compile(r'id="(page-\d+)"')
    img_pat = re.compile(
        r'<img\b([^>]*?\bclass="(?:diag|sym)"[^>]*?\bsrc=")'
        r'((?:data:image/png;base64,[^"]+)|(?:\.\./assets/images/manual/crops/[^"]+))'
        r'(")([^>]*>)',
        re.DOTALL,
    )

    crop_idx = 0
    current_page = 0
    out: list[str] = []
    pos = 0

    for m in img_pat.finditer(html):
        out.append(html[pos : m.start()])
        page_m = None
        for pm in page_pat.finditer(html, 0, m.start()):
            page_m = pm
        if page_m:
            current_page = int(page_m.group(1).split("-")[1])

        prefix, _, suffix, tail = m.group(1), m.group(2), m.group(3), m.group(4)
        if current_page >= 60 and crop_idx < len(CROP_ORDER):
            name = CROP_ORDER[crop_idx]
            crop_idx += 1
            tail = re.sub(r'\s*data-crop="[^"]*"', "", tail)
            out.append(f'<img{prefix}{cache[name]}" data-crop="{name}"{tail}')
        else:
            out.append(m.group(0))
        pos = m.end()

    out.append(html[pos:])
    html = "".join(out)
    HTML.write_text(html, encoding="utf-8")
    print(f"Refreshed {crop_idx} crops (pages 60+) in {HTML}")


if __name__ == "__main__":
    main()
