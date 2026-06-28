#!/usr/bin/env python3
"""Convert image-based PDF pages to positioned HTML replica (A4 595x842pt)."""
from __future__ import annotations

import html
import io
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import cv2
import easyocr
import fitz
import numpy as np
import pytesseract
from PIL import Image

PDF = Path("/workspace/assets/pdf/source.pdf")
OUT_HTML = Path("/workspace/output/dandap_replica.html")
CROPS_DIR = Path("/workspace/assets/images/crops")
META_JSON = Path("/workspace/output/page_meta.json")

PAGE_W, PAGE_H = 595.0, 842.0
OCR_SCALE = 2.0
MIN_CROP_AREA = 4000  # at 1x (PDF points^2)
TEXT_MASK_PAD = 4
MARGIN_LEFT = 52  # spiral binding gutter
TESS_CONFIG = "--oem 3 --psm 6 -c preserve_interword_spaces=1"

# Decorative pages: relative crop zones (x0,y0,x1,y1) for illustration parts
DECOR_ZONES: dict[int, list[tuple[float, float, float, float]]] = {
    1: [(0.0, 0.0, 0.45, 0.45), (0.40, 0.15, 0.95, 0.78), (0.30, 0.78, 0.72, 0.90)],
    2: [(0.05, 0.10, 0.95, 0.90)],
    3: [(0.0, 0.0, 0.38, 0.32), (0.06, 0.28, 0.30, 0.72), (0.72, 0.55, 0.92, 0.72)],
    4: [(0.08, 0.52, 0.58, 0.93)],
}

_READER: easyocr.Reader | None = None


def get_reader() -> easyocr.Reader:
    global _READER
    if _READER is None:
        _READER = easyocr.Reader(["ko", "en"], gpu=False, verbose=False)
    return _READER


@dataclass
class Word:
    text: str
    x: float
    y: float
    w: float
    h: float
    color: str
    size: float
    bold: bool = False


@dataclass
class Line:
    words: list[Word] = field(default_factory=list)
    y: float = 0.0


@dataclass
class HLine:
    x: float
    y: float
    w: float
    color: str


@dataclass
class CropImg:
    x: float
    y: float
    w: float
    h: float
    src: str


@dataclass
class TableCell:
    x: float
    y: float
    w: float
    h: float
    text: str
    color: str
    bg: str | None
    align: str


@dataclass
class Table:
    x: float
    y: float
    w: float
    h: float
    cells: list[TableCell]


def render_page(page: fitz.Page, scale: float) -> tuple[np.ndarray, Image.Image]:
    pix = page.get_pixmap(matrix=fitz.Matrix(scale, scale))
    pil = Image.open(io.BytesIO(pix.tobytes("png")))
    return np.array(pil), pil


def classify_color(rgb: tuple[int, int, int]) -> str:
    r, g, b = int(rgb[0]), int(rgb[1]), int(rgb[2])
    if r + g + b > 700:
        return "white"
    if r > 150 and g < 120 and b < 120:
        return "red"
    # answer highlight: light pink / rose
    if r > 145 and g > 100 and b > 100 and r >= g and (r - g) < 70 and (r - b) < 90:
        return "pink"
    if max(r, g, b) - min(r, g, b) < 30 and 80 < r < 170:
        return "gray"
    return "black"


def sample_word_color(img: np.ndarray, x: float, y: float, w: float, h: float, scale: float) -> str:
    sx = int(x * scale)
    sy = int(y * scale)
    sw = max(1, int(w * scale))
    sh = max(1, int(h * scale))
    roi = img[sy : sy + sh, sx : sx + sw]
    if roi.size == 0:
        return "black"
    # focus on center band to avoid background bleed
    cy0 = int(sh * 0.25)
    cy1 = int(sh * 0.85)
    cx0 = int(sw * 0.1)
    cx1 = int(sw * 0.9)
    band = roi[cy0:cy1, cx0:cx1]
    pixels = band.reshape(-1, 3)
    # ignore near-white pixels
    mask = np.sum(pixels, axis=1) < 700
    if not mask.any():
        return "black"
    pixels = pixels[mask]
    med = np.median(pixels, axis=0).astype(int)
    return classify_color(tuple(med))


