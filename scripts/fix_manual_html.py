#!/usr/bin/env python3
"""Fix formula rendering, remove decorative images, re-crop diagrams, fix TOC."""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"
CROPS = ROOT / "assets" / "images" / "manual" / "crops"
PDF = ROOT / "assets" / "pdf" / "source.pdf"

CROP_SPECS: dict[int, list[tuple[str, fitz.Rect]]] = {
    17: [("p018_diag036.png", fitz.Rect(52, 94, 556, 535))],
    18: [("p019_diag037.png", fitz.Rect(48, 82, 554, 408))],
    20: [
        ("p021_fig1.png", fitz.Rect(52, 182, 302, 478)),
        ("p021_fig2.png", fitz.Rect(298, 182, 548, 478)),
    ],
    21: [
        ("p022_fig1b.png", fitz.Rect(52, 44, 302, 278)),
        ("p022_fig2b.png", fitz.Rect(298, 44, 548, 278)),
    ],
    28: [
        ("p029_tbl053.png", fitz.Rect(46, 126, 554, 328)),
        ("p029_tbl054.png", fitz.Rect(46, 472, 554, 748)),
    ],
    31: [("p032_diag059.png", fitz.Rect(46, 168, 554, 392))],
    34: [("p035_diag065.png", fitz.Rect(44, 100, 556, 302))],
    40: [("p041_tbl081.png", fitz.Rect(44, 162, 556, 472))],
    43: [("p044_tbl089.png", fitz.Rect(44, 182, 556, 296))],
    44: [("p045_tbl092.png", fitz.Rect(44, 84, 556, 432))],
    48: [("p049_diag099.png", fitz.Rect(44, 92, 556, 328))],
}

PAGE_IMAGES: dict[str, list[str]] = {
    "page-018": ["p018_diag036.png"],
    "page-019": ["p019_diag037.png"],
    "page-021": ["p021_fig1.png", "p021_fig2.png"],
    "page-022": ["p022_fig1b.png", "p022_fig2b.png"],
    "page-029": ["p029_tbl053.png", "p029_tbl054.png"],
    "page-032": ["p032_diag059.png"],
    "page-035": ["p035_diag065.png"],
    "page-041": ["p041_tbl081.png"],
    "page-044": ["p044_tbl089.png"],
    "page-045": ["p045_tbl092.png"],
    "page-049": ["p049_diag099.png"],
}

REMOVE_ALL_IMG_PAGES = {
    "page-001",
    "page-002",
    "page-003",
    "page-004",
    "page-014",
    "page-028",
    "page-036",
    "page-048",
}

IMG_STYLE: dict[str, str] = {
    "p018_diag036.png": "max-height:360px",
    "p019_diag037.png": "max-height:340px",
    "p021_fig1.png": "max-height:300px",
    "p021_fig2.png": "max-height:300px",
    "p022_fig1b.png": "max-height:260px",
    "p022_fig2b.png": "max-height:260px",
    "p029_tbl053.png": "max-height:200px",
    "p029_tbl054.png": "max-height:220px",
    "p032_diag059.png": "max-height:200px",
    "p035_diag065.png": "max-height:260px",
    "p041_tbl081.png": "max-height:280px",
    "p044_tbl089.png": "max-height:100px",
    "p045_tbl092.png": "max-height:340px",
    "p049_diag099.png": "max-height:220px",
}

KATEX_PRELOAD = """  <link rel="preload" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/fonts/KaTeX_Main-Regular.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/fonts/KaTeX_Math-Italic.woff2" as="font" type="font/woff2" crossorigin>
"""


def recrop_images() -> None:
    doc = fitz.open(PDF)
    CROPS.mkdir(parents=True, exist_ok=True)
    for page_idx, items in CROP_SPECS.items():
        page = doc[page_idx]
        for name, rect in items:
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
            path = CROPS / name
            pix.save(str(path))
            print(f"cropped {name} ({path.stat().st_size // 1024}KB)")


