#!/usr/bin/env python3
"""Embed manual crop images as base64 data URIs in dandap_manual.html."""
import base64
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"
CROPS = ROOT / "assets" / "images" / "manual" / "crops"


def mime(path: Path) -> str:
    return "image/png" if path.suffix.lower() == ".png" else "image/jpeg"


def to_data_uri(path: Path) -> str:
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime(path)};base64,{data}"


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    pattern = re.compile(
        r'src="(\.\./assets/images/manual/crops/([^"]+))"'
    )
    cache: dict[str, str] = {}
    count = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal count
        rel, name = m.group(1), m.group(2)
        if name not in cache:
            path = CROPS / name
            if not path.exists():
                raise FileNotFoundError(path)
            cache[name] = to_data_uri(path)
            count += 1
        return f'src="{cache[name]}" data-crop="{name}"'

    html = pattern.sub(repl, html)
    HTML.write_text(html, encoding="utf-8")
    print(f"Embedded {count} images into {HTML}")


if __name__ == "__main__":
    main()
