#!/usr/bin/env python3
"""Detect overflowing manual pages and apply compact/dense/ultra density classes."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output/dandap_manual.html"

# Available vertical space inside a page for .content (px at 595x842 layout)
CONTENT_TOP = 118
FOOT_SAFE = 72  # keep clear of footer
MAX_H = 842 - CONTENT_TOP - FOOT_SAFE

DENSITY_ORDER = ["", "compact", "dense", "ultra"]


def patch_css(html: str) -> str:
  """Replace clipping CSS with fit-oriented density tiers."""
  html = re.sub(
    r"\.content \{ overflow: hidden; max-height: calc\(842px - 172px\); \}\n?",
    "",
    html,
  )
  html = re.sub(
    r"overflow: hidden; max-height: calc\(842px - 172px\); ",
    "",
    html,
  )

  if ".content.dense" not in html:
    insert = """
    /* Page-fit density tiers (no clipping — shrink to fit) */
    .content.compact { font-size: 9.6pt; line-height: 1.46; }
    .content.compact .q { margin-bottom: 12px; }
    .content.compact .q-num { font-size: 12pt; }
    .content.compact .q-hline { margin: 2px 0 5px; }
    .content.compact .q-text { margin-bottom: 4px; }
    .content.compact .ans-line { margin: 1px 0; }
    .content.compact .formula { margin: 4px 0; font-size: 9.2pt; }
    .content.compact .katex-display { margin: 0.2em 0; }
    .content.compact .box { font-size: 9pt; padding: 5px 7px; line-height: 1.5; }
    .content.compact img.diag { margin: 4px 0; }

    .content.dense { font-size: 9.1pt; line-height: 1.38; }
    .content.dense .q { margin-bottom: 8px; }
    .content.dense .q-num { font-size: 11.5pt; }
    .content.dense .q-hline { margin: 1px 0 4px; }
    .content.dense .q-text { margin-bottom: 3px; }
    .content.dense .ans-line { margin: 0; }
    .content.dense .formula { margin: 2px 0; font-size: 8.8pt; }
    .content.dense .katex-display { margin: 0.1em 0; }
    .content.dense .katex { font-size: 0.95em; }
    .content.dense .box { font-size: 8.6pt; padding: 4px 6px; line-height: 1.42; }
    .content.dense img.diag { margin: 2px 0; }

    .content.ultra { font-size: 8.6pt; line-height: 1.32; }
    .content.ultra .q { margin-bottom: 5px; }
    .content.ultra .q-num { font-size: 11pt; }
    .content.ultra .q-hline { margin: 1px 0 3px; }
    .content.ultra .q-text { margin-bottom: 2px; }
    .content.ultra .ans-line { margin: 0; }
    .content.ultra .formula { margin: 1px 0; font-size: 8.3pt; }
    .content.ultra .katex-display { margin: 0; }
    .content.ultra .katex { font-size: 0.9em; }
    .content.ultra .box { font-size: 8.2pt; padding: 3px 5px; line-height: 1.35; }
    .content.ultra img.diag { margin: 1px 0; }
    .content.ultra table.tbl { font-size: 8.4pt; margin-top: 4px; }
    .content.ultra table.tbl th, .content.ultra table.tbl td { padding: 3px 4px; }

    /* Cover title — prevent vertical wrap */
    .title-box { width: 96px; height: 236px; }
    .title-box .vtext { font-size: 30pt; letter-spacing: .08em; }
"""
    html = html.replace("    @media print {", insert + "\n    @media print {")

  # Remove duplicate compact rules from prior patch if present
  html = re.sub(
    r"    \.content\.compact \{ font-size: 9\.2pt; line-height: 1\.42; \}\n"
    r"    \.content\.compact \.q \{ margin-bottom: 10px; \}\n",
    "",
    html,
  )
  return html


def apply_density(html: str, page_id: str, level: str) -> str:
  pat = re.compile(
    rf'(<div class="page" id="{re.escape(page_id)}">.*?<div class=")([^"]*)(")',
    re.DOTALL,
  )

  def repl(m: re.Match[str]) -> str:
    parts = m.group(2).split()
    kept = [p for p in parts if p not in ("compact", "dense", "ultra")]
    if not kept or kept[0] != "content":
      kept = ["content"] + [p for p in kept if p != "content"]
    if level:
      kept.append(level)
    return f'{m.group(1)}{" ".join(kept)}{m.group(3)}'

  return pat.sub(repl, html, count=1)


def measure_and_fit(html_path: Path) -> dict[str, str]:
  from playwright.sync_api import sync_playwright

  html_uri = html_path.resolve().as_uri()
  results: dict[str, str] = {}

  with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 800, "height": 1200})
    page.goto(html_uri, wait_until="networkidle")
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
    page.wait_for_function(
      """() => {
        const formulas = document.querySelectorAll('p.formula');
        if (!formulas.length) return true;
        return [...formulas].every(
          el => el.querySelector('.katex') || !/\\$\\$/.test(el.textContent || '')
        );
      }""",
      timeout=45000,
    )
    page.wait_for_timeout(400)

    page_ids = page.eval_on_selector_all(
      ".page",
      "els => els.map(e => e.id)",
    )

    for pid in page_ids:
      if not pid:
        continue
      pg_num = int(pid.split("-")[1])
      if pg_num <= 4:
        continue

      best = ""
      for level in DENSITY_ORDER:
        page.evaluate(
          """([pid, level]) => {
            const pg = document.getElementById(pid);
            if (!pg) return;
            const c = pg.querySelector('.content');
            if (!c) return;
            for (const d of ['compact','dense','ultra']) c.classList.remove(d);
            if (level) c.classList.add(level);
          }""",
          [pid, level],
        )
        page.wait_for_timeout(80)
        overflow = page.evaluate(
          """(pid) => {
            const pg = document.getElementById(pid);
            const c = pg?.querySelector('.content');
            if (!c) return false;
            const pgRect = pg.getBoundingClientRect();
            const kids = [...c.querySelectorAll('.q, .memo-label, .box, table, img.diag, p.q-text, p.formula')];
            let bottom = c.getBoundingClientRect().top;
            if (kids.length) {
              for (const k of kids) bottom = Math.max(bottom, k.getBoundingClientRect().bottom);
            } else {
              bottom = c.getBoundingClientRect().bottom;
            }
            const limit = pgRect.bottom - 50;
            return bottom > limit + 0.5;
          }""",
          pid,
        )
        if not overflow:
          best = level
          break
        best = level

      if best:
        results[pid] = best

    browser.close()

  return results


def main() -> None:
  from apply_page_fit_patch import patch

  html = HTML.read_text(encoding="utf-8")
  html = patch(html)
  html = patch_css(html)
  HTML.write_text(html, encoding="utf-8")

  print("Measuring page overflow...")
  levels = measure_and_fit(HTML)

  html = HTML.read_text(encoding="utf-8")
  for pid, level in sorted(levels.items()):
    html = apply_density(html, pid, level)
  HTML.write_text(html, encoding="utf-8")

  counts: dict[str, int] = {}
  for lv in levels.values():
    counts[lv or "normal"] = counts.get(lv or "normal", 0) + 1
  print("Density applied:", counts)
  still = [pid for pid, lv in levels.items() if lv == "ultra"]
  if still:
    print("Still ultra-dense (may need content split):", len(still), still[:10])


if __name__ == "__main__":
  main()