def normalize_ocr_text(text: str) -> str:
    text = text.replace("@", "①").replace("®", "①").replace("©", "②")
    text = re.sub(r"\bHHS\b", "댐퍼", text)
    return text.strip()


def colored_spans(img_arr: np.ndarray, x: float, y: float, w: float, h: float, text: str, scale: float) -> list[tuple[str, str]]:
    if not text:
        return []
    n = max(len(text), 1)
    spans: list[tuple[str, str]] = []
    cur_color: str | None = None
    buf: list[str] = []
    for i, ch in enumerate(text):
        px = x + (i + 0.5) * (w / n)
        color = sample_word_color(img_arr, px - 2, y, max(4, w / n), h, scale)
        if color in ("white", "gray") and ch.strip():
            color = "black"
        if color == cur_color:
            buf.append(ch)
        else:
            if buf:
                spans.append((cur_color or "black", "".join(buf)))
            cur_color = color
            buf = [ch]
    if buf:
        spans.append((cur_color or "black", "".join(buf)))
    return spans


def ocr_lines(pil_img: Image.Image, img_arr: np.ndarray, scale: float) -> list[Line]:
    reader = get_reader()
    results = reader.readtext(np.array(pil_img))
    lines: list[Line] = []
    for bbox, text, conf in results:
        text = normalize_ocr_text(text)
        if not text or conf < 0.12:
            continue
        xs = [p[0] for p in bbox]
        ys = [p[1] for p in bbox]
        x = min(xs) / scale
        y = min(ys) / scale
        w = (max(xs) - min(xs)) / scale
        h = (max(ys) - min(ys)) / scale
        if x < MARGIN_LEFT - 5:
            continue
        if w > PAGE_W * 0.9 or h > 50:
            continue
        size = max(h * 0.88, 9.5)
        spans = colored_spans(img_arr, x, y, w, h, text, scale)
        words = [
            Word(text=seg, x=x, y=y, w=w, h=h, color=col, size=size, bold=False)
            for col, seg in spans
            if seg.strip()
        ]
        if not words:
            continue
        bold = bool(
            re.match(r"^\d{3}\.?$", text)
            or re.match(r"^DAY\s*\d+", text)
            or text in ("부록", "목차", "memo")
            or (size > 14 and len(text) <= 10)
        )
        if bold:
            for wobj in words:
                wobj.bold = True
        lines.append(Line(words=words, y=y))
    lines.sort(key=lambda ln: (ln.y, ln.words[0].x))
    return lines


