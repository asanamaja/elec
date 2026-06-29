#!/usr/bin/env python3
"""Insert assets/images/manual/{page}[-{n}].jpg into dandap_manual.html by filename."""
from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "assets/images/manual"
HTML = ROOT / "output/dandap_manual.html"

# Filename page -> HTML id page (footer). +1 where user crop label is one below footer.
HTML_PAGE = {
    135: 136,
    139: 140,
    140: 141,
    146: 147,
    147: 148,
    148: 149,
    158: 159,
    159: 160,
    160: 161,
}

IMG_TAG = re.compile(r"<img\b[^>]*>", re.DOTALL)
PAGE_BLOCK = re.compile(
    r'(<div class="page" id="page-(\d+)">)(.*?)(</div>\n</div>)',
    re.DOTALL,
)


def load_groups() -> dict[int, list[Path]]:
    groups: dict[int, list[tuple[int, Path]]] = defaultdict(list)
    for p in sorted(MANUAL.glob("*.jpg")):
        stem = p.stem
        if "-" in stem:
            page_s, num_s = stem.split("-", 1)
            groups[int(page_s)].append((int(num_s), p))
        else:
            groups[int(stem)].append((1, p))
    return {k: [path for _, path in sorted(v)] for k, v in groups.items()}


def enhance_image(src: Path) -> None:
    """Light cleanup so symbols/diagrams read clearly on white paper."""
    im = Image.open(src).convert("RGB")
    w, h = im.size
    if max(w, h) < 220:
        im = im.resize((w * 2, h * 2), Image.Resampling.LANCZOS)
    im = ImageOps.autocontrast(im, cutoff=1)
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Sharpness(im).enhance(1.15)
    im.save(src, format="JPEG", quality=92, optimize=True)


def img_tag(filename: str, kind: str = "diag", extra_style: str = "") -> str:
    base = "max-height:28px;width:auto;display:inline-block;vertical-align:middle;object-fit:contain;background:#fff;padding:1px 2px"
    if kind == "diag":
        base = "max-height:320px;width:100%;object-fit:contain;margin:8px 0;display:block"
    if extra_style:
        base = extra_style
    return (
        f'<img class="{kind}" src="../assets/images/manual/{filename}" '
        f'style="{base};" alt="" data-file="{filename}">'
    )


def sym_inline(filename: str) -> str:
    return img_tag(filename, "sym")


def replace_imgs_in_body(body: str, files: list[Path]) -> str:
    if not files:
        return body
    tags = list(IMG_TAG.finditer(body))
    if not tags:
        return body

    def make_tag(f: Path, old: str) -> str:
        if 'class="sym"' in old:
            return sym_inline(f.name)
        extra = ""
        if f.stem in {"139", "146"}:
            extra = "max-height:260px;width:100%;object-fit:contain;margin:8px 0;display:block"
        return img_tag(f.name, "diag", extra) if extra else img_tag(f.name, "diag")

    parts: list[str] = []
    last = 0
    for i, m in enumerate(tags):
        parts.append(body[last : m.start()])
        if i < len(files):
            parts.append(make_tag(files[i], m.group(0)))
        last = m.end()
    parts.append(body[last:])
    return "".join(parts)


def insert_page_041(body: str, files: list[Path]) -> str:
    grid = '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:8px 0;justify-items:center;">'
    for f in files:
        grid += img_tag(f.name, "diag", "max-height:120px;width:auto;object-fit:contain")
    grid += "</div>"
    return re.sub(
        r'<table class="tbl manual-table"[^>]*>.*?</table>',
        grid,
        body,
        count=1,
        flags=re.DOTALL,
    )


def insert_page_103(body: str, files: list[Path]) -> str:
    labels = ["(1) OCR", "(2) OVR", "(3) UVR", "(4) GR", "(5) DGR", "(6) PWR"]
    lines = []
    for i, f in enumerate(files):
        lab = labels[i] if i < len(labels) else f"({i+1})"
        lines.append(f'<p class="ans-line">{lab} : {sym_inline(f.name)}</p>')
    block = "\n      ".join(lines)
    return body.replace(
        '<p class="q-text">다음 각 계전기의 이름을 작성하시오.</p>',
        '<p class="q-text">다음 각 계전기의 이름을 작성하시오.</p>\n      ' + block,
        1,
    )


