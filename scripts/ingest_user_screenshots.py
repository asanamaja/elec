#!/usr/bin/env python3
"""Map random-named user screenshots to manual symbols and diagram crops."""
from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
USER = ROOT / "assets/images/manual/user"
CROPS = ROOT / "assets/images/manual/crops"
SYM = USER

# Extra top trim for images that still show page/header bleed
TOP_TRIM = {
    "Screenshot_20260628_230310_Samsung Notes (2).jpg": 0.22,
    "Screenshot_20260628_230313_Samsung Notes.jpg": 0.14,
}

# Skip question-text band below top trim (duct row only)
DUCT_BAND_SKIP = 0.42

SHOT = USER / "Screenshot_20260628_{name}_Samsung Notes{suffix}.jpg"


def path_for(name: str, suffix: str = "") -> Path:
    p = SHOT.parent / f"Screenshot_20260628_{name}_Samsung Notes{suffix}.jpg"
    if p.exists():
        return p
    raise FileNotFoundError(p)


def open_img(path: Path) -> Image.Image:
    im = Image.open(path)
    if im.mode not in ("RGB", "RGBA"):
        im = im.convert("RGB")
    return im


def trim_top(im: Image.Image, ratio: float) -> Image.Image:
    w, h = im.size
    y0 = max(0, int(h * ratio))
    return im.crop((0, y0, w, h))


def trim_symbol_top(im: Image.Image, ratio: float = 0.06) -> Image.Image:
    w, h = im.size
    y0 = max(0, int(h * ratio))
    return im.crop((0, y0, w, h))


def split_cols(im: Image.Image, n: int, pad: float = 0.02) -> list[Image.Image]:
    w, h = im.size
    out = []
    for i in range(n):
        x0 = int((w / n) * i + w * pad / n)
        x1 = int((w / n) * (i + 1) - w * pad / n)
        out.append(im.crop((x0, 0, x1, h)))
    return out


def split_rows(im: Image.Image, n: int, pad: float = 0.04) -> list[Image.Image]:
    w, h = im.size
    out = []
    for i in range(n):
        y0 = int((h / n) * i + h * pad / n)
        y1 = int((h / n) * (i + 1) - h * pad / n)
        out.append(im.crop((0, y0, w, y1)))
    return out


