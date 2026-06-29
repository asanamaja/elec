#!/usr/bin/env python3
"""Embed user crop PNGs from assets/images/manual/crops into dandap_manual.html.

Uses page-order matching for diagram slots (pages 60+). Only replaces an image
when the corresponding crop file exists — never pulls from PDF.
"""
from __future__ import annotations

import base64
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"
CROPS = ROOT / "assets/images/manual/crops"

# Sequential diagram crops on pages 60+ (order must match HTML layout)
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
]

# Q043 NCS figures on page 21 (two side-by-side diagrams)
NCS_PAGE = 21
NCS_CROPS = ["p043_ncs_fig1.png", "p043_ncs_fig2.png"]


def to_data_uri(path: Path) -> str:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{data}"


def embed_page_crops(html: str) -> tuple[str, int]:
    cache: dict[str, str] = {}
    for name in CROP_ORDER:
        p = CROPS / name
        if p.exists():
            cache[name] = to_data_uri(p)

    page_pat = re.compile(r'id="(page-\d+)"')
    img_pat = re.compile(
        r'<img\b([^>]*?\bclass="(?:diag|sym)"[^>]*?\bsrc=")'
        r'((?:data:image/[^"]+)|(?:\.\./assets/images/manual/crops/[^"]+))'
        r'(")([^>]*>)',
        re.DOTALL,
    )

    crop_idx = 0
    current_page = 0
    ncs_idx = 0
    replaced = 0
    out: list[str] = []
    pos = 0

    for m in img_pat.finditer(html):
        out.append(html[pos : m.start()])
        for pm in page_pat.finditer(html, 0, m.start()):
            current_page = int(pm.group(1).split("-")[1])

        prefix, _, suffix, tail = m.group(1), m.group(2), m.group(3), m.group(4)
        tail = re.sub(r'\s*data-crop="[^"]*"', "", tail)
        new_src: str | None = None
        crop_name: str | None = None

        if current_page == NCS_PAGE and ncs_idx < len(NCS_CROPS):
            name = NCS_CROPS[ncs_idx]
            ncs_idx += 1
            if (CROPS / name).exists():
                new_src = cache.get(name) or to_data_uri(CROPS / name)
                crop_name = name
        elif current_page >= 60 and crop_idx < len(CROP_ORDER):
            name = CROP_ORDER[crop_idx]
            crop_idx += 1
            if name in cache:
                new_src = cache[name]
                crop_name = name

        if new_src and crop_name:
            out.append(f'<img{prefix}{new_src}" data-crop="{crop_name}"{tail}')
            replaced += 1
        else:
            out.append(m.group(0))
        pos = m.end()

    out.append(html[pos:])
    return "".join(out), replaced


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    html, n = embed_page_crops(html)
    HTML.write_text(html, encoding="utf-8")
    print(f"Embedded {n} user crop images into {HTML}")


if __name__ == "__main__":
    main()
