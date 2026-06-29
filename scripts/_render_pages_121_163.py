#!/usr/bin/env python3
"""Render scripts/pages_121_163.py."""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).with_name("pages_121_163.py")
L: list[str] = []


def add(*lines: str) -> None:
    L.extend(lines)


def memo(n: int) -> None:
    add(
        f"<!-- ===== p.{n} memo ===== -->",
        f'<div class="page" id="page-{n:03d}">',
        '  <div class="brand abs">전기치트키</div>',
        '  <div class="content">',
        '    <p class="memo-label">memo</p>',
        '    <hr class="memo-line">',
        "  </div>",
        f'  <div class="foot-r abs">전기기사 실기 단답비급 • {n}</div>',
        "</div>",
        "",
    )


def day(n: int, d: int, topics: str) -> None:
    add(
        f"<!-- ===== p.{n} DAY {d} ===== -->",
        f'<div class="page" id="page-{n:03d}">',
        f'  <div class="day-banner abs">DAY {d}</div>',
        f'  <div class="topic-box abs">{topics}</div>',
        "</div>",
        "",
    )


def page_open(n: int, label: str, *, day_tag: str = "", brand: str = "foot-r", sec: str = "", compact: bool = False, top: str = ""):
    add(f"<!-- ===== p.{n} {label} ===== -->", f'<div class="page" id="page-{n:03d}">')
    if day_tag:
        add(f'  <div class="day-tag abs">{day_tag}</div>')
    elif brand == "foot-r":
        add('  <div class="brand abs">전기치트키</div>')
    if sec:
        add(f'  <div class="sec-title abs">{sec}</div>')
    cls = "content compact" if compact else "content"
    style = f' style="{top}"' if top else ""
    add(f'  <div class="{cls}"{style}>')


def page_close(n: int, brand: str = "foot-r") -> None:
    add("  </div>")
    if brand == "foot-r":
        add(f'  <div class="foot-r abs">전기기사 실기 단답비급 • {n}</div>')
    else:
        add(f'  <div class="brand-l abs">{n} • 전기치트키</div>')
    add("</div>", "")


def q(num: str, text: str, *ans_lines: str) -> None:
    add(
        '    <div class="q">',
        f'      <div class="q-num">{num}</div><hr class="q-hline">',
        f'      <p class="q-text">{text}</p>',
    )
    for a in ans_lines:
        add(f'      {a}')
    add("    </div>")


# --- pages ---
add(
    "<!-- ===== p.121 292~294 ===== -->",
    '<div class="page" id="page-121">',
    '  <div class="brand abs">전기치트키</div>',
    '  <div class="content">',
)
q("292.", "UPS가 동작되면 전력 공급을 위한 축전지가 필요한데 그 때의 축전지 용량을 구하는 공식을 쓰시오. (단, 사용 기호에 대한 의미도 설명하도록 하시오.)",
  r'      <p class="formula">$C = \dfrac{1}{L} \cdot K \cdot I$ [Ah]</p>',
  '      <p class="ans-line">$C$ : <span class="ans">축전지 용량[Ah]</span></p>',
  '      <p class="ans-line">$L$ : <span class="ans">보수율(경년용량 저하율)</span></p>',
  '      <p class="ans-line">$K$ : <span class="ans">용량환산 시간계수</span></p>',
  '      <p class="ans-line">$I$ : <span class="ans">방전전류[A]</span></p>')
q("293.", "연축전지 설비의 초기에 전해액 비중이 저하되고, 전압계가 역전하였다. 어떤 원인으로 추정될 수 있는가?",
  '      <p class="ans-line"><span class="ans">축전지의 역접속</span></p>')
q("294.", "충전장치고장, 과충전, 액면 저하로 인한 극판 노출, 교류분 전류의 유입 과대 등의 원인에 의하여 발생될 수 있는 현상은?",
  '      <p class="ans-line"><span class="ans">축전지의 현저한 온도상승 또는 소손</span></p>')
page_close(121)

page_open(122, "295~297", day_tag="단답비급 DAY 10")
q("295.", "무정전 전원은 정전 시 사용하지만 평상 운전 시에는 예비전원으로 200[Ah]의 연축전지 100개가 설치되었다. 부동충전 시에 발생하는 가스, 그리고 충전이 부족할 경우 극판에 발생하는 현상 등에 대하여 설명하시오.",
  '      <p class="ans-line">① 충전 시 발생되는 가스 : <span class="ans">수소가스</span></p>',
  '      <p class="ans-line">② 현상 : <span class="ans">설페이션 현상</span></p>')
q("296.", "연축전지 사용중 고장현상이 다음과 같을 때 이의 추정 원인을 쓰시오.",
  '      <p class="ans-line">1. 전체 셀의 전압 불균일이 크고 비중이 낮다. : <span class="ans">충전 부족으로 장시간 방치한 경우</span></p>',
  '      <p class="ans-line">2. 전체 셀의 비중이 높다. : <span class="ans">증류수가 부족한 경우</span></p>',
  '      <p class="ans-line">3. 전해액 변색, 충전하지 않고 그냥 두어도 다량으로 가스가 발생한다. : <span class="ans">전해액 불순물의 혼입</span></p>')
q("297.", "묽은 황산의 농도는 표준이고, 액면이 저하하여 극판이 노출되어 있다. 어떤 조치를 하여야 하는가?",
  '      <p class="ans-line"><span class="ans">증류수 보충</span></p>')
page_close(122, "brand-l")

memo(123)
day(124, 11, "UPS<br>고장 및 사고")

