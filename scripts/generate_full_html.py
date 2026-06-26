#!/usr/bin/env python3
"""Generate full 단답비급 HTML (001-389) with contextual explanations."""
import re
import html
import json
import glob
import fitz
from pathlib import Path

PDF = Path("/home/ubuntu/.cursor/projects/workspace/uploads/_________________5d19.pdf")
OUT = Path("/workspace/private_study_notes.html")
SCRIPTS = Path("/workspace/scripts")

DAY_MAP = {
    1: "DAY 1 — 가공/지중/송전/배전선로",
    2: "DAY 2 — 역률/콘덴서/고조파/설비불평형",
    3: "DAY 3 — 배선공사",
    4: "DAY 4 — 조명/전동기1",
    5: "DAY 5 — 전동기2/발전기/태양광/전지",
    6: "DAY 6 — 변압기",
    7: "DAY 7 — 차단기/퓨즈/개폐기1",
    8: "DAY 8 — 개폐기2/피뢰기",
    9: "DAY 9 — 부하특성/계전기/수변전1",
    10: "DAY 10 — 수변전2/축전지",
    11: "DAY 11 — UPS/고장 및 사고",
    12: "DAY 12 — 접지/절연",
    13: "DAY 13 — 측정/시퀀스",
    14: "DAY 14 — 정의·규정/옥내기호",
    15: "부록 — 감리",
}

EXPLANATIONS: dict[int, str] = {}


