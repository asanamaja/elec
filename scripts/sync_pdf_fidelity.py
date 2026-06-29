#!/usr/bin/env python3
"""Sync dandap_manual.html text colors and line breaks from dandap_replica.html (PDF ground truth)."""
from __future__ import annotations

import html as html_lib
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANUAL = ROOT / "output/dandap_manual.html"
REPLICA = ROOT / "output/dandap_replica.html"

RED_FILLS = {"#c9a0a8", "#d94848", "#e57373", "#e06666"}
PAGE_RE = re.compile(
    r'(<div class="page" id="page-(\d+)">)(.*?)(</div>\s*</div>)',
    re.DOTALL,
)
Q_BLOCK_RE = re.compile(
    r'(<div class="q">\s*<div class="q-num">)(\d+)\.(</div><hr class="q-hline">\s*)(.*?)(</div>)',
    re.DOTALL,
)
TEXT_EL_RE = re.compile(
    r'(<p class="(q-text|ans-line)"[^>]*>)(.*?)(</p>)',
    re.DOTALL,
)
TSPAN_RE = re.compile(r'<tspan[^>]*fill="([^"]*)"[^>]*(?:font-weight="(\d+)")?[^>]*>([^<]*)</tspan>')
TEXT_LINE_RE = re.compile(
    r'<text\b([^>]*)>(.*?)</text>',
    re.DOTALL,
)


@dataclass
class Span:
    text: str
    red: bool
    bold: bool


@dataclass
class RLine:
    y: float
    spans: list[Span] = field(default_factory=list)

    @property
    def plain(self) -> str:
        return "".join(s.text for s in self.spans)

    def red_mask(self) -> list[bool]:
        out: list[bool] = []
        for s in self.spans:
            out.extend([s.red] * len(s.text))
        return out


def norm(s: str) -> str:
    s = html_lib.unescape(s)
    s = re.sub(r"\s+", "", s)
    s = s.replace("×", "x").replace("／", "/")
    return s.lower()


def parse_replica_page(body: str) -> list[RLine]:
    lines: list[RLine] = []
    for m in TEXT_LINE_RE.finditer(body):
        attrs, inner = m.group(1), m.group(2)
        ym = re.search(r'\by="([0-9.]+)"', attrs)
        if not ym:
            continue
        y = float(ym.group(1))
        spans: list[Span] = []
        for sm in TSPAN_RE.finditer(inner):
            fill, weight, text = sm.group(1), sm.group(2), sm.group(3)
            if not text:
                continue
            spans.append(
                Span(
                    text=text,
                    red=fill.lower() in RED_FILLS,
                    bold=weight == "700",
                )
            )
        if spans:
            lines.append(RLine(y=y, spans=spans))
    lines.sort(key=lambda ln: ln.y)
    return lines


def group_replica_by_question(lines: list[RLine]) -> dict[str, list[RLine]]:
    groups: dict[str, list[RLine]] = {}
    current: str | None = None
    for ln in lines:
        m = re.search(r"(\d{3})\.?", ln.plain)
        if m and ln.y < 750 and float(m.group(1)) < 400:
            current = m.group(1)
            groups.setdefault(current, [])
        if current:
            groups[current].append(ln)
    return groups