def detect_hlines(img_arr: np.ndarray, scale: float) -> list[HLine]:
    gray = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
    inv = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 8)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (int(60 * scale), 1))
    horiz = cv2.morphologyEx(inv, cv2.MORPH_OPEN, kernel)
    cnts, _ = cv2.findContours(horiz, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    out: list[HLine] = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w < 80 * scale or h > 8 * scale:
            continue
        # sample color
        sy = min(img_arr.shape[0] - 1, y + h // 2)
        sx = min(img_arr.shape[1] - 1, x + w // 2)
        color = classify_color(tuple(img_arr[sy, sx]))
        if color in ("white", "black"):
            color = "pink"
        out.append(HLine(x=x / scale, y=y / scale, w=w / scale, color=color))
    # dedupe by y
    out.sort(key=lambda h: h.y)
    deduped: list[HLine] = []
    for hl in out:
        if deduped and abs(deduped[-1].y - hl.y) < 2:
            if hl.w > deduped[-1].w:
                deduped[-1] = hl
        else:
            deduped.append(hl)
    return deduped


def text_mask(img_shape: tuple[int, int], lines: list[Line], scale: float) -> np.ndarray:
    mask = np.zeros(img_shape[:2], dtype=np.uint8)
    for ln in lines:
        for w in ln.words:
            x0 = max(0, int((w.x - TEXT_MASK_PAD) * scale))
            y0 = max(0, int((w.y - TEXT_MASK_PAD) * scale))
            x1 = min(img_shape[1], int((w.x + w.w + TEXT_MASK_PAD) * scale))
            y1 = min(img_shape[0], int((w.y + w.h + TEXT_MASK_PAD) * scale))
            mask[y0:y1, x0:x1] = 255
    return mask


def all_words(lines: list[Line]) -> list[Word]:
    return [w for ln in lines for w in ln.words]


def crop_overlaps_text(cx: float, cy: float, cw: float, ch: float, words: list[Word]) -> float:
    crop_area = cw * ch
    if crop_area <= 0:
        return 0.0
    overlap = 0.0
    for w in words:
        ix0 = max(cx, w.x - 2)
        iy0 = max(cy, w.y - 2)
        ix1 = min(cx + cw, w.x + w.w + 2)
        iy1 = min(cy + ch, w.y + w.h + 2)
        if ix1 > ix0 and iy1 > iy0:
            overlap += (ix1 - ix0) * (iy1 - iy0)
    return overlap / crop_area


def decor_zone_crops(img_arr: np.ndarray, scale: float, page_no: int, lines: list[Line]) -> list[CropImg]:
    zones = list(DECOR_ZONES.get(page_no, []))
    if not zones:
        has_day = any("DAY" in "".join(w.text for w in ln.words) for ln in lines)
        if has_day or page_no in (2,):
            zones = [(0.0, 0.50, 0.60, 0.95)]
    crops: list[CropImg] = []
    CROPS_DIR.mkdir(parents=True, exist_ok=True)
    for zi, (rx0, ry0, rx1, ry1) in enumerate(zones):
        x0 = int(rx0 * img_arr.shape[1])
        y0 = int(ry0 * img_arr.shape[0])
        x1 = int(rx1 * img_arr.shape[1])
        y1 = int(ry1 * img_arr.shape[0])
        crop = img_arr[y0:y1, x0:x1]
        if crop.size == 0:
            continue
        fname = f"p{page_no:03d}_zone{zi:02d}.png"
        Image.fromarray(crop).save(CROPS_DIR / fname)
        crops.append(
            CropImg(
                x=x0 / scale,
                y=y0 / scale,
                w=(x1 - x0) / scale,
                h=(y1 - y0) / scale,
                src=f"../assets/images/crops/{fname}",
            )
        )
    return crops


def detect_crops(
    img_arr: np.ndarray, lines: list[Line], scale: float, page_no: int
) -> list[CropImg]:
    decorative = page_no in DECOR_ZONES or len(lines) < 10
    if decorative:
        return decor_zone_crops(img_arr, scale, page_no, lines)

    words = all_words(lines)
    content_page = len(lines) >= 12
    max_area = PAGE_W * PAGE_H * (0.22 if content_page else 0.55)
    max_h = PAGE_H * (0.28 if content_page else 0.65)
    max_w = PAGE_W * (0.55 if content_page else 0.85)

    mask = text_mask(img_arr.shape, lines, scale)
    gray = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
    content = (gray < 245).astype(np.uint8) * 255
    content[mask > 0] = 0
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    content = cv2.morphologyEx(content, cv2.MORPH_OPEN, kernel)
    content = cv2.dilate(content, kernel, iterations=1)
    cnts, _ = cv2.findContours(content, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    crops: list[CropImg] = []
    CROPS_DIR.mkdir(parents=True, exist_ok=True)
    for idx, c in enumerate(cnts):
        x, y, w, h = cv2.boundingRect(c)
        cx, cy, cw, ch = x / scale, y / scale, w / scale, h / scale
        if cx < MARGIN_LEFT - 10:
            continue
        area = cw * ch
        if area < MIN_CROP_AREA or area > max_area:
            continue
        if cw > max_w or ch > max_h:
            continue
        if crop_overlaps_text(cx, cy, cw, ch, words) > 0.12:
            continue
        pad = int(4 * scale)
        x0 = max(0, x - pad)
        y0 = max(0, y - pad)
        x1 = min(img_arr.shape[1], x + w + pad)
        y1 = min(img_arr.shape[0], y + h + pad)
        crop = img_arr[y0:y1, x0:x1]
        fname = f"p{page_no:03d}_img{idx:02d}.png"
        fpath = CROPS_DIR / fname
        Image.fromarray(crop).save(fpath)
        crops.append(
            CropImg(
                x=x0 / scale,
                y=y0 / scale,
                w=(x1 - x0) / scale,
                h=(y1 - y0) / scale,
                src=f"../assets/images/crops/{fname}",
            )
        )
    crops.sort(key=lambda c: (c.y, c.x))
    return crops


def detect_table(img_arr: np.ndarray, lines: list[Line], scale: float) -> Table | None:
    gray = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
    inv = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 8)
    hk = cv2.getStructuringElement(cv2.MORPH_RECT, (int(50 * scale), 1))
    vk = cv2.getStructuringElement(cv2.MORPH_RECT, (1, int(30 * scale)))
    horiz = cv2.morphologyEx(inv, cv2.MORPH_OPEN, hk)
    vert = cv2.morphologyEx(inv, cv2.MORPH_OPEN, vk)
    h_cnts, _ = cv2.findContours(horiz, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    v_cnts, _ = cv2.findContours(vert, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    h_ys = []
    for c in h_cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w > 200 * scale:
            h_ys.append(y / scale)
    v_xs = []
    for c in v_cnts:
        x, y, w, h = cv2.boundingRect(c)
        if h > 80 * scale:
            v_xs.append(x / scale)

    h_ys = sorted(set(round(y, 1) for y in h_ys))
    v_xs = sorted(set(round(x, 1) for x in v_xs))

    if len(h_ys) < 4 or len(v_xs) < 1:
        return None

    # cluster nearby lines
    def cluster(vals: list[float], tol: float = 4.0) -> list[float]:
        if not vals:
            return []
        clusters = [[vals[0]]]
        for v in vals[1:]:
            if v - clusters[-1][-1] <= tol:
                clusters[-1].append(v)
            else:
                clusters.append([v])
        return [sum(c) / len(c) for c in clusters]

    h_ys = cluster(h_ys)
    v_xs = cluster(v_xs)

    if len(h_ys) < 4:
        return None

    # find table region: consecutive horizontal lines with similar x span
    best = None
    for i in range(len(h_ys) - 3):
        block = h_ys[i : i + 6]
        if block[-1] - block[0] < 40 or block[-1] - block[0] > 350:
            continue
        y0, y1 = block[0], block[-1]
        # words inside
        inside = []
        for ln in lines:
            for w in ln.words:
                cy = w.y + w.h / 2
                if y0 <= cy <= y1 + 5:
                    inside.append(w)
        if len(inside) < 6:
            continue
        xs = [w.x for w in inside] + [w.x + w.w for w in inside]
        x0, x1 = min(xs) - 5, max(xs) + 5
        best = (x0, y0, x1 - x0, y1 - y0 + 8, block, v_xs, inside)
        break

    if not best:
        return None

    x0, y0, tw, th, h_lines, v_lines, inside_words = best
    col_xs = [x0] + [x for x in v_lines if x0 < x < x0 + tw] + [x0 + tw]
    col_xs = sorted(set(col_xs))
    if len(col_xs) < 2:
        col_xs = [x0, x0 + tw * 0.28, x0 + tw]

    row_ys = h_lines
    cells: list[TableCell] = []
    for ri in range(len(row_ys) - 1):
        ry0, ry1 = row_ys[ri], row_ys[ri + 1]
        for ci in range(len(col_xs) - 1):
            cx0, cx1 = col_xs[ci], col_xs[ci + 1]
            cell_words = [
                w
                for w in inside_words
                if cx0 <= w.x + w.w / 2 <= cx1 and ry0 <= w.y + w.h / 2 <= ry1
            ]
            cell_words.sort(key=lambda w: (w.y, w.x))
            text = " ".join(w.text for w in cell_words)
            if not text:
                continue
            colors = [w.color for w in cell_words if w.color not in ("white",)]
            color = colors[0] if colors else "black"
            bg = "#e8e8e8" if ri == 0 else None
            align = "center" if ci == 0 or ri == 0 else "left"
            cells.append(
                TableCell(x=cx0, y=ry0, w=cx1 - cx0, h=ry1 - ry0, text=text, color=color, bg=bg, align=align)
            )

    if len(cells) < 4:
        return None
    return Table(x=x0, y=y0, w=tw, h=th, cells=cells)


COLOR_CSS = {
    "black": "#1a1a1a",
    "pink": "#c9a0a8",
    "red": "#c44",
    "gray": "#666",
}


def line_to_html(ln: Line, table: Table | None) -> str:
    if not ln.words:
        return ""
    words = ln.words
    if table:
        words = [
            w
            for w in words
            if not (
                table.x - 2 <= w.x <= table.x + table.w + 2
                and table.y - 2 <= w.y <= table.y + table.h + 2
            )
        ]
        if not words:
            return ""

    y = ln.y
    x_start = words[0].x
    size = max(w.size for w in words)
    parts = []
    for w in words:
        fill = COLOR_CSS.get(w.color, "#1a1a1a")
        parts.append(f'<tspan fill="{fill}">{html.escape(w.text)}</tspan>')

    fw = "700" if any(w.bold for w in words) or re.match(r"^\d{3}\.$", words[0].text) else "400"
    return (
        f'<text x="{x_start:.1f}" y="{y + size:.1f}" '
        f'font-size="{size:.1f}" font-weight="{fw}" '
        f'font-family="\'Noto Sans KR\',\'Apple SD Gothic Neo\',sans-serif">'
        + "".join(parts)
        + "</text>"
    )


def table_to_html(table: Table) -> str:
    # group cells by row
    rows: dict[float, list[TableCell]] = {}
    for c in table.cells:
        rows.setdefault(round(c.y, 1), []).append(c)
    svg_rows = []
    for y in sorted(rows.keys()):
        row_cells = sorted(rows[y], key=lambda c: c.x)
        for c in row_cells:
            fill = f' fill="{c.bg}"' if c.bg else ""
            anchor = "middle" if c.align == "center" else "start"
            tx = c.x + c.w / 2 if c.align == "center" else c.x + 6
            svg_rows.append(
                f'<rect x="{c.x:.1f}" y="{c.y:.1f}" width="{c.w:.1f}" height="{c.h:.1f}"'
                f' stroke="#bbb" stroke-width="0.6"{fill}/>'
                f'<text x="{tx:.1f}" y="{c.y + c.h * 0.62:.1f}" font-size="10.5" '
                f'text-anchor="{anchor}" fill="{COLOR_CSS.get(c.color, "#1a1a1a")}" '
                f'font-family="\'Noto Sans KR\',sans-serif">{html.escape(c.text)}</text>'
            )
    return (
        f'<g class="table" transform="translate(0,0)">'
        + "".join(svg_rows)
        + "</g>"
    )


def page_to_svg(page_no: int, page: fitz.Page) -> tuple[str, dict]:
    img_arr, pil = render_page(page, OCR_SCALE)
    lines = ocr_lines(pil, img_arr, OCR_SCALE)
    hlines = detect_hlines(img_arr, OCR_SCALE)
    table = detect_table(img_arr, lines, OCR_SCALE)
    crops = detect_crops(img_arr, lines, OCR_SCALE, page_no)

    svg_parts = [
        f'<svg class="page-svg" viewBox="0 0 {PAGE_W} {PAGE_H}" xmlns="http://www.w3.org/2000/svg">',
        f'<rect width="100%" height="100%" fill="#fff"/>',
    ]

    for crop in crops:
        svg_parts.append(
            f'<image href="{html.escape(crop.src)}" x="{crop.x:.1f}" y="{crop.y:.1f}" '
            f'width="{crop.w:.1f}" height="{crop.h:.1f}" preserveAspectRatio="xMidYMid meet"/>'
        )

    for hl in hlines:
        # skip lines inside table (table draws its own borders)
        if table and table.y <= hl.y <= table.y + table.h:
            continue
        stroke = "#d4a0a8" if hl.color == "pink" else "#ccc"
        svg_parts.append(
            f'<line x1="{hl.x:.1f}" y1="{hl.y:.1f}" x2="{hl.x + hl.w:.1f}" y2="{hl.y:.1f}" '
            f'stroke="{stroke}" stroke-width="0.8"/>'
        )

    if table:
        svg_parts.append(table_to_html(table))

    for ln in lines:
        svg = line_to_html(ln, table)
        if svg:
            svg_parts.append(svg)

    svg_parts.append("</svg>")

    meta = {
        "page": page_no,
        "lines": len(lines),
        "crops": len(crops),
        "has_table": table is not None,
    }
    return "\n".join(svg_parts), meta


def build_html(pages_svg: list[str]) -> str:
    page_divs = "\n".join(
        f'  <div class="page" id="page-{i+1:03d}">\n{svg}\n  </div>'
        for i, svg in enumerate(pages_svg)
    )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>전기기사 실기 단답비급 — HTML 복제본</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
  <style>
    @page {{
      size: 595pt 842pt;
      margin: 0;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #888;
      font-family: 'Noto Sans KR', 'Apple SD Gothic Neo', sans-serif;
    }}
    .toolbar {{
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      background: #1e293b; color: #fff; padding: .6rem 1rem;
      display: flex; gap: 1rem; align-items: center; font-size: .9rem;
    }}
    .toolbar a {{ color: #93c5fd; }}
  .pages {{ padding: 3rem 1rem 2rem; display: flex; flex-direction: column; align-items: center; gap: 12px; }}
    .page {{
      width: 595px; height: 842px;
      background: #fff;
      box-shadow: 0 2px 12px rgba(0,0,0,.25);
      overflow: hidden;
      page-break-after: always;
    }}
    .page-svg {{ width: 595px; height: 842px; display: block; }}
    @media print {{
      body {{ background: #fff; }}
      .toolbar {{ display: none; }}
      .pages {{ padding: 0; gap: 0; }}
      .page {{ box-shadow: none; margin: 0; }}
    }}
  </style>
</head>
<body>
  <div class="toolbar">
    <strong>전기기사 실기 단답비급 — HTML 복제본</strong>
    <span>{len(pages_svg)}페이지 · A4 (595×842pt)</span>
    <a href="#" onclick="window.print();return false;">인쇄/PDF 저장</a>
  </div>
  <div class="pages">
{page_divs}
  </div>
</body>
</html>"""


def main():
    if not PDF.exists():
        raise SystemExit(f"PDF not found: {PDF}")

    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    CROPS_DIR.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(PDF)
    pages_svg: list[str] = []
    all_meta: list[dict] = []

    for i in range(len(doc)):
        page_no = i + 1
        print(f"Processing page {page_no}/{len(doc)}...", flush=True)
        svg, meta = page_to_svg(page_no, doc[i])
        pages_svg.append(svg)
        all_meta.append(meta)

    html_out = build_html(pages_svg)
    OUT_HTML.write_text(html_out, encoding="utf-8")
    META_JSON.write_text(json.dumps(all_meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Done: {OUT_HTML} ({len(html_out):,} bytes)")
    print(f"Crops: {len(list(CROPS_DIR.glob('*.png')))} images")
    print(f"Meta: {META_JSON}")


if __name__ == "__main__":
    main()
