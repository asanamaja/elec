#!/usr/bin/env python3
"""Build a lightweight mobile-friendly symbol pages viewer (p.158-160)."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from pages_121_163 import PAGES_121_163
from rebuild_symbol_pages import SYM_IMG, extract_page, inject_syms, EXTRA_CSS

OUT = ROOT / "output/symbols_view.html"
BUILD = "20260629-photo"
ASSET_PREFIX = "../assets/images/manual/user/"


def main() -> None:
    blocks = []
    for pid in ("page-159", "page-160", "page-161"):
        blocks.append(inject_syms(extract_page(PAGES_121_163, pid)))

    body = "\n\n".join(blocks)
    # keep external image paths (no base64) for fast mobile load

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="build" content="{BUILD}">
  <title>옥내기호 심벌 (p.158-160) — 사진 반영</title>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ background: #444; font-family: 'Noto Sans KR', sans-serif; }}
    .banner {{
      position: sticky; top: 0; z-index: 99;
      background: #0f766e; color: #fff; padding: .7rem 1rem; font-size: .9rem;
      line-height: 1.5;
    }}
    .banner a {{ color: #fef08a; }}
    .pages {{ padding: 1rem .5rem 2rem; display: flex; flex-direction: column; align-items: center; gap: 12px; }}
    .page {{
      width: min(595px, 100vw - 8px); height: auto; min-height: 842px;
      position: relative; background: #fff; overflow: hidden;
      box-shadow: 0 2px 14px rgba(0,0,0,.25);
      font-size: 10.5pt; line-height: 1.55; color: #1a1a1a;
    }}
    .abs {{ position: absolute; }}
    .brand {{ top: 38px; right: 52px; font-style: italic; font-weight: 700; font-size: 13.5pt; }}
    .day-tag {{ top: 42px; left: 52px; font-size: 9pt; font-weight: 700; }}
    .foot-r {{ bottom: 44px; right: 52px; font-size: 8.5pt; }}
    .content {{ position: absolute; left: 72px; right: 52px; top: 118px; padding-bottom: 54px; }}
    .q {{ margin-bottom: 20px; }}
    .q-num {{ font-size: 12.5pt; font-weight: 700; margin-bottom: 2px; }}
    .q-hline {{ border: none; border-top: 0.8px solid #d4a0a8; margin: 3px 0 7px; }}
    .q-text {{ margin-bottom: 6px; }}
    .ans {{ color: #c9a0a8; }}
    .ans-line {{ margin: 2px 0 2px 4px; }}
    table.tbl {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 10pt; }}
    table.tbl th, table.tbl td {{ border: 0.6px solid #bbb; padding: 7px 8px; vertical-align: middle; }}
    table.tbl th {{ background: #ececec; font-weight: 700; text-align: center; }}
    img.sym, img.diag {{ object-fit: contain; }}
{EXTRA_CSS}
  </style>
</head>
<body>
  <div class="banner">
    <strong>사진 반영 {BUILD}</strong> · p.158–160 심벌 페이지<br>
    <a href="dandap_manual.html?v={BUILD}">전체 175페이지 보기</a>
    · <a href="../index.html">목록</a>
  </div>
  <div class="pages">
{body}
  </div>
</body>
</html>
"""
    OUT.write_text(html, encoding="utf-8")
    n_img = len(re.findall(rf'src="{re.escape(ASSET_PREFIX)}', html))
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB, {n_img} external images)")


if __name__ == "__main__":
    main()