def load_explanations() -> dict[int, str]:
    merged: dict[int, str] = {}
    for path in sorted(SCRIPTS.glob("explanations_*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        for key, text in data.items():
            merged[int(key)] = text.strip()
    return merged


def extract_text() -> str:
    doc = fitz.open(PDF)
    lines = []
    for page in doc:
        for line in page.get_text().splitlines():
            line = line.strip()
            if not line:
                continue
            if re.match(r"^전기기사 실기 단답비급\s*•", line):
                continue
            if line in ("전기치트키", "memo", "memo 영역", "memo 영역 | DAY 3", "memo 영역 | DAY 4"):
                continue
            lines.append(line)
    return "\n".join(lines)


def parse_questions(text: str) -> list[dict]:
    text = re.sub(r"\[표지\]|\[내부 표지\]|\[목차\]", "", text)
    text = re.sub(r"\[DAY \d+ 표지\]", "", text)
    text = re.sub(r"단답비급 DAY \d+.*?\n", "", text)
    text = re.sub(r"단답비급 부록\n", "", text)

    current_day = 1
    current_section = ""
    items = []

    # Split on question numbers
    parts = re.split(r"(?<=\n)(\d{3})\.\s*", text)
    # parts[0] is preamble, then num, body, num, body...

    preamble = parts[0]
    for m in re.finditer(r"DAY (\d+)", preamble):
        current_day = int(m.group(1))

    i = 1
    while i < len(parts) - 1:
        num = int(parts[i])
        body = parts[i + 1].strip()
        i += 2

        # Update day/section from body start
        dm = re.search(r"^DAY (\d+)", body)
        if dm:
            current_day = int(dm.group(1))
            body = re.sub(r"^DAY \d+\s*", "", body).strip()

        sm = re.search(r"^섹션:\s*(.+?)(?:\n|$)", body)
        if sm:
            current_section = sm.group(1).strip()
            body = re.sub(r"^섹션:\s*.+?\n", "", body).strip()

        if num > 389:
            continue
        if num >= 372:
            current_day = 15

        # Infer day from number ranges if needed
        day_ranges = [
            (1, 26, 1), (27, 52, 2), (53, 65, 3), (66, 98, 4), (99, 121, 5),
            (122, 170, 6), (171, 208, 7), (209, 232, 8), (233, 264, 9),
            (265, 297, 10), (298, 317, 11), (318, 335, 12), (336, 355, 13),
            (356, 371, 14), (372, 389, 15),
        ]
        for lo, hi, d in day_ranges:
            if lo <= num <= hi:
                current_day = d
                break

        # Split question vs answer heuristically
        lines = [l for l in body.split("\n") if l.strip()]
        q_lines, a_lines = [], []
        answer_started = False
        for line in lines:
            if re.match(r"^[①②③④⑤⑥⑦⑧⑨⑩]|^\(\d+\)|^[\-\*]?\s*답\s*[:：]|^장점$|^단점$|^수식$|^명칭$|^구분$|^표:", line):
                answer_started = True
            if re.match(r"^[①②③④⑤]\s", line) and len(q_lines) > 0 and not answer_started:
                # might be answer
                if any(k in line for k in ["설치", "kVA", "이하", "방지", "증가", "감소", "계전", "차단"]):
                    answer_started = True
            if answer_started or (q_lines and re.match(r"^[①②③④⑤⑥]", line)):
                a_lines.append(line)
            else:
                q_lines.append(line)

        if not a_lines:
            # fallback: first paragraph question, rest answer
            if len(lines) > 1:
                split_at = 1
                for idx, line in enumerate(lines[1:], 1):
                    if re.match(r"^[①②③④⑤⑥⑦⑧⑨⑩\(]", line):
                        split_at = idx
                        break
                q_lines = lines[:split_at]
                a_lines = lines[split_at:]
            else:
                q_lines = lines
                a_lines = []

        question = "\n".join(q_lines).strip()
        answer = "\n".join(a_lines).strip() if a_lines else "(답안 참고 PDF 원문)"

        items.append({
            "num": num,
            "day": current_day,
            "section": current_section,
            "question": question,
            "answer": answer,
        })

    items.sort(key=lambda x: x["num"])
    # dedupe by num
    seen = set()
    unique = []
    for it in items:
        if it["num"] not in seen:
            seen.add(it["num"])
            unique.append(it)
    return unique


def make_tip(item: dict) -> str:
    n = item["num"]
    return EXPLANATIONS.get(n, "이 항목의 설명을 준비 중입니다.")


def esc(s: str) -> str:
    return html.escape(s).replace("\n", "<br>\n")


def generate_html(items: list[dict]) -> str:
    by_day: dict[int, list] = {}
    for it in items:
        by_day.setdefault(it["day"], []).append(it)

    nav = ""
    for d in sorted(by_day):
        nav += f'      <a href="#day{d}">{DAY_MAP.get(d, f"DAY {d}")}</a>\n'

    sections = ""
    for d in sorted(by_day):
        day_items = by_day[d]
        cards = ""
        for it in day_items:
            tip = make_tip(it)
            sec = f' <span class="sec-tag">{html.escape(it["section"])}</span>' if it["section"] else ""
            cards += f"""
        <article class="q-card" id="q{it['num']:03d}">
          <div class="q-head">
            <span class="q-num">{it['num']:03d}</span>{sec}
          </div>
          <div class="q-body"><strong>문제</strong><p>{esc(it['question'])}</p></div>
          <div class="q-ans"><strong>답</strong><p>{esc(it['answer'])}</p></div>
          <div class="q-extra"><strong>💡 왜 이 답인가요?</strong><p>{html.escape(tip)}</p></div>
        </article>"""

        sections += f"""
    <section class="day-block" id="day{d}">
      <h2 class="day-title">{DAY_MAP.get(d, f'DAY {d}')} <span class="count">({len(day_items)}문항)</span></h2>
      {cards}
    </section>"""

    missing = [n for n in range(1, 390) if n not in {it["num"] for it in items}]

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>전기기사 실기 단답비급 001~389 전체</title>
  <style>
    :root {{
      --bg:#f0f4f8; --surface:#fff; --text:#1a2332; --muted:#64748b;
      --border:#e2e8f0; --accent:#2563eb; --accent-soft:#eff6ff;
      --ans:#ecfdf5; --extra:#fffbeb;
    }}
    *{{box-sizing:border-box;margin:0;padding:0}}
    body{{font-family:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",sans-serif;
      background:var(--bg);color:var(--text);line-height:1.75;font-size:15px}}
    .layout{{display:grid;grid-template-columns:280px 1fr;max-width:1400px;margin:0 auto}}
    .sidebar{{position:sticky;top:0;height:100vh;overflow-y:auto;padding:1.25rem 1rem;
      background:var(--surface);border-right:1px solid var(--border)}}
    .sidebar h2{{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin-bottom:.75rem}}
    .sidebar a{{display:block;padding:.35rem .65rem;margin-bottom:.12rem;border-radius:6px;
      color:var(--muted);text-decoration:none;font-size:.82rem}}
    .sidebar a:hover{{background:var(--accent-soft);color:var(--accent)}}
    .content{{padding:1.75rem 2rem 4rem}}
    .hero{{background:linear-gradient(135deg,#1e3a5f,#2563eb);color:#fff;border-radius:12px;
      padding:1.75rem;margin-bottom:1.5rem}}
    .hero h1{{font-size:1.6rem;font-weight:800;margin-bottom:.4rem}}
    .hero .meta{{opacity:.9;font-size:.9rem}}
    .search{{width:100%;padding:.65rem .85rem;border:1px solid var(--border);border-radius:8px;
      margin-bottom:1rem;font-size:.95rem}}
    .day-block{{margin-bottom:2.5rem}}
    .day-title{{font-size:1.2rem;font-weight:800;padding:.75rem 1rem;background:var(--accent-soft);
      border-left:4px solid var(--accent);border-radius:0 8px 8px 0;margin-bottom:1rem}}
    .count{{font-size:.85rem;color:var(--muted);font-weight:500}}
    .q-card{{background:var(--surface);border:1px solid var(--border);border-radius:10px;
      padding:1.1rem 1.2rem;margin-bottom:.85rem;box-shadow:0 1px 3px rgba(0,0,0,.04)}}
    .q-head{{display:flex;align-items:center;gap:.5rem;margin-bottom:.65rem}}
    .q-num{{background:var(--accent);color:#fff;font-weight:800;font-size:.85rem;
      padding:.2rem .55rem;border-radius:6px}}
    .sec-tag{{font-size:.75rem;background:#f1f5f9;color:#475569;padding:.15rem .5rem;border-radius:4px}}
    .q-body,.q-ans,.q-extra{{margin:.5rem 0;font-size:.92rem}}
    .q-body strong,.q-ans strong,.q-extra strong{{display:block;font-size:.78rem;
      text-transform:uppercase;letter-spacing:.04em;margin-bottom:.25rem}}
    .q-body strong{{color:var(--accent)}}
    .q-ans{{background:var(--ans);border-radius:8px;padding:.65rem .85rem}}
    .q-ans strong{{color:#059669}}
    .q-extra{{background:var(--extra);border-radius:8px;padding:.65rem .85rem;border-left:3px solid #f59e0b}}
    .q-extra strong{{color:#b45309}}
    .warn{{background:#fef2f2;border:1px solid #fecaca;padding:.75rem;border-radius:8px;
      font-size:.85rem;color:#991b1b;margin-bottom:1rem}}
    @media(max-width:900px){{.layout{{grid-template-columns:1fr}}.sidebar{{position:static;height:auto}}}}
  </style>
</head>
<body>
<div class="layout">
  <aside class="sidebar">
    <h2>DAY 목차</h2>
    <nav>
{nav}      <a href="#q050">→ 050 설비불평형</a>
    </nav>
  </aside>
  <main class="content">
    <header class="hero">
      <h1>⚡ 전기기사 실기 단답비급 전체</h1>
      <p class="meta">001번 ~ 389번 · 문제 + 답 + 맥락 설명 · 총 {len(items)}문항</p>
    </header>
    <input class="search" type="search" placeholder="번호 또는 키워드 검색 (예: 050, 피뢰기, 변압기)" id="search">
    {"<div class='warn'>⚠️ 파싱 누락 번호: " + ", ".join(f'{n:03d}' for n in missing) + "</div>" if missing else ""}
    {sections}
    <footer style="text-align:center;color:var(--muted);font-size:.8rem;margin-top:2rem">
      개인 학습용 · 2026-06-26 생성
    </footer>
  </main>
</div>
<script>
document.getElementById('search').addEventListener('input', function(e) {{
  const q = e.target.value.trim().toLowerCase();
  document.querySelectorAll('.q-card').forEach(card => {{
    const text = card.textContent.toLowerCase();
    const num = card.id.replace('q','');
    card.style.display = !q || text.includes(q) || num.includes(q) ? '' : 'none';
  }});
  document.querySelectorAll('.day-block').forEach(day => {{
    const visible = [...day.querySelectorAll('.q-card')].some(c => c.style.display !== 'none');
    day.style.display = visible ? '' : 'none';
  }});
}});
</script>
</body>
</html>"""


def main():
    global EXPLANATIONS
    EXPLANATIONS = load_explanations()
    text = extract_text()
    Path("/workspace/scripts/extracted.txt").write_text(text, encoding="utf-8")
    items = parse_questions(text)
    print(f"Parsed {len(items)} questions")
    nums = sorted(it["num"] for it in items)
    print(f"Range: {nums[0]:03d} - {nums[-1]:03d}")
    missing = [n for n in range(1, 390) if n not in set(nums)]
    if missing:
        print(f"Missing ({len(missing)}): {missing[:20]}...")
    html_out = generate_html(items)
    OUT.write_text(html_out, encoding="utf-8")
    print(f"Written {OUT} ({len(html_out)} bytes)")


if __name__ == "__main__":
    main()
