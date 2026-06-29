#!/usr/bin/env python3
"""Insert assets/images/manual/{page}[-{n}].jpg into dandap_manual.html by filename."""
from __future__ import annotations

import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from table_styles import CELL, TABLE_STYLE, TH  # noqa: E402

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


def sym_inline(filename: str) -> str:
    return (
        f'<img class="sym" src="../assets/images/manual/{filename}" '
        f'style="max-height:32px;width:auto;display:inline-block;vertical-align:middle;'
        f'object-fit:contain;" alt="" data-file="{filename}">'
    )


def img_tag(filename: str, kind: str = "diag", extra_style: str = "") -> str:
    if kind == "sym":
        return sym_inline(filename)
    base = "max-height:320px;width:100%;object-fit:contain;margin:8px 0;display:block"
    if extra_style:
        base = extra_style
    return (
        f'<img class="diag" src="../assets/images/manual/{filename}" '
        f'style="{base};" alt="" data-file="{filename}">'
    )


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
    names = ["400[W] 수은등", "F40×2", "F32×2", "비상용 형광등"]
    rows = ""
    for name, f in zip(names, files):
        rows += (
            f'<tr><td style="{CELL}">{name}</td>'
            f'<td style="{CELL}">{sym_inline(f.name)}</td></tr>'
        )
    table = (
        f'<table class="tbl manual-table" style="{TABLE_STYLE}">'
        f'<thead><tr><th style="{TH}">명칭</th><th style="{TH}">기호</th></tr></thead>'
        f"<tbody>{rows}</tbody></table>"
    )
    body = re.sub(
        r'<div style="display:grid[^"]*"[^>]*>.*?</div>',
        table,
        body,
        count=1,
        flags=re.DOTALL,
    )
    body = re.sub(
        r'<table class="tbl manual-table"[^>]*>.*?</table>',
        table,
        body,
        count=1,
        flags=re.DOTALL,
    )
    if table not in body:
        body = body.replace(
            "<p class=\"q-text\">아래 조명의 명칭에 따른 기호를 그리시오.</p>",
            "<p class=\"q-text\">아래 조명의 명칭에 따른 기호를 그리시오.</p>\n      " + table,
            1,
        )
    return body


def insert_page_103(body: str, files: list[Path]) -> str:
    labels = ["(1) OCR", "(2) OVR", "(3) UVR", "(4) GR", "(5) DGR", "(6) PWR"]
    answers = [
        "과전류 계전기",
        "과전압 계전기",
        "부족전압 계전기",
        "지락 계전기",
        "방향 지락 계전기",
        "전력 계전기",
    ]
    sym_rows = ""
    for i in range(0, 6, 2):
        sym_rows += (
            f"<tr><td style=\"{CELL}\">{labels[i]}<br>{sym_inline(files[i].name)}</td>"
            f"<td style=\"{CELL}\">{labels[i + 1]}<br>{sym_inline(files[i + 1].name)}</td></tr>"
        )
    sym_table = (
        f'<table class="tbl manual-table" style="{TABLE_STYLE}">'
        f"<tbody>{sym_rows}</tbody></table>"
    )
    ans_lines = [
        f'<p class="ans-line">{labels[0]} : <span class="ans">{answers[0]}</span>'
        f" &nbsp; {labels[1]} : <span class=\"ans\">{answers[1]}</span></p>",
        f'<p class="ans-line">{labels[2]} : <span class="ans">{answers[2]}</span>'
        f" &nbsp; {labels[3]} : <span class=\"ans\">{answers[3]}</span></p>",
        f'<p class="ans-line">{labels[4]} : <span class="ans">{answers[4]}</span>'
        f" &nbsp; {labels[5]} : <span class=\"ans\">{answers[5]}</span></p>",
    ]
    block = sym_table + "\n      " + "\n      ".join(ans_lines)
    return re.sub(
        r'(<p class="q-text">다음 각 계전기의 이름을 작성하시오.</p>).*?(?=\s*<div class="q">\s*<div class="q-num">244)',
        r"\1\n      " + block + "\n    </div>\n    ",
        body,
        count=1,
        flags=re.DOTALL,
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
    if IMG_TAG.search(body):
        return replace_imgs_in_body(body, files[:1])
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
    html = re.sub(
        r"사진반영 [^<\"]+",
        "사진반영 20260629-fidelity",
        html,
        count=1,
    )
    html = re.sub(
        r'<meta name="build" content="[^"]*">',
        '<meta name="build" content="20260629-fidelity">',
        html,
        count=1,
    )
    return html


def apply_html(groups: dict[int, list[Path]]) -> str:
    html = HTML.read_text(encoding="utf-8")

    def repl_page(m: re.Match[str]) -> str:
        opener, page_s, body, closer = m.group(1), m.group(2), m.group(3), m.group(4)
        page_num = int(page_s)

        files: list[Path] = []
        for fp, flist in groups.items():
            if HTML_PAGE.get(fp, fp) == page_num:
                files = flist
                break

        if not files:
            return m.group(0)

        if page_num in INSERTERS:
            body = INSERTERS[page_num](body, files)
        elif IMG_TAG.search(body):
            body = replace_imgs_in_body(body, files)
            body = re.sub(r"<img\b[^>]*src=\"\"[^>]*>", "", body)

        return opener + body + closer

    html = PAGE_BLOCK.sub(repl_page, html)
    html = re.sub(r'src="data:image[^"]*"', 'src=""', html)
    html = re.sub(r"<img\b[^>]*Screenshot[^>]*>", "", html)
    return patch_colors(html)


def main() -> None:
    groups = load_groups()
    print(f"Found {sum(len(v) for v in groups.values())} images on {len(groups)} pages")
    html = apply_html(groups)
    HTML.write_text(html, encoding="utf-8")

    n_img = len(re.findall(r"<img\b", html))
    n_named = len(re.findall(r'data-file="', html))
    print(f"HTML: {n_img} images, {n_named} from manual/, base64={html.count('data:image')}")

    subprocess.run([sys.executable, str(ROOT / "scripts/sync_pdf_fidelity.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/build_symbols_view.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/fit_page_layout.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/export_manual_pdf.py")], check=True)


if __name__ == "__main__":
    main()
