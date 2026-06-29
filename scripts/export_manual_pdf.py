#!/usr/bin/env python3
"""Export dandap_manual.html to PDF via headless Chrome print."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output/dandap_manual.html"
OUT = ROOT / "output/dandap_manual.pdf"


def main() -> None:
    from playwright.sync_api import sync_playwright

    uri = HTML.resolve().as_uri()
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
        page.wait_for_timeout(800)
        page.pdf(
            path=str(OUT),
            width="595px",
            height="842px",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )
        browser.close()
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