def insert_page_113(body: str, files: list[Path]) -> str:
    if len(files) < 10:
        return body
    syms265 = files[:6]
    la, pf, vtt, ctt = files[6:10]

    def repl_row265(m: re.Match[str]) -> str:
        nonlocal syms265
        if not syms265:
            return m.group(0)
        sym = syms265.pop(0)
        return f'<tr><td>{sym_inline(sym.name)}</td><td>{m.group(2)}</td><td>{m.group(3)}</td></tr>'

    body = re.sub(
        r"<tr><td>(DS|PF|CB|PT|CT|ZCT)</td><td>(<span class=\"ans\">[^<]+</span>)</td><td>(<span class=\"ans\">[^<]+</span>)</td></tr>",
        repl_row265,
        body,
        count=6,
    )

    row266 = (
        f"<tr><td>{sym_inline(la.name)}</td><td><span class=\"ans\">피뢰기</span></td>"
        f"<td>{sym_inline(vtt.name)}</td><td><span class=\"ans\">전압시험용 단자</span></td></tr>"
        f"<tr><td>{sym_inline(pf.name)}</td><td><span class=\"ans\">전력퓨즈</span></td>"
        f"<td>{sym_inline(ctt.name)}</td><td><span class=\"ans\">전류시험용 단자</span></td></tr>"
    )
    body = re.sub(
        r"<tr><td>(?:LA|PF|VTT|CTT|img class=\"sym\"[^>]*113-[78][^>]*>)[^<]*</td>.*?</tr>\s*"
        r"<tr><td>(?:LA|PF|VTT|CTT|img class=\"sym\"[^>]*113-[78][^>]*>)[^<]*</td>.*?</tr>",
        row266,
        body,
        count=1,
        flags=re.DOTALL,
    )
    return body


def insert_page_127(body: str, files: list[Path]) -> str:
    if not files:
        return body
    pic = img_tag(files[0].name, "diag", "max-height:220px;width:100%;object-fit:contain;margin:8px 0")
    return body.replace(
        "<p class=\"q-text\">UPS 장치 시스템의 중심부분을 구성하는 CVCF의 기본 회로를 보고 다음 각 물음에 답하시오.</p>",
        "<p class=\"q-text\">UPS 장치 시스템의 중심부분을 구성하는 CVCF의 기본 회로를 보고 다음 각 물음에 답하시오.</p>\n            " + pic,
        1,
    )


INSERTERS = {
    41: insert_page_041,
    103: insert_page_103,
    113: insert_page_113,
    127: insert_page_127,
}


def patch_colors(html: str) -> str:
    html = html.replace(".ans { color: #c9a0a8; }", ".ans { color: #d94848; }")
    html = html.replace(".ans .katex { color: #c9a0a8; }", ".ans .katex { color: #d94848; }")
    html = re.sub(
        r"(    \.q-num \{ font-size: [^;]+; font-weight: 700;)( margin-bottom:[^}]*)?(\s*\})",
        r"\1 color: #1a1a1a;\3",
        html,
        count=1,
    )
    html = re.sub(
        r"(    \.q-text \{ margin-bottom: [^;]+;)(\s*\})",
        r"\1 color: #1a1a1a;\2",
        html,
        count=1,
    )
    html = html.replace(
        "border-top: 0.8px solid #d4a0a8;",
        "border-top: 0.8px solid #e8a8a8;",
    )
    if "img.sym" in html and "background:#fff" not in html:
        html = html.replace(
            "    img.sym { max-height: 28px; width: auto; display: inline-block; vertical-align: middle; object-fit: contain; }",
            "    img.sym { max-height: 28px; width: auto; display: inline-block; vertical-align: middle; object-fit: contain; background: #fff; padding: 1px 2px; }",
        )
    html = re.sub(
        r"사진반영 [^<\"]+",
        "사진반영 20260629-named",
        html,
        count=1,
    )
    return html


def apply_html(groups: dict[int, list[Path]]) -> str:
    html = HTML.read_text(encoding="utf-8")

    def repl_page(m: re.Match[str]) -> str:
        opener, page_s, body, closer = m.group(1), m.group(2), m.group(3), m.group(4)
        page_num = int(page_s)

        file_page = None
        files: list[Path] = []
        for fp, flist in groups.items():
            if HTML_PAGE.get(fp, fp) == page_num:
                file_page = fp
                files = flist
                break

        if not files:
            return m.group(0)

        if page_num in INSERTERS and not IMG_TAG.search(body):
            body = INSERTERS[page_num](body, files)
        else:
            body = replace_imgs_in_body(body, files)
            # single photo for multi-slot pages: drop empty leftover imgs
            if len(files) == 1 and len(IMG_TAG.findall(body)) == 0:
                pass
            body = re.sub(r"<img\b[^>]*src=\"\"[^>]*>", "", body)

        return opener + body + closer

    html = PAGE_BLOCK.sub(repl_page, html)
    html = re.sub(r'src="data:image[^"]*"', 'src=""', html)
    html = re.sub(r"<img\b[^>]*Screenshot[^>]*>", "", html)
    html = patch_colors(html)
    return html


def main() -> None:
    groups = load_groups()
    print(f"Found {sum(len(v) for v in groups.values())} images on {len(groups)} pages")
    for flist in groups.values():
        for f in flist:
            enhance_image(f)
    html = apply_html(groups)
    HTML.write_text(html, encoding="utf-8")

    n_img = len(re.findall(r"<img\b", html))
    n_named = len(re.findall(r'data-file="', html))
    n_b64 = html.count("data:image")
    print(f"HTML: {n_img} images, {n_named} from manual/, base64={n_b64}")

    subprocess.run([sys.executable, str(ROOT / "scripts/build_symbols_view.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/fit_page_layout.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/export_manual_pdf.py")], check=True)


if __name__ == "__main__":
    main()
