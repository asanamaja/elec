#!/usr/bin/env python3
"""Audit all manual pages for header/content overlap and apply fixes."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output/dandap_manual.html"
REPORT = ROOT / "output/overlap_audit.json"

# Minimum content top (px) by header layout inside a page
TOP_RULES = {
    "day+sec": 140,   # day-tag + sec-title
    "sec": 128,       # sec-title only (brand pages)
    "day": 76,        # day-tag only
    "brand": 76,      # brand only (right-footer pages)
    "none": 72,       # minimal header
}

HEADER_REPAIR = [
    (re.compile(r'<div class="content\s+(day-tag[^"]*)">'), r'<div class="\1">'),
    (re.compile(r'<div class="content\s+(brand[^"]*)">'), r'<div class="\1">'),
    (re.compile(r'<div class="content\s+(sec-title[^"]*)">'), r'<div class="\1">'),
    (re.compile(r'<div class="(day-tag[^"]*)\s+compact([^"]*)">'), r'<div class="\1\2">'),
    (re.compile(r'<div class="(day-tag[^"]*)\s+dense([^"]*)">'), r'<div class="\1\2">'),
    (re.compile(r'<div class="(day-tag[^"]*)\s+ultra([^"]*)">'), r'<div class="\1\2">'),
    (re.compile(r'<div class="(brand[^"]*)\s+compact([^"]*)">'), r'<div class="\1\2">'),
    (re.compile(r'<div class="(brand[^"]*)\s+dense([^"]*)">'), r'<div class="\1\2">'),
    (re.compile(r'<div class="(brand[^"]*)\s+ultra([^"]*)">'), r'<div class="\1\2">'),
]


def repair_headers(html: str) -> tuple[str, int]:
    n = 0
    for pat, repl in HEADER_REPAIR:
        html, c = pat.subn(repl, html)
        n += c
    return html, n


def page_layout(html: str, page_id: str) -> str:
    m = re.search(
        rf'<div class="page" id="{re.escape(page_id)}">(.*?)</div>\s*\n</div>',
        html,
        re.DOTALL,
    )
    if not m:
        return "none"
    block = m.group(1)
    has_day = 'class="day-tag' in block
    has_sec = 'class="sec-title' in block
    has_brand = 'class="brand abs"' in block
    if has_day and has_sec:
        return "day+sec"
    if has_sec:
        return "sec"
    if has_day:
        return "day"
    if has_brand:
        return "brand"
    return "none"


def set_content_top(html: str, page_id: str, top: int) -> str:
    pat = re.compile(
        rf'(<div class="page" id="{re.escape(page_id)}">.*?<div class="content[^"]*")([^>]*)(>)',
        re.DOTALL,
    )

    def repl(m: re.Match[str]) -> str:
        attrs = m.group(2)
        attrs = re.sub(r'\s*style="[^"]*"', "", attrs)
        return f'{m.group(1)}{attrs} style="top:{top}px;">'

    return pat.sub(repl, html, count=1)


def measure_overlaps(html_path: Path) -> list[dict]:
    from playwright.sync_api import sync_playwright

    uri = html_path.resolve().as_uri()
    issues: list[dict] = []

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 595, "height": 842})
        page.goto(uri, wait_until="networkidle")
        page.evaluate(
            """async () => {
              if (typeof renderMathInElement === 'function') {
                renderMathInElement(document.body, {
                  delimiters: [
                    { left: '$$', right: '$$', display: true },
                    { left: '$', right: '$', display: false }
                  ],
                  throwOnError: false
                });
              }
              await document.fonts.ready;
            }"""
        )
        page.wait_for_timeout(600)

        rows = page.evaluate(
            """() => {
              const out = [];
              for (const pg of document.querySelectorAll('.page')) {
                const id = pg.id;
                if (!id) continue;
                const num = parseInt(id.split('-')[1], 10);
                if (num <= 4) continue;
                const content = pg.querySelector('.content');
                if (!content) continue;
                const pgRect = pg.getBoundingClientRect();
                const headers = [...pg.querySelectorAll('.day-tag, .sec-title, .brand')];
                const cTop = content.getBoundingClientRect().top - pgRect.top;
                const cStyle = content.getAttribute('style') || '';
                let worst = 0;
                let hit = '';
                for (const h of headers) {
                  const hb = h.getBoundingClientRect().bottom - pgRect.top;
                  const overlap = hb - cTop + 2;
                  if (overlap > worst) {
                    worst = overlap;
                    hit = h.className;
                  }
                }
                const kids = [...content.querySelectorAll('.q, .box, table, img.diag, .memo-label')];
                let bottom = cTop;
                for (const k of kids) {
                  bottom = Math.max(bottom, k.getBoundingClientRect().bottom - pgRect.top);
                }
                const footLimit = pgRect.height - 48;
                const footOverflow = bottom - footLimit;
                out.push({
                  id, num, cTop: Math.round(cTop), style: cStyle,
                  headerOverlap: Math.round(worst * 10) / 10,
                  headerHit: hit,
                  footOverflow: Math.round(footOverflow * 10) / 10,
                });
              }
              return out;
            }"""
        )
        issues = rows
        browser.close()

    return issues


def parse_content_top(style: str) -> int | None:
    m = re.search(r"top:\s*(\d+)px", style)
    return int(m.group(1)) if m else None


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    html, repaired = repair_headers(html)
    print(f"Repaired {repaired} corrupted header divs")

  # Apply layout-based minimum tops
    page_ids = re.findall(r'id="(page-\d+)"', html)
    tops_applied = 0
    for pid in page_ids:
        num = int(pid.split("-")[1])
        if num <= 4:
            continue
        layout = page_layout(html, pid)
        min_top = TOP_RULES[layout]
        html = set_content_top(html, pid, min_top)
        tops_applied += 1
    print(f"Set content top for {tops_applied} pages")

    HTML.write_text(html, encoding="utf-8")

    print("Measuring overlaps...")
    rows = measure_overlaps(HTML)

    # Bump top for pages still overlapping (page-relative px, not viewport coords)
    html = HTML.read_text(encoding="utf-8")
    fixed_overlap = 0
    for row in rows:
        if row["headerOverlap"] > 1:
            cur = parse_content_top(row["style"]) or TOP_RULES[page_layout(html, row["id"])]
            new_top = cur + int(row["headerOverlap"]) + 4
            html = set_content_top(html, row["id"], new_top)
            fixed_overlap += 1
    if fixed_overlap:
        HTML.write_text(html, encoding="utf-8")
        print(f"Bumped top on {fixed_overlap} pages with residual overlap")
        rows = measure_overlaps(HTML)

    still_header = [r for r in rows if r["headerOverlap"] > 1]
    still_foot = [r for r in rows if r["footOverflow"] > 1]

    REPORT.write_text(
        json.dumps(
            {"header": still_header, "footer": still_foot, "all": rows},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    print(f"Header overlap remaining: {len(still_header)}")
    if still_header[:8]:
        for r in still_header[:8]:
            print(f"  {r['id']}: overlap {r['headerOverlap']}px ({r['headerHit']})")
    print(f"Footer overflow remaining: {len(still_foot)}")
    if still_foot[:8]:
        for r in still_foot[:8]:
            print(f"  {r['id']}: foot +{r['footOverflow']}px")


if __name__ == "__main__":
    main()