page_open(125, "298~299", sec="UPS", top="top:108px;")
q("298.", "UPS를 우리말로 하면 어떤 것을 뜻하는가?", '      <p class="ans-line"><span class="ans">무정전 전원 공급 장치</span></p>')
q("299.", '다음은 컴퓨터 등의 중요한 부하에 대한 무정전 전원공급을 위한 그림이다. "(가)"~"(마)"에 적당한 전기 시설물의 명칭을 쓰시오.',
  "      <!--IMG:p125_diag299-->",
  '      <p class="ans-line">(가) <span class="ans">자동전압조정기(AVR)</span> &nbsp; (나) <span class="ans">절체용 개폐기</span></p>',
  '      <p class="ans-line">(다) <span class="ans">정류기(컨버터)</span> &nbsp; (라) <span class="ans">역변환장치(인버터)</span> &nbsp; (마) <span class="ans">축전지</span></p>')
page_close(125)

page_open(126, "300", day_tag="단답비급 DAY 11")
q("300.", "현재 비상 전원으로 쓰이는 UPS의 원리에 대하여 개략의 블록다이어그램을 그려서 설명하시오.",
  "      <!--IMG:p126_diag300-->",
  '      <p><b>• 설명</b></p>',
  '      <p class="ans-line">UPS 설비는 <span class="ans">직류 전원장치</span>와 <span class="ans">사이리스터(컨버터, 인버터)</span>를 조합한 것으로서 <span class="ans">평상시</span>에는 <span class="ans">상용</span> 전원을 <span class="ans">정류기(컨버터)</span>를 통해 <span class="ans">직류</span>로 변환하여 <span class="ans">축전지</span>를 <span class="ans">충전</span>한다. 이때 <span class="ans">정류된 직류</span>는 <span class="ans">인버터</span>에 의해 <span class="ans">교류</span>로 변환되어 <span class="ans">절체 스위치</span>를 통하여 부하에 전원을 공급한다. <span class="ans">상용전원 정전시</span>에는 <span class="ans">축전지</span>의 <span class="ans">직류</span>를 <span class="ans">인버터</span>에 의하여 안정된 <span class="ans">교류</span>로 다시 변환하여 부하에 전력을 공급한다. <span class="ans">비상발전기(비상전원)</span>는 축전지 용량이 부족한 경우 운전한다.</p>')
page_close(126, "brand-l")

page_open(127, "301~302")
q("301.", "UPS 장치 시스템의 중심부분을 구성하는 CVCF의 기본 회로를 보고 다음 각 물음에 답하시오.",
  '      <p class="ans-line">(1) UPS 장치는 어떤 장치인가? <span class="ans">무정전 전원 공급 장치</span></p>',
  '      <p class="ans-line">(2) CVCF는 무엇을 뜻하는가? <span class="ans">정전압 정주파수 장치</span></p>',
  '      <p class="ans-line">(3) 회로의 ①, ②에 해당되는 것은? <span class="ans">① 컨버터 ② 인버터</span></p>')
q("302.", "UPS에서 AC→DC부와 DC→AC부로 변환하는 명칭을 각각 무엇이라 부르는가?",
  '      <p class="ans-line">① AC→DC : <span class="ans">컨버터</span></p>',
  '      <p class="ans-line">② DC→AC : <span class="ans">인버터</span></p>')
page_close(127)

page_open(128, "303", day_tag="단답비급 DAY 11", compact=True)
q("303.", "컴퓨터나 마이크로프로세서에 사용하기 위하여 무정전전원장치(UPS)를 구성하려고 한다. 다음 각 물음에 답하시오.",
  "      <!--IMG:p128_diag303-->",
  '      <p class="ans-line">(1) 그림의 ①~④에 들어갈 기기 또는 명칭을 쓰고 그 역할에 대하여 간단히 설명하시오.</p>',
  '      <table class="tbl">',
  "        <tr><th>명칭</th><th>역할</th></tr>",
  '        <tr><td><span class="ans">컨버터</span></td><td><span class="ans">교류</span>를 <span class="ans">직류</span>로 변환</td></tr>',
  '        <tr><td><span class="ans">축전지</span></td><td>충전장치에 의해 변환된 <span class="ans">직류 전력</span>을 저장</td></tr>',
  '        <tr><td><span class="ans">인버터</span></td><td><span class="ans">직류</span>를 사용 주파수의 <span class="ans">교류</span> 전압으로 변환</td></tr>',
  '        <tr><td><span class="ans">동기절체 스위치</span></td><td>상용전원 <span class="ans">정전 시 인버터 회로</span>로 <span class="ans">절체</span>되어 부하에 <span class="ans">무정전</span>으로 <span class="ans">전력</span>을 <span class="ans">공급</span>하기 위한 장치</td></tr>',
  "      </table>",
  '      <p class="ans-line">(2) Bypass Transformer를 설치하여 회로를 구성하는 이유를 설명하시오.</p>',
  '      <p class="ans-line">① 회로의 <span class="ans">절연</span></p>',
  '      <p class="ans-line">② UPS나 축전지의 <span class="ans">점검 및 고장</span> 시에도 부하에 <span class="ans">정상적</span>으로 <span class="ans">전력</span>을 <span class="ans">공급</span>하기 위함</p>')
page_close(128, "brand-l")

# Continue in part 2 - append via exec
exec(Path(__file__).with_name("_render_pages_121_163_p2.py").read_text(encoding="utf-8"), globals())

OUT.write_text(
    '#!/usr/bin/env python3\n"""HTML transcription for manual pages 121-163."""\n\n'
    "PAGES_121_163 = r\"\"\"\n" + "\n".join(L) + '\n\"\"\"\n',
    encoding="utf-8",
)
print(f"Wrote {OUT} ({OUT.stat().st_size} bytes, {len(L)} lines)")
