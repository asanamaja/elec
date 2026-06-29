#!/usr/bin/env python3
"""Safe layout patches for dandap_manual.html (no giant-line edits)."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output/dandap_manual.html"

# Remove clipping — content must shrink to fit, never hide overflow
REMOVE_CLIP = re.compile(
    r"\n\s*\.content \{ overflow: hidden; max-height: calc\(842px - 172px\); \}\n?",
)

DENSITY_CSS = """
    /* Page-fit density tiers (no clipping) */
    .content.compact { font-size: 9.5pt; line-height: 1.44; }
    .content.compact .q { margin-bottom: 11px; }
    .content.compact .q-num { font-size: 12pt; }
    .content.compact .q-hline { margin: 2px 0 5px; }
    .content.compact .q-text { margin-bottom: 4px; }
    .content.compact .ans-line { margin: 1px 0; }
    .content.compact .formula { margin: 4px 0; font-size: 9.1pt; }
    .content.compact .katex-display { margin: 0.15em 0; }
    .content.compact .box { font-size: 9pt; padding: 5px 7px; line-height: 1.48; }
    .content.compact img.diag { margin: 4px 0; }

    .content.dense { font-size: 9.0pt; line-height: 1.36; }
    .content.dense .q { margin-bottom: 7px; }
    .content.dense .q-num { font-size: 11.5pt; }
    .content.dense .q-hline { margin: 1px 0 3px; }
    .content.dense .q-text { margin-bottom: 2px; }
    .content.dense .ans-line { margin: 0; }
    .content.dense .formula { margin: 2px 0; font-size: 8.7pt; }
    .content.dense .katex-display { margin: 0.05em 0; }
    .content.dense .katex { font-size: 0.94em; }
    .content.dense .box { font-size: 8.5pt; padding: 4px 6px; line-height: 1.38; }
    .content.dense img.diag { margin: 2px 0; }

    .content.ultra { font-size: 8.5pt; line-height: 1.30; }
    .content.ultra .q { margin-bottom: 4px; }
    .content.ultra .q-num { font-size: 11pt; }
    .content.ultra .q-hline { margin: 1px 0 2px; }
    .content.ultra .q-text { margin-bottom: 1px; }
    .content.ultra .ans-line { margin: 0; }
    .content.ultra .formula { margin: 1px 0; font-size: 8.2pt; }
    .content.ultra .katex-display { margin: 0; }
    .content.ultra .katex { font-size: 0.88em; }
    .content.ultra .box { font-size: 8.1pt; padding: 3px 5px; line-height: 1.32; }
    .content.ultra img.diag { margin: 1px 0; }
    .content.ultra table.tbl { font-size: 8.3pt; margin-top: 3px; }
    .content.ultra table.tbl th, .content.ultra table.tbl td { padding: 2px 4px; }

    /* Cover — keep vertical title on one line */
    .title-box { width: 92px; height: 228px; }
    .title-box .vtext { font-size: 30pt; letter-spacing: .06em; }
"""

OLD_COMPACT = re.compile(
    r"    \.content\.compact \{ font-size: 9\.[26]pt; line-height: 1\.4[28]; \}\n"
    r"    \.content\.compact \.q \{ margin-bottom: (?:10|14)px; \}\n"
    r"(?:    \.content\.compact \.box \{ font-size: 9pt; padding: 6px 8px; \}\n)?",
)


def repair_density_classes(html: str) -> str:
    html = html.replace('class="contentcompact"', 'class="content compact"')
    html = html.replace('class="contentdense"', 'class="content dense"')
    html = html.replace('class="contentultra"', 'class="content ultra"')
    html = re.sub(
        r'class="content(compact|dense|ultra)(\s[^"]*)?"',
        r'class="content \1\2"',
        html,
    )
    return html


def patch(html: str) -> str:
    html = repair_density_classes(html)
    html = REMOVE_CLIP.sub("\n", html)
    html = OLD_COMPACT.sub("", html)

    if ".content.ultra" not in html:
        html = html.replace("    @media print {", DENSITY_CSS + "\n    @media print {")

    # Cover typography
    html = html.replace(
        ".title-box .vtext { font-size: 38pt; font-weight: 700; }",
        ".title-box .vtext { font-size: 30pt; font-weight: 700; letter-spacing: .06em; }",
    )
    html = html.replace(
        'style="left:0;right:0;top:50%;text-align:center;font-size:28pt;font-weight:700;">단답비급',
        'style="left:0;right:0;top:50%;text-align:center;font-size:24pt;font-weight:700;letter-spacing:.04em;">단답비급',
    )

    # KaTeX-friendly formula on p.16 (HTML entities break auto-render)
    html = html.replace(
        '<p class="formula">$$5\\omega L &gt; \\frac{1}{5\\omega C} \\Rightarrow \\omega L &gt; \\frac{1}{5^2\\omega C} = 0.04 \\times \\frac{1}{\\omega C}$$</p>',
        '<p class="formula">$$5\\omega L > \\frac{1}{5\\omega C} \\Rightarrow \\omega L > \\frac{1}{5^{2}\\omega C} = 0.04 \\times \\frac{1}{\\omega C}$$</p>',
    )

    # Tighten duplicate Q034 follow-up spacing
    html = html.replace(
        '<p class="q-text" style="margin-top:6px;">제3고조파를 감소시키기 위한',
        '<p class="q-text" style="margin-top:2px;">제3고조파를 감소시키기 위한',
    )

    return html


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    before = len(html)
    html = patch(html)
    HTML.write_text(html, encoding="utf-8")
    pages = len(re.findall(r'id="page-', html))
    print(f"Patched {HTML} ({pages} pages, {before} -> {len(html)} bytes)")


if __name__ == "__main__":
    main()
