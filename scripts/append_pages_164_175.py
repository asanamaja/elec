#!/usr/bin/env python3
"""Append pages 164-175, fix Q373 text, inject new diagram crops, refresh embeds."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from pages_164_175 import PAGES_164_175

HTML = ROOT / "output" / "dandap_manual.html"

IMG_EXTRA: dict[str, tuple[str, str, str]] = {
    "p170_table385": ("p170_table385.png", "diag", "max-height:150px"),
    "p171_table387": ("p171_table387.png", "diag", "max-height:320px"),
}

Q373_OLD = (
    "      <p class=\"q-text\">시운전 완료 후 발주자에게 인계하여야 할 사항(서류 등)을 5가지만 쓰시오.</p>"
)
Q373_NEW = """      <p class="q-text">감리원은 공사 완료 후 준공검사 전에 사전 시운전 등이 필요한 부분에 대하여는 공사업자에게 시운전을 위한 계획을 수립하여 시운전에 입회할 수 있다. 이에 따른 <strong>시운전 완료 후 성과물</strong>을 공사업자로부터 제출받아 검토한 후 <strong>발주자에게 인계하여야 할 사항(서류 등)을 5가지</strong>만 쓰시오.</p>"""


def inject_placeholders(html: str) -> str:
    def repl(m: re.Match[str]) -> str:
        key = m.group(1)
        if key not in IMG_EXTRA:
            return m.group(0)
        fname, cls, style = IMG_EXTRA[key]
        return (
            f'<img class="{cls}" src="../assets/images/manual/crops/{fname}" '
            f'style="{style};" alt="">'
        )

    return re.sub(r"<!--IMG:([\w]+)-->", repl, html)


def main() -> None:
    subprocess.run([sys.executable, str(ROOT / "scripts/crop_all_diagrams.py")], check=True)

    html = HTML.read_text(encoding="utf-8")
    html = html.replace(Q373_OLD, Q373_NEW)

    if 'id="page-164"' not in html:
        marker = "\n</div>\n\n<script defer src="
        html = html.replace(marker, PAGES_164_175 + marker, 1)

    html = inject_placeholders(html)
    html = html.replace(
        '<span id="pg-info">p.1–163 완료 · 직접 전사</span>',
        '<span id="pg-info">p.1–175 완료 · 직접 전사</span>',
    )
    HTML.write_text(html, encoding="utf-8")

    subprocess.run([sys.executable, str(ROOT / "scripts/refresh_embedded_crops.py")], check=True)

    final = HTML.read_text(encoding="utf-8")
    n_pages = len(re.findall(r'id="page-\d+"', final))
    n_q = len(re.findall(r'<div class="q-num">', final))
    print(f"Done: {n_pages} pages, {n_q} questions")


if __name__ == "__main__":
    main()
