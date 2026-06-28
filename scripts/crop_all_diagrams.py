#!/usr/bin/env python3
"""Crop diagram/symbol regions from PDF — only marked figure areas, not full pages."""
from __future__ import annotations

from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "assets/pdf/source.pdf"
CROPS = ROOT / "assets/images/manual/crops"

# PDF page index (0-based) -> list of (filename, rect)
SPECS: dict[int, list[tuple[str, fitz.Rect]]] = {
    # DAY 6
    59: [("p060_diag126.png", fitz.Rect(72, 228, 528, 468))],
    60: [("p061_diag128.png", fitz.Rect(72, 208, 528, 458))],
    70: [("p071_diag162.png", fitz.Rect(72, 178, 528, 332))],
    72: [("p073_sym168.png", fitz.Rect(72, 128, 168, 208))],
    73: [("p074_diag170.png", fitz.Rect(52, 108, 548, 408))],
    # p.80, 88, 96-97
    79: [("p080_diag182.png", fitz.Rect(52, 108, 548, 380))],
    87: [
        ("p088_diag208_1.png", fitz.Rect(52, 108, 302, 320)),
        ("p088_diag208_2.png", fitz.Rect(302, 108, 548, 320)),
    ],
    95: [("p096_diag224.png", fitz.Rect(52, 108, 548, 360))],
    96: [("p097_diag228.png", fitz.Rect(52, 108, 548, 360))],
    # 큐비클 Q257
    107: [
        ("p108_cubicle_l.png", fitz.Rect(52, 112, 302, 318)),
        ("p108_cubicle_r.png", fitz.Rect(302, 112, 548, 318)),
    ],
    108: [("p109_q258_diag.png", fitz.Rect(52, 108, 548, 400))],
    113: [("p114_diag268.png", fitz.Rect(52, 108, 548, 400))],
    # TR#1/TR#2
    114: [("p115_diag270.png", fitz.Rect(52, 108, 548, 498))],
    # 부동충전 회로 Q282
    117: [("p118_diag282.png", fitz.Rect(105, 558, 515, 612))],
    # UPS
    124: [("p125_diag299.png", fitz.Rect(52, 198, 548, 358))],
    125: [("p126_diag300.png", fitz.Rect(52, 178, 548, 398))],
    127: [("p128_diag303.png", fitz.Rect(52, 112, 548, 278))],
    # 접지 Q320
    134: [
        ("p135_sys_gnd.png", fitz.Rect(70, 500, 300, 620)),
        ("p135_eq_gnd.png", fitz.Rect(310, 500, 540, 620)),
    ],
    # Q329 선로+휴대접지기
    138: [
        ("p139_line_gnd.png", fitz.Rect(52, 112, 288, 388)),
        ("p139_portable_gnd.png", fitz.Rect(292, 112, 548, 388)),
    ],
    # 접지계통 M,P,C,B
    139: [("p140_diag331.png", fitz.Rect(52, 108, 548, 378))],
    # 토양비저항
    145: [
        ("p146_fig1.png", fitz.Rect(52, 198, 298, 358)),
        ("p146_fig2.png", fitz.Rect(302, 198, 548, 358)),
    ],
    146: [("p147_wenner.png", fitz.Rect(52, 178, 548, 288))],
    147: [("p148_earth_tester.png", fitz.Rect(52, 178, 548, 338))],
    # Q353 한시동작 접점 기호 (PDF p.149)
    148: [("p149_timed_contact.png", fitz.Rect(72, 478, 138, 512))],
    # Q354 8핀 타이머 결선도 (PDF p.150, not p.153)
    149: [("p153_relay8.png", fitz.Rect(75, 255, 420, 405))],
    # DAY14 기호 p.158 (PDF index 157)
    157: [
        ("p158_sym_sw.png", fitz.Rect(368, 172, 384, 188)),
        ("p158_sym_2p.png", fitz.Rect(118, 222, 152, 242)),
        ("p158_sym_4w.png", fitz.Rect(198, 222, 228, 242)),
        ("p158_sym_outdoor.png", fitz.Rect(106, 328, 126, 348)),
        ("p158_sym_h400.png", fitz.Rect(178, 358, 224, 378)),
        ("p158_sym_m400.png", fitz.Rect(258, 358, 304, 378)),
        ("p158_sym_n400.png", fitz.Rect(338, 358, 384, 378)),
        ("p158_sym_outlet.png", fitz.Rect(238, 398, 262, 422)),
        ("p158_sym_ceiling.png", fitz.Rect(368, 418, 392, 442)),
        ("p158_sym_floor.png", fitz.Rect(456, 418, 480, 442)),
        ("p158_sym_2gang.png", fitz.Rect(108, 468, 148, 492)),
        ("p158_sym_3p_out.png", fitz.Rect(208, 468, 258, 492)),
    ],
    # p.159 Q367-369
    158: [
        ("p159_outlet_table.png", fitz.Rect(52, 108, 548, 248)),
        ("p159_switch_sym.png", fitz.Rect(52, 278, 198, 378)),
        ("p159_duct_syms.png", fitz.Rect(52, 418, 548, 498)),
    ],
    159: [("p160_breaker_syms.png", fitz.Rect(52, 108, 548, 198))],
    160: [("p161_tr_syms.png", fitz.Rect(52, 108, 548, 248))],
}


def main() -> None:
    CROPS.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    for page_idx, items in sorted(SPECS.items()):
        page = doc[page_idx]
        for name, rect in items:
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
            path = CROPS / name
            pix.save(str(path))
            print(f"p{page_idx+1:03d} -> {name} ({pix.width}x{pix.height})")
    doc.close()


if __name__ == "__main__":
    main()
