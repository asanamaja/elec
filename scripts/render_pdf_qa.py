#!/usr/bin/env python3
"""Render selected PDF pages to PNG for visual QA."""
from __future__ import annotations

import sys
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "output/dandap_manual.pdf"
OUT_DIR = ROOT / "output/qa_pdf"


def main() -> None:
    pages = [int(x) for x in sys.argv[1:]] if len(sys.argv) > 1 else [
        1, 2, 16, 50, 100, 159, 160, 161, 170, 171
    ]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    for n in pages:
        idx = n - 1
        if idx < 0 or idx >= len(doc):
            continue
        path = OUT_DIR / f"p{n:03d}.png"
        doc[idx].get_pixmap(matrix=fitz.Matrix(2, 2)).save(str(path))
        print(path)
    doc.close()


if __name__ == "__main__":
    main()