def apply_color_map(text: str, red_flags: list[bool]) -> str:
    if not text:
        return text
    if len(red_flags) != len(norm(text)):
        # length mismatch — word-level fallback
        words = re.split(r"(\s+)", text)
        out: list[str] = []
        for w in words:
            if not w.strip():
                out.append(w)
                continue
            nw = norm(w)
            best = 0.0
            best_red = False
            for ln_flags, ln_text in red_flags if False else []:
                pass
            # simple: if any replica red substring appears in word
            out.append(w)
        return "".join(out)

    # char alignment on normalized chars, map back to original
    chars = list(text)
    nchars = [c for c in chars if not c.isspace()]
    if len(nchars) != len(red_flags):
        return text

    result: list[str] = []
    ri = 0
    buf = ""
    in_ans = False
    for c in chars:
        if c.isspace():
            if buf:
                result.append(f'<span class="ans">{buf}</span>' if in_ans else buf)
                buf = ""
                in_ans = False
            result.append(c)
            continue
        is_red = red_flags[ri]
        ri += 1
        if is_red:
            if not in_ans and buf:
                result.append(buf)
                buf = ""
            in_ans = True
            buf += c
        else:
            if in_ans and buf:
                result.append(f'<span class="ans">{buf}</span>')
                buf = ""
                in_ans = False
            buf += c
    if buf:
        result.append(f'<span class="ans">{buf}</span>' if in_ans else buf)
    return "".join(result)


def colorize_from_replica(manual_text: str, replica_line: RLine) -> str:
    """Map replica per-char colors onto manual text via sequence alignment."""
    mt = norm(manual_text)
    rt = norm(replica_line.plain)
    if not mt or not rt:
        return manual_text

    rmask = replica_line.red_mask()
    if len(rmask) != len(rt):
        rmask = [any(s.red for s in replica_line.spans)] * len(rt)

    sm = SequenceMatcher(None, mt, rt)
    char_red = [False] * len(mt)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k, j in enumerate(range(j1, j2)):
                if j < len(rmask) and rmask[j]:
                    char_red[i1 + k] = True
        elif tag in ("replace", "insert"):
            rep_red = any(rmask[j1:j2]) if j2 > j1 else False
            if rep_red:
                for k in range(i1, i2):
                    char_red[k] = True

    # rebuild with original manual spacing
    out: list[str] = []
    mi = 0
    buf = ""
    in_ans = False
    for c in manual_text:
        if c.isspace():
            if buf:
                out.append(f'<span class="ans">{buf}</span>' if in_ans else buf)
                buf = ""
                in_ans = False
            out.append(c)
            continue
        red = char_red[mi] if mi < len(char_red) else False
        mi += 1
        if red:
            if not in_ans and buf:
                out.append(buf)
                buf = ""
            in_ans = True
            buf += c
        else:
            if in_ans and buf:
                out.append(f'<span class="ans">{buf}</span>')
                buf = ""
                in_ans = False
            buf += c
    if buf:
        out.append(f'<span class="ans">{buf}</span>' if in_ans else buf)
    return "".join(out)


def split_to_lines(manual_plain: str, replica_lines: list[RLine]) -> list[str]:
    """Split a merged manual paragraph into lines matching replica line count."""
    if len(replica_lines) <= 1:
        return [manual_plain]
    # try split on numbered list markers
    parts = re.split(r"(?=\d+\.\s)", manual_plain)
    parts = [p.strip() for p in parts if p.strip()]
    if len(parts) == len(replica_lines):
        return parts
    return [manual_plain]