def save_png(im: Image.Image, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if im.mode != "RGB":
        im = im.convert("RGB")
    im.save(dest, format="PNG", optimize=True)


def save_sym(name: str, im: Image.Image) -> None:
    save_png(im, SYM / name)


def save_crop(name: str, im: Image.Image) -> None:
    save_png(im, CROPS / name)


def maybe_top_trim(path: Path, im: Image.Image) -> Image.Image:
    ratio = TOP_TRIM.get(path.name, 0)
    return trim_top(im, ratio) if ratio else im


def process_symbols() -> int:
    n = 0

    mapping = [
        ("230306", "", "sym_2p.png", lambda im: im.crop((0, 0, im.width // 2, im.height))),
        ("230306", " (1)", "sym_4w.png", None),
        ("230306", " (2)", "sym_outlet.png", None),
        ("230306", " (3)", "sym_2gang.png", None),
        ("230306", " (2) (2)", "sym_3p_out.png", None),
        ("230042", "", "sym_outdoor.png", None),
        ("230051", "", "sym_ceiling.png", None),
        ("230306", " (2) (1)", "sym_floor.png", lambda im: split_rows(im, 2)[1]),
    ]

    # sym_sw — flasher dot from 2P crop circle
    p2p = SHOT.parent / "Screenshot_20260628_230306_Samsung Notes.jpg"
    if p2p.exists():
        im = open_img(p2p)
        w, h = im.size
        save_sym("sym_sw.png", im.crop((0, 0, w // 2, h)))
        n += 1
        print("sym sym_sw.png <-", p2p.name)

    for stamp, suffix, out, fn in mapping:
        p = SHOT.parent / f"Screenshot_20260628_{stamp}_Samsung Notes{suffix}.jpg"
        if not p.exists():
            print("skip missing", p.name)
            continue
        im = maybe_top_trim(p, open_img(p))
        part = fn(im) if fn else im
        save_sym(out, part)
        n += 1
        print("sym", out, "<-", p.name)

    # HID stack -> 3 symbols
    p4 = SHOT.parent / "Screenshot_20260628_230306_Samsung Notes (4).jpg"
    if p4.exists():
        im = trim_top(open_img(p4), 0.08)
        for i, name in enumerate(["sym_h400.png", "sym_m400.png", "sym_n400.png"]):
            row = split_rows(im, 3)[i]
            save_sym(name, row)
            n += 1
            print("sym", name, "<-", p4.name, f"row{i+1}")

    # Switch 368
    p368 = SHOT.parent / "Screenshot_20260628_230310_Samsung Notes (1).jpg"
    if p368.exists():
        save_sym("sym_switch_368.png", trim_top(open_img(p368), 0.06))
        n += 1
        print("sym sym_switch_368.png <-", p368.name)

    # Duct row MD LD F7 — extra top trim
    pduct = SHOT.parent / "Screenshot_20260628_230310_Samsung Notes (2).jpg"
    if pduct.exists():
        im = trim_top(open_img(pduct), TOP_TRIM[pduct.name])
        w, h = im.size
        band = im.crop((0, int(h * DUCT_BAND_SKIP), w, h))
        for part, name in zip(split_cols(band, 3, pad=0.03), ["sym_md.png", "sym_ld.png", "sym_f7.png"]):
            save_sym(name, trim_symbol_top(part, 0.08))
            n += 1
            print("sym", name, "<-", pduct.name)

    # Transformer symbols — extra top trim on TB/TN/TH stack
    ptr = SHOT.parent / "Screenshot_20260628_230313_Samsung Notes.jpg"
    if ptr.exists():
        im = trim_top(open_img(ptr), TOP_TRIM[ptr.name])
        for part, name in zip(split_rows(im, 3, pad=0.03), ["sym_tr_tb.png", "sym_tr_tn.png", "sym_tr_th.png"]):
            save_sym(name, trim_symbol_top(part, 0.06))
            n += 1
            print("sym", name, "<-", ptr.name)

    ptr2 = SHOT.parent / "Screenshot_20260628_230313_Samsung Notes (1).jpg"
    if ptr2.exists():
        im = trim_top(open_img(ptr2), 0.22)
        for part, name in zip(split_rows(im, 2, pad=0.03), ["sym_tr_tr.png", "sym_tr_tf.png"]):
            save_sym(name, trim_symbol_top(part, 0.06))
            n += 1
            print("sym", name, "<-", ptr2.name)

    return n


def process_diagrams() -> int:
    n = 0
    singles = [
        ("225940", "", "p032_diag059.png"),
        ("225945", "", "p035_diag065.png"),
        ("225926", "", "p128_diag303.png"),
        ("230211", "", "p125_diag299.png"),
        ("230218", "", "p126_diag300.png"),
        ("230025", "", "p080_diag182.png"),
        ("230045", "", "p114_diag268.png"),
        ("230156", "", "p118_diag282.png"),
        ("230238", "", "p140_diag331.png"),
        ("230247", "", "p147_wenner.png"),
        ("230249", "", "p148_earth_tester.png"),
        ("230254", "", "p149_timed_contact.png"),
        ("230102", "", "p153_relay8.png"),
        ("230159", "", "p109_q258_diag.png"),
        ("230138", "", "p108_cubicle_r.png"),
        ("230015", "", "p096_diag224.png"),
        ("230113", "", "p097_diag228.png"),
        ("230204", "", "p115_diag270.png"),
        ("230220", "", "p088_diag208_2.png"),
        ("230244", "", "p088_diag208_1.png"),
        ("225916", "", "p019_diag037.png"),
        ("225919", "", "p018_diag036.png"),
        ("230028", "", "p096_diag224_alt.png"),
    ]
    for stamp, suffix, out in singles:
        p = SHOT.parent / f"Screenshot_20260628_{stamp}_Samsung Notes{suffix}.jpg"
        if not p.exists():
            continue
        im = trim_top(open_img(p), 0.04)
        save_crop(out, im)
        n += 1
        print("crop", out, "<-", p.name)

    # split pairs
    p228 = SHOT.parent / "Screenshot_20260628_230228_Samsung Notes.jpg"
    if p228.exists():
        im = trim_top(open_img(p228), 0.05)
        left, right = split_cols(im, 2, pad=0.02)
        save_crop("p135_sys_gnd.png", left)
        save_crop("p135_eq_gnd.png", right)
        n += 2
        print("crop p135_* <-", p228.name)

    p235 = SHOT.parent / "Screenshot_20260628_230235_Samsung Notes.jpg"
    if p235.exists():
        im = trim_top(open_img(p235), 0.05)
        left, right = split_cols(im, 2, pad=0.03)
        save_crop("p139_line_gnd.png", left)
        save_crop("p139_portable_gnd.png", right)
        n += 2
        print("crop p139_* <-", p235.name)

    p110 = SHOT.parent / "Screenshot_20260628_230110_Samsung Notes.jpg"
    if p110.exists():
        im = trim_top(open_img(p110), 0.06)
        top, bottom = split_rows(im, 2, pad=0.04)
        save_crop("p146_fig1.png", top)
        save_crop("p146_fig2.png", bottom)
        n += 2
        print("crop p146_* <-", p110.name)

    p108l = SHOT.parent / "Screenshot_20260628_230147_Samsung Notes.jpg"
    if p108l.exists():
        save_crop("p108_cubicle_l.png", trim_top(open_img(p108l), 0.05))
        n += 1

    return n


def embed_diagrams_in_html() -> None:
    import base64

    html_path = ROOT / "output/dandap_manual.html"
    html = html_path.read_text(encoding="utf-8")
    count = 0
    for crop in sorted(CROPS.glob("*.png")):
        uri = base64.b64encode(crop.read_bytes()).decode("ascii")
        data = f"data:image/png;base64,{uri}"
        # replace legacy relative paths
        rel = f"../assets/images/manual/crops/{crop.name}"
        if rel in html:
            html = html.replace(f'src="{rel}"', f'src="{data}" data-crop="{crop.name}"')
            count += 1
        # replace existing data-crop marker
        pat = rf'src="data:image/[^"]+"( data-crop="{re.escape(crop.name)}")'
        if re.search(pat, html):
            html = re.sub(pat, f'src="{data}"\\1', html, count=1)
            count += 1
    html_path.write_text(html, encoding="utf-8")
    print(f"Embedded/updated {count} diagram crops in HTML")


def main() -> None:
    ns = process_symbols()
    nd = process_diagrams()
    print(f"Processed {ns} symbols, {nd} diagram crops")
    subprocess.run([sys.executable, str(ROOT / "scripts/rebuild_symbol_pages.py")], check=True)
    embed_diagrams_in_html()
    subprocess.run([sys.executable, str(ROOT / "scripts/fit_page_layout.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/export_manual_pdf.py")], check=True)
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/render_pdf_qa.py"), "159", "160", "161"],
        check=True,
    )
    print("Done.")


if __name__ == "__main__":
    main()