def patch_css(html: str) -> str:
    if "KaTeX_Main-Regular.woff2" not in html:
        html = html.replace(
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">',
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">\n'
            + KATEX_PRELOAD.rstrip(),
        )

    if ".formula-item" not in html:
        html = html.replace(
            "    .formula-row { gap: 14px; }\n"
            "    .formula-row > span { max-width: 100%; overflow-x: auto; }\n"
            "    img { max-width: 100%; height: auto; }\n"
            "    .katex { font-size: 1.02em; }\n"
            "    .katex-display { margin: 0.4em 0; overflow-x: auto; overflow-y: hidden; }",
            "    .formula-row { gap: 14px; align-items: flex-start; }\n"
            "    .formula-item { max-width: 100%; display: inline-block; vertical-align: top; background: none; }\n"
            "    img { max-width: 100%; height: auto; display: block; }\n"
            "    img.diag { width: 100%; object-fit: contain; margin: 8px 0; }\n"
            "    .katex, .katex * { background: transparent !important; }\n"
            "    .katex { font-size: 1.02em; line-height: 1.2; }\n"
            "    .katex-display {\n"
            "      margin: 0.4em 0; overflow-x: auto; overflow-y: hidden;\n"
            "      scrollbar-width: none;\n"
            "    }\n"
            "    .katex-display::-webkit-scrollbar { display: none; height: 0; }\n"
            "    .ans .katex { color: #c9a0a8; }",
        )

    toc_css = """    .toc-panel {
      left: 158px; top: 48px; width: 390px; height: 780px;
      background: rgba(255,255,255,.93); padding: 28px 18px 32px 18px;
      border-radius: 4px; overflow: hidden;
    }
    .toc-row {
      display: flex; align-items: flex-start; gap: 6px;
      margin-bottom: 10px; font-size: 9pt; line-height: 1.5;
    }
    .toc-badge {
      background: #d5d5d5; border-radius: 10px; padding: 3px 7px;
      font-weight: 700; font-size: 8pt; min-width: 52px; flex-shrink: 0;
      text-align: center;
    }
    .toc-title { flex: 1 1 auto; min-width: 0; word-break: keep-all; overflow-wrap: break-word; }
    .toc-dots { display: none; }
    .toc-page { font-weight: 700; min-width: 20px; flex-shrink: 0; text-align: right; padding-top: 1px; }"""

    html = re.sub(
        r"    \.toc-panel \{.*?\n    \.toc-page \{[^}]+\}",
        toc_css,
        html,
        count=1,
        flags=re.S,
    )
    return html


def fix_pages(html: str) -> str:
    parts = re.split(r'(<div class="page[^"]*" id="([^"]+)">)', html)
    out = [parts[0]]
    i = 1
    while i < len(parts):
        opener, page_id = parts[i], parts[i + 1]
        body = parts[i + 2] if i + 2 < len(parts) else ""

        if page_id == "page-002":
            body = (
                '\n  <div class="abs" style="left:0;right:0;top:42%;text-align:center;'
                'font-size:22pt;font-weight:700;">전기기사 실기</div>\n'
                '  <div class="abs" style="left:0;right:0;top:50%;text-align:center;'
                'font-size:28pt;font-weight:700;">단답비급</div>\n'
                '  <div class="cover-foot abs">전기치트키</div>\n'
            )

        if page_id in REMOVE_ALL_IMG_PAGES:
            body = re.sub(r"\s*<img\b[^>]*>\s*", "\n", body)

        elif page_id in PAGE_IMAGES:
            files = PAGE_IMAGES[page_id][:]

            def repl_img(_: re.Match[str]) -> str:
                if not files:
                    return ""
                name = files.pop(0)
                style = IMG_STYLE.get(name, "max-height:300px")
                return (
                    f'<img class="diag" src="../assets/images/manual/crops/{name}" '
                    f'style="{style};" alt="">'
                )

            body = re.sub(r"<img\b[^>]*>", repl_img, body)

        out.extend([opener, body])
        i += 3
    return "".join(out)


def fix_formulas(html: str) -> str:
    html = html.replace(r"\tan\theta", r"\tan \theta")
    html = html.replace(r"\cos^2\theta", r"\cos^2 \theta")
    html = re.sub(
        r'<span>\((\d)\) (\$[^$]+\$)</span>',
        r'<span class="formula-item">(\1) \2</span>',
        html,
    )
    return html


def main() -> None:
    print("Re-cropping diagram images from PDF...")
    recrop_images()

    html = HTML.read_text(encoding="utf-8")
    html = patch_css(html)
    html = fix_formulas(html)
    html = html.replace('<span class="toc-dots"></span>', "")
    html = fix_pages(html)

    HTML.write_text(html, encoding="utf-8")
    print("Patched HTML; embedding diagram images...")
    subprocess.run(["python3", str(ROOT / "scripts" / "embed_manual_assets.py")], check=True)

    final = HTML.read_text(encoding="utf-8")
    assert final.rstrip().endswith("</html>"), "HTML file truncated!"
    n_img = len(re.findall(r"<img\b", final))
    n_b64 = len(re.findall(r"data:image/png;base64,", final))
    print(f"Done: {HTML.stat().st_size // 1024}KB, {n_img} imgs ({n_b64} embedded)")


if __name__ == "__main__":
    main()