def rebuild_question_body(body: str, replica_lines: list[RLine]) -> str:
    """Rebuild q-text / ans-line paragraphs using replica line structure."""
    if not replica_lines:
        return body

    # skip header/footer replica lines (y > 750 or brand text)
    content_lines = [
        ln
        for ln in replica_lines
        if ln.y < 750
        and "전기치트키" not in ln.plain
        and "단답비급" not in ln.plain
        and "전기기사" not in ln.plain
    ]
    if not content_lines:
        return body

    # first line is usually question number — skip
    q_lines = content_lines[1:] if re.match(r"^\d{3}", content_lines[0].plain.strip()) else content_lines

    # collect manual text elements
    elements = list(TEXT_EL_RE.finditer(body))
    if not elements:
        return body

    manual_texts = [html_lib.unescape(re.sub(r"<[^>]+>", "", m.group(3))) for m in elements]

    # if manual has fewer elements than replica answer lines, split first big block
    if len(manual_texts) == 1 and len(q_lines) > 2:
        # keep first replica line as question, rest as answers
        q_rep = q_lines[0]
        ans_rep = q_lines[1:]
        q_manual = manual_texts[0]
        # heuristic: question ends at ? or before numbered answers
        split_m = re.split(r"(?=\d+\.\s)", q_manual, maxsplit=1)
        if len(split_m) == 2:
            q_part, ans_part = split_m
            new_parts = [q_part.strip(), ans_part.strip()]
        else:
            new_parts = [q_manual]
        manual_texts = new_parts

    new_html_parts: list[str] = []
    rep_idx = 0
    for el in elements:
        opener, cls, inner, closer = el.group(1), el.group(2), el.group(3), el.group(4)
        plain = html_lib.unescape(re.sub(r"<[^>]+>", "", inner))
        if not plain.strip():
            new_html_parts.append(el.group(0))
            continue

        # pick best matching replica line
        best_j = rep_idx
        best_score = 0.0
        for j in range(rep_idx, min(rep_idx + 4, len(q_lines))):
            score = SequenceMatcher(None, norm(plain), norm(q_lines[j].plain)).ratio()
            if score > best_score:
                best_score = score
                best_j = j
        rline = q_lines[best_j] if best_score > 0.25 else q_lines[min(rep_idx, len(q_lines) - 1)]
        rep_idx = min(best_j + 1, len(q_lines))

        # preserve <b> tags from manual
        bold_bits = re.findall(r"<b>(.*?)</b>", inner)
        colored = colorize_from_replica(plain, rline)
        for b in bold_bits:
            colored = colored.replace(b, f"<b>{b}</b>", 1)

        # preserve inline images / formulas
        for tag in re.findall(r"<img\b[^>]*>|<span class=\"formula\"[^>]*>.*?</span>|\\$[^$]+\\$", inner, re.DOTALL):
            if tag not in colored:
                colored += " " + tag

        new_html_parts.append(f"{opener}{colored}{closer}")

    # replace elements in body
    out = body
    for el, new in zip(elements, new_html_parts):
        out = out.replace(el.group(0), new, 1)
    return out


def sync_page(manual_body: str, replica_body: str, skip_photo_pages: set[int]) -> str:
    page_num = int(re.search(r'id="page-(\d+)"', manual_body).group(1)) if False else 0
    rep_lines = parse_replica_page(replica_body)
    by_q = group_replica_by_question(rep_lines)

    def repl_q(m: re.Match[str]) -> str:
        qnum = m.group(2)
        body = m.group(4)
        if qnum not in by_q:
            return m.group(0)
        # skip questions with tables/images-only bodies
        if "<table" in body and "<img" in body:
            return m.group(0)
        if re.search(r"<img\b", body) and "ans-line" not in body:
            return m.group(0)
        new_body = rebuild_question_body(body, by_q[qnum])
        return m.group(1) + qnum + m.group(3) + new_body + m.group(5)

    return Q_BLOCK_RE.sub(repl_q, manual_body)


def main() -> None:
    manual = MANUAL.read_text(encoding="utf-8")
    replica = REPLICA.read_text(encoding="utf-8")

    rep_pages = {m.group(2): m.group(3) for m in PAGE_RE.finditer(replica)}
    skip = {41, 103, 113, 127, 135, 136, 159, 160, 161}  # photo-heavy; handled separately

    def repl_page(m: re.Match[str]) -> str:
        opener, pid, body, closer = m.group(1), m.group(2), m.group(3), m.group(4)
        page_num = int(pid)
        if page_num in skip:
            return m.group(0)
        rep_body = rep_pages.get(pid)
        if not rep_body:
            return m.group(0)
        return opener + sync_page(body, rep_body, skip) + closer

    manual = PAGE_RE.sub(repl_page, manual)
    MANUAL.write_text(manual, encoding="utf-8")
    print("Synced colors/line breaks from replica for text pages")


if __name__ == "__main__":
    main()
