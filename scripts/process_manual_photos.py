#!/usr/bin/env python3
"""Classify, split, trim manual/ screenshots → user/ + crops/, rebuild HTML."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "assets/images/manual"
USER = MANUAL / "user"
CROPS = MANUAL / "crops"
MANIFEST = ROOT / "output/manual_photo_map.json"


def open_img(path: Path) -> Image.Image:
    im = Image.open(path)
    return im.convert("RGB") if im.mode != "RGB" else im


def save_png(im: Image.Image, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.save(dest, format="PNG", optimize=True)


def gray_array(im: Image.Image) -> np.ndarray:
    return np.array(im.convert("L"), dtype=np.float32)


def find_line_positions(arr: np.ndarray, axis: int, thresh_ratio: float = 0.82) -> list[int]:
    """Find dark separator lines along axis (0=horizontal lines, 1=vertical)."""
    proj = arr.mean(axis=axis)
    base = float(proj.mean())
    lines: list[int] = []
    for i in range(2, len(proj) - 2):
        if proj[i] < base * thresh_ratio and proj[i] <= proj[i - 1] and proj[i] <= proj[i + 1]:
            if not lines or i - lines[-1] > 4:
                lines.append(i)
    return lines


def bands_from_lines(size: int, lines: list[int], margin: int = 2) -> list[tuple[int, int]]:
    cuts = [0] + lines + [size]
    out = []
    for a, b in zip(cuts, cuts[1:]):
        y0 = min(size, a + margin)
        y1 = max(y0 + 1, b - margin)
        if y1 - y0 >= 8:
            out.append((y0, y1))
    return out


def split_horizontal(im: Image.Image, min_band: int = 8) -> list[Image.Image]:
    arr = gray_array(im)
    lines = find_line_positions(arr, axis=1)
    bands = bands_from_lines(im.height, lines)
    if len(bands) <= 1:
        return [im]
    return [im.crop((0, y0, im.width, y1)) for y0, y1 in bands if y1 - y0 >= min_band]


def split_equal_rows(im: Image.Image, n: int, pad: float = 0.04) -> list[Image.Image]:
    w, h = im.size
    out = []
    for i in range(n):
        y0 = int((h / n) * i + h * pad / n)
        y1 = int((h / n) * (i + 1) - h * pad / n)
        if y1 > y0:
            out.append(im.crop((0, y0, w, y1)))
    return out


def split_equal_cols(im: Image.Image, n: int, pad: float = 0.03) -> list[Image.Image]:
    w, h = im.size
    out = []
    for i in range(n):
        x0 = int((w / n) * i + w * pad / n)
        x1 = int((w / n) * (i + 1) - w * pad / n)
        if x1 > x0:
            out.append(im.crop((x0, 0, x1, h)))
    return out


def split_vertical(im: Image.Image, min_band: int = 8) -> list[Image.Image]:
    arr = gray_array(im)
    lines = find_line_positions(arr, axis=0)
    bands = bands_from_lines(im.width, lines)
    if len(bands) <= 1:
        n = 3 if im.width > im.height * 3 else 2
        w = im.width
        return [im.crop((int(w * i / n), 0, int(w * (i + 1) / n), im.height)) for i in range(n)]
    return [im.crop((x0, 0, x1, im.height)) for x0, x1 in bands if x1 - x0 >= min_band]


def trim_top_dark_band(im: Image.Image, max_ratio: float = 0.45) -> Image.Image:
    arr = gray_array(im)
    h, w = arr.shape
    row_mean = arr.mean(axis=1)
    base = float(row_mean[h // 2 :].mean()) if h > 4 else float(row_mean.mean())
    y0 = 0
    for y in range(h):
        if y > h * max_ratio:
            break
        if row_mean[y] < base * 0.92:
            y0 = y + 1
        elif y > h * 0.08 and row_mean[y] > base * 0.97:
            break
    return im.crop((0, min(y0, int(h * max_ratio)), w, h))


def trim_question_header(im: Image.Image) -> Image.Image:
    """Remove top band with question text / numbered headers."""
    arr = gray_array(im)
    h, w = arr.shape
    # find first row where content spans most of width with higher variance
    row_std = arr.std(axis=1)
    row_mean = arr.mean(axis=1)
    content_y = 0
    for y in range(h):
        if y < h * 0.45 and row_std[y] > 12 and 40 < row_mean[y] < 220:
            if y > h * 0.05:
                content_y = y
                break
    if content_y == 0:
        return trim_top_dark_band(im)
    return im.crop((0, content_y, w, h))


def crop_left_fraction(im: Image.Image, frac: float = 0.42) -> Image.Image:
    w, h = im.size
    return im.crop((0, 0, int(w * frac), h))


def shot(name: str, suffix: str = "") -> Path:
    return MANUAL / f"Screenshot_20260628_{name}_Samsung Notes{suffix}.jpg"


def process_all() -> dict:
    USER.mkdir(parents=True, exist_ok=True)
    CROPS.mkdir(parents=True, exist_ok=True)
    log: dict = {"symbols": [], "crops": [], "missing": [], "source_files": []}

    def sym(out: str, im: Image.Image, src: str, page: str, note: str = "") -> None:
        save_png(im, USER / out)
        log["symbols"].append({"file": out, "source": src, "page": page, "note": note})

    def crop(out: str, im: Image.Image, src: str, page: str, note: str = "") -> None:
        save_png(im, CROPS / out)
        log["crops"].append({"file": out, "source": src, "page": page, "note": note})

    # --- p.158 symbols (Q365-366) ---
    p2p = shot("230306")
    if p2p.exists():
        im = open_img(p2p)
        w, h = im.size
        sym("sym_2p.png", im.crop((0, 0, w // 2, h)), p2p.name, "p.158", "2P left half")
        sym("sym_sw.png", im.crop((0, 0, w // 2, h)), p2p.name, "p.158", "점멸기=2P좌측")
    for stamp, suffix, out, fn, page_note in [
        ("230306", " (1)", "sym_4w.png", None, "4로 스위치"),
        ("230306", " (2)", "sym_outlet.png", None, "콘센트 기호"),
        ("230306", " (3)", "sym_2gang.png", None, "2구 콘센트"),
        ("230306", " (2) (2)", "sym_3p_out.png", None, "3극 콘센트"),
        ("230042", "", "sym_outdoor.png", None, "옥외등"),
        ("230051", "", "sym_ceiling.png", None, "천장 콘센트"),
    ]:
        p = shot(stamp, suffix)
        if not p.exists():
            continue
        im = open_img(p)
        if fn:
            im = fn(im)
        sym(out, im, p.name, "p.158", page_note)

    pf = shot("230306", " (2) (1)")
    if pf.exists():
        rows = split_horizontal(open_img(pf))
        sym("sym_floor.png", rows[-1], pf.name, "p.158", "바닥 콘센트 하단행")

    p4 = shot("230306", " (4)")
    if p4.exists():
        im = trim_top_dark_band(open_img(p4), 0.1)
        rows = split_horizontal(im)
        for i, name in enumerate(["sym_h400.png", "sym_m400.png", "sym_n400.png"]):
            if i < len(rows):
                sym(name, rows[i], p4.name, "p.158", f"HID row{i+1}")

    # --- p.160 Q367 outlet table (7 cells) ---
    p_out4 = shot("230310")
    if p_out4.exists():
        rows = split_equal_rows(open_img(p_out4), 4)
        names4 = ["sym_lk.png", "sym_el.png", "sym_t_outlet.png", "sym_h_outlet.png"]
        for i, n in enumerate(names4):
            if i < len(rows):
                sym(n, rows[i], p_out4.name, "p.160 Q367", f"표 (1)(3)(5)(7)")

    p_out6 = shot("230153")
    if p_out6.exists():
        rows = split_horizontal(open_img(p_out6))
        names3 = ["sym_et.png", "sym_e_outlet.png", "sym_wp.png"]
        # 6행 중 짝수 인덱스 0,2,4 → (2)(4)(6)
        picks = [0, 2, 4] if len(rows) >= 5 else list(range(min(3, len(rows))))
        for n, idx in zip(names3, picks):
            if idx < len(rows):
                sym(n, rows[idx], p_out6.name, "p.160 Q367", "표 (2)(4)(6)")

    # --- p.160 Q368 switch ---
    p368 = shot("230310", " (1)")
    if p368.exists():
        sym("sym_switch_368.png", crop_left_fraction(open_img(p368), 0.45), p368.name, "p.160 Q368", "S심볼만, 글자는 HTML")

    # --- p.160 Q369 duct ---
    pduct = shot("230310", " (2)")
    if pduct.exists():
        im = trim_question_header(open_img(pduct))
        cols = split_equal_cols(im, 3)
        for part, name in zip(cols[:3], ["sym_md.png", "sym_ld.png", "sym_f7.png"]):
            sym(name, trim_top_dark_band(part, 0.12), pduct.name, "p.160 Q369", "덕트 3열")

    # --- p.161 Q370 breakers ---
    pbrk = shot("230313")
    if pbrk.exists():
        im = trim_question_header(open_img(pbrk))
        cols = split_equal_cols(im, 5)
        for part, name in zip(cols[:5], [
            "sym_breaker_e.png", "sym_breaker_b.png", "sym_breaker_ec.png",
            "sym_breaker_s.png", "sym_breaker_g.png",
        ]):
            sym(name, part, pbrk.name, "p.161 Q370", "(1)~(5) 헤더 제거")

    # --- p.161 Q371 transformers ---
    ptr2 = shot("230313", " (1)")
    if ptr2.exists():
        im = trim_top_dark_band(open_img(ptr2), 0.12)
        rows = split_equal_rows(im, 2)
        if len(rows) >= 2:
            sym("sym_tr_tr.png", rows[0], ptr2.name, "p.161 Q371", "TR")
            sym("sym_tr_tf.png", rows[1], ptr2.name, "p.161 Q371", "TF")
        elif len(rows) == 1:
            sym("sym_tr_tr.png", rows[0], ptr2.name, "p.161 Q371", "TR")

    # --- diagram crops (full-page diagrams) ---
    diagram_map = [
        ("225916", "", "p019_diag037.png", "p.19", "도면"),
        ("225919", "", "p018_diag036.png", "p.18", "도면"),
        ("225940", "", "p032_diag059.png", "p.32", "도면"),
        ("225945", "", "p035_diag065.png", "p.35", "도면"),
        ("225926", "", "p128_diag303.png", "p.128", "도면"),
        ("230211", "", "p125_diag299.png", "p.125", "도면"),
        ("230218", "", "p126_diag300.png", "p.126", "도면"),
        ("230025", "", "p080_diag182.png", "p.80", "도면"),
        ("230045", "", "p114_diag268.png", "p.114", "도면"),
        ("230156", "", "p118_diag282.png", "p.118", "도면"),
        ("230238", "", "p140_diag331.png", "p.140", "도면"),
        ("230247", "", "p147_wenner.png", "p.147", "도면"),
        ("230249", "", "p148_earth_tester.png", "p.148", "도면"),
        ("230254", "", "p149_timed_contact.png", "p.149", "도면"),
        ("230102", "", "p153_relay8.png", "p.153", "도면"),
        ("230159", "", "p109_q258_diag.png", "p.109", "도면"),
        ("230138", "", "p108_cubicle_r.png", "p.108", "도면"),
        ("230015", "", "p096_diag224.png", "p.96", "도면"),
        ("230113", "", "p097_diag228.png", "p.97", "도면"),
        ("230204", "", "p115_diag270.png", "p.115", "도면"),
        ("230220", "", "p088_diag208_2.png", "p.88", "도면"),
        ("230244", "", "p088_diag208_1.png", "p.88", "도면"),
        ("230028", "", "p096_diag224_alt.png", "p.96", "도면 alt"),
    ]
    for stamp, suffix, out, page, note in diagram_map:
        p = shot(stamp, suffix)
        if not p.exists():
            continue
        crop(out, trim_top_dark_band(open_img(p), 0.04), p.name, page, note)

    p228 = shot("230228")
    if p228.exists():
        im = trim_top_dark_band(open_img(p228), 0.05)
        left, right = split_vertical(im)[:2] if len(split_vertical(im)) >= 2 else (im, im)
        crop("p135_sys_gnd.png", left, p228.name, "p.135", "좌")
        crop("p135_eq_gnd.png", right, p228.name, "p.135", "우")

    p235 = shot("230235")
    if p235.exists():
        im = trim_top_dark_band(open_img(p235), 0.05)
        parts = split_vertical(im)
        if len(parts) >= 2:
            crop("p139_line_gnd.png", parts[0], p235.name, "p.139", "좌")
            crop("p139_portable_gnd.png", parts[1], p235.name, "p.139", "우")

    p110 = shot("230110")
    if p110.exists():
        im = trim_top_dark_band(open_img(p110), 0.06)
        rows = split_horizontal(im)
        if len(rows) >= 2:
            crop("p146_fig1.png", rows[0], p110.name, "p.146", "상")
            crop("p146_fig2.png", rows[1], p110.name, "p.146", "하")

    p108l = shot("230147")
    if p108l.exists():
        crop("p108_cubicle_l.png", trim_top_dark_band(open_img(p108l), 0.05), p108l.name, "p.108", "좌")

    # p.71 Q162 — CT·전류계 결선도
    p162 = shot("230038")
    if p162.exists():
        crop("p071_diag162.png", open_img(p162), p162.name, "p.71 Q162", "CT 결선도")

    # p.21 Q043 — NCS/NVS [그림1][그림2] (세로 2분할)
    pncs = shot("225930")
    if pncs.exists():
        rows = split_equal_rows(open_img(pncs), 2)
        if len(rows) >= 2:
            crop("p043_ncs_fig1.png", rows[0], pncs.name, "p.21 Q043", "[그림1]")
            crop("p043_ncs_fig2.png", rows[1], pncs.name, "p.21 Q043", "[그림2]")

    # p.126 Q300 UPS 블록도 (230215가 230218보다 정확한 UPS 도면)
    pups = shot("230215")
    if pups.exists():
        crop("p126_diag300.png", trim_top_dark_band(open_img(pups), 0.04), pups.name, "p.126 Q300", "UPS 블록")

    # HTML slots still needing crops (no matching upload identified)
    for need in [
        "p060_diag126.png",
        "p061_diag128.png",
        "p073_sym168.png",
        "p074_diag170.png",
        "sym_tr_tb.png",
        "sym_tr_tn.png",
        "sym_tr_th.png",
    ]:
        if not (CROPS / need).exists() and not (USER / need).exists():
            page = "p.161 Q371" if need.startswith("sym_tr_") else "diagram"
            log["missing"].append({"file": need, "page": page, "reason": "manual에 매칭 스크린샷 없음"})

    # classify unprocessed source screenshots
    used = {x["source"] for x in log["symbols"] + log["crops"]}
    for p in sorted(MANUAL.glob("Screenshot_*.jpg")):
        entry = {"file": p.name, "used": p.name in used}
        if not entry["used"]:
            entry["note"] = "분류 보류 — 도면/기타 또는 중복"
        log["source_files"].append(entry)

    MANIFEST.write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    return log


def embed_all(html_path: Path) -> None:
    import base64

    html = html_path.read_text(encoding="utf-8")
    for folder, attr in [(USER, "data-sym"), (CROPS, "data-crop")]:
        for png in sorted(folder.glob("*.png")):
            uri = base64.b64encode(png.read_bytes()).decode("ascii")
            data = f"data:image/png;base64,{uri}"
            rel = f"../assets/images/manual/{folder.name}/{png.name}"
            if rel in html:
                html = html.replace(f'src="{rel}"', f'src="{data}" {attr}="{png.name}"')
            pat = rf'src="data:image/[^"]+"( {attr}="{re.escape(png.name)}")'
            if re.search(pat, html):
                html = re.sub(pat, f'src="{data}"\\1', html, count=1)
    html_path.write_text(html, encoding="utf-8")


def main() -> None:
    log = process_all()
    print(json.dumps({"symbols": len(log["symbols"]), "crops": len(log["crops"]), "missing": len(log["missing"])}, indent=2))
    print(f"Wrote {MANIFEST}")

    # rebuild symbol pages from templates (text/tables stay in HTML)
    subprocess.run([sys.executable, str(ROOT / "scripts/rebuild_symbol_pages.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/embed_user_crops.py")], check=True)
    embed_all(ROOT / "output/dandap_manual.html")
    subprocess.run([sys.executable, str(ROOT / "scripts/build_symbols_view.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/fit_page_layout.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/export_manual_pdf.py")], check=True)
    subprocess.run(
        [sys.executable, str(ROOT / "scripts/render_pdf_qa.py"), "159", "160", "161"],
        check=True,
    )


if __name__ == "__main__":
    main()
