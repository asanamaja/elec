#!/usr/bin/env python3
"""Crop symbol images from PDF into assets/images/manual/user/."""
from __future__ import annotations

from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "assets/pdf/source.pdf"
OUT = ROOT / "assets/images/manual/user"

# PDF page index (0-based) -> list of (filename, rect)
SPECS: dict[int, list[tuple[str, fitz.Rect]]] = {
    # book p.158 Q365-366
    157: [
        ("sym_sw.png", fitz.Rect(246, 170, 270, 194)),
        ("sym_2p.png", fitz.Rect(108, 216, 170, 254)),
        ("sym_4w.png", fitz.Rect(184, 216, 248, 254)),
        ("sym_outdoor.png", fitz.Rect(88, 378, 136, 420)),
        ("sym_h400.png", fitz.Rect(96, 418, 136, 454)),
        ("sym_m400.png", fitz.Rect(96, 448, 136, 484)),
        ("sym_n400.png", fitz.Rect(96, 478, 136, 514)),
        ("sym_outlet.png", fitz.Rect(216, 512, 264, 554)),
        ("sym_ceiling.png", fitz.Rect(334, 536, 382, 580)),
        ("sym_floor.png", fitz.Rect(332, 566, 382, 614)),
        ("sym_2gang.png", fitz.Rect(80, 618, 142, 662)),
        ("sym_3p_out.png", fitz.Rect(200, 618, 268, 662)),
    ],
    # book p.159 Q367-369
    158: [
        ("sym_lk.png", fitz.Rect(68, 145, 300, 190)),
        ("sym_et.png", fitz.Rect(300, 145, 532, 190)),
        ("sym_el.png", fitz.Rect(68, 190, 300, 235)),
        ("sym_e_outlet.png", fitz.Rect(300, 190, 532, 235)),
        ("sym_t_outlet.png", fitz.Rect(68, 235, 300, 280)),
        ("sym_wp.png", fitz.Rect(300, 235, 532, 280)),
        ("sym_h_outlet.png", fitz.Rect(68, 280, 300, 330)),
        ("sym_switch_368.png", fitz.Rect(68, 388, 530, 505)),
        ("sym_md.png", fitz.Rect(68, 590, 210, 655)),
        ("sym_ld.png", fitz.Rect(210, 590, 385, 655)),
        ("sym_f7.png", fitz.Rect(385, 590, 538, 655)),
    ],
    # book p.160 Q370-371
    159: [
        ("sym_breaker_e.png", fitz.Rect(72, 188, 138, 248)),
        ("sym_breaker_b.png", fitz.Rect(148, 188, 214, 248)),
        ("sym_breaker_ec.png", fitz.Rect(224, 188, 310, 248)),
        ("sym_breaker_s.png", fitz.Rect(316, 188, 392, 248)),
        ("sym_breaker_g.png", fitz.Rect(406, 188, 518, 248)),
        ("sym_tr_tb.png", fitz.Rect(75, 370, 190, 408)),
        ("sym_tr_tr.png", fitz.Rect(288, 370, 405, 408)),
        ("sym_tr_tn.png", fitz.Rect(75, 415, 190, 453)),
        ("sym_tr_tf.png", fitz.Rect(288, 415, 405, 453)),
        ("sym_tr_th.png", fitz.Rect(75, 498, 190, 535)),
    ],
}


def extract_tr_symbols_from_preview() -> None:
    """Left-column PDF scan shadow makes direct TH/TN crops dark; use area render."""
    try:
        from PIL import Image, ImageEnhance, ImageOps
    except ImportError:
        return

    import fitz

    preview = OUT.parent / "preview"
    preview.mkdir(parents=True, exist_ok=True)
    area = preview / "q371_area.png"
    doc = fitz.open(PDF)
    doc[159].get_pixmap(matrix=fitz.Matrix(3, 3), clip=fitz.Rect(60, 360, 520, 530)).save(str(area))
    doc.close()

    src = Image.open(area)
    w, h = src.size
    boxes = {
        "sym_tr_tb.png": (int(w * 0.02), int(h * 0.05), int(w * 0.22), int(h * 0.28)),
        "sym_tr_tr.png": (int(w * 0.52), int(h * 0.05), int(w * 0.78), int(h * 0.28)),
        "sym_tr_tn.png": (int(w * 0.02), int(h * 0.42), int(w * 0.22), int(h * 0.65)),
        "sym_tr_tf.png": (int(w * 0.52), int(h * 0.42), int(w * 0.78), int(h * 0.65)),
        "sym_tr_th.png": (int(w * 0.02), int(h * 0.82), int(w * 0.22), int(h * 0.98)),
    }
    for name, box in boxes.items():
        c = src.crop(box)
        c = ImageOps.autocontrast(c)
        c = ImageEnhance.Brightness(c).enhance(1.3)
        c.save(OUT / name)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    for page_idx, items in sorted(SPECS.items()):
        page = doc[page_idx]
        for name, rect in items:
            if name.startswith("sym_tr_"):
                continue
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
            path = OUT / name
            pix.save(str(path))
            print(f"p{page_idx + 1:03d} -> {name} ({pix.width}x{pix.height})")
    doc.close()
    extract_tr_symbols_from_preview()
    for name in [
        "sym_tr_tb.png",
        "sym_tr_tr.png",
        "sym_tr_tn.png",
        "sym_tr_tf.png",
        "sym_tr_th.png",
    ]:
        p = OUT / name
        if p.exists():
            from PIL import Image

            im = Image.open(p)
            print(f"p160 -> {name} ({im.width}x{im.height}) [area extract]")


if __name__ == "__main__":
    main()
