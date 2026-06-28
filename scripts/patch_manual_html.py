#!/usr/bin/env python3
"""Apply KaTeX/CSS improvements and append transcribed pages to dandap_manual.html."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"

KATEX_HEAD = """  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
"""

EXTRA_CSS = """
    .content, .q-text, .ans-line, .box, table.tbl td, table.tbl th {
      overflow-wrap: anywhere;
      word-break: keep-all;
      max-width: 100%;
    }
    .formula-row { gap: 14px; }
    .formula-row > span { max-width: 100%; overflow-x: auto; }
    img { max-width: 100%; height: auto; }
    .katex { font-size: 1.02em; }
    .katex-display { margin: 0.4em 0; overflow-x: auto; overflow-y: hidden; }
    @media (max-width: 640px) {
      .pages { padding: 2.8rem 0 1.5rem; gap: 6px; align-items: stretch; }
      .page {
        transform-origin: top center;
        transform: scale(calc((100vw - 6px) / 595));
        margin-bottom: calc(-842px * (1 - (100vw - 6px) / 595));
      }
    }
"""

KATEX_SCRIPTS = """
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function () {
  if (typeof renderMathInElement === "function") {
    renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
      ],
      throwOnError: false
    });
  }
});
</script>
"""

NEW_PAGES = r"""
<!-- ===== p.32 059~060 ===== -->
<div class="page" id="page-032">
  <div class="day-tag abs">단답비급 DAY 3</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">059.</div><hr class="q-hline">
      <p class="q-text">다음은 과부하 보호장치의 설치위치에 대한 내용이다. 주어진 조건에 의하여 (가)의 거리는 몇 [m] 이내인가? <span class="ans">3[m]</span></p>
      <p class="q-text" style="margin-top:6px;"><b>【조건】</b></p>
      <p class="ans-line">1. 분기점 O와 $P_2$ 사이에 다른 분기회로 및 콘센트의 설치가 없을 것.</p>
      <p class="ans-line">2. 단락의 위험과 화재 및 인체에 대한 위험성이 최소화 되도록 시설할 것.</p>
      <p class="ans-line">3. 분기회로도체 $S_2$는 전원 측 보호장치 $P_1$에 의해 단락보호가 보장되지 않는다.</p>
      <img src="../assets/images/manual/crops/p032_diag059.png" style="width:100%;max-height:220px;object-fit:contain;margin:8px 0;" alt="과부하 보호장치 회로도">
    </div>
    <div class="q">
      <div class="q-num">060.</div><hr class="q-hline">
      <p class="q-text">아래의 표와 같이 규모별로 표준적인 콘센트 수와 바람직한 콘센트 수를 규정하고 있다. 아래 표를 완성하시오.</p>
      <table class="tbl">
        <tr><th>방의 크기 [$m^2$]</th><th>표준적인 설치 수</th></tr>
        <tr><td>5 미만</td><td><span class="ans">1</span></td></tr>
        <tr><td>5 ~ 10 미만</td><td><span class="ans">2</span></td></tr>
        <tr><td>10 ~ 15 미만</td><td><span class="ans">3</span></td></tr>
        <tr><td>15 ~ 20 미만</td><td><span class="ans">3</span></td></tr>
        <tr><td>부억</td><td><span class="ans">2</span></td></tr>
      </table>
    </div>
  </div>
  <div class="brand-l abs">32 • 전기치트키</div>
</div>

<!-- ===== p.33 061~062 ===== -->
<div class="page" id="page-033">
  <div class="brand abs">전기치트키</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">061.</div><hr class="q-hline">
      <p class="q-text">예상이 곤란한 콘센트, 비틀어 끼우는 접속기, 소켓 등이 있는 경우 수구의 종류에 따른 예상 부하[VA/개]를 쓰시오.</p>
      <p class="ans-line">1. 콘센트 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span class="ans">150</span> [VA/개]</p>
      <p class="ans-line">2. 소형 전등수구 &nbsp; <span class="ans">150</span> [VA/개]</p>
      <p class="ans-line">3. 대형 전등수구 &nbsp; <span class="ans">300</span> [VA/개]</p>
    </div>
    <div class="q">
      <div class="q-num">062.</div><hr class="q-hline">
      <p class="q-text">다른 조건을 고려하지 않는다면 수용가 설비의 인입구로부터 기기까지의 전압강하는 다음 표의 값 이하여야 한다.</p>
      <p class="q-text" style="margin-top:6px;">1. 아래의 표를 채우시오. [수용가 설비의 전압강하]</p>
      <table class="tbl" style="font-size:9.5pt;">
        <tr><th>설비의 유형</th><th>조명 [%]</th><th>기타 [%]</th></tr>
        <tr><td>A - 저압으로 수전하는 경우</td><td>① <span class="ans">3</span></td><td>③ <span class="ans">5</span></td></tr>
        <tr><td>B - 고압 이상으로 수전하는 경우<sup>a</sup></td><td>② <span class="ans">6</span></td><td>④ <span class="ans">8</span></td></tr>
      </table>
      <p class="q-text" style="font-size:9pt;margin-top:4px;"><sup>a</sup>가능한 한 최종회로 내의 전압강하가 A 유형의 값을 넘지 않도록 하는 것이 바람직하다.</p>
      <p class="q-text" style="font-size:9.5pt;margin-top:4px;">사용자의 배선설비가 100[m]를 넘는 부분의 전압강하는 미터 당 0.005[%] 증가할 수 있으나 이러한 증가분은 0.5[%]를 넘지 않아야 한다.</p>
      <p class="q-text" style="margin-top:8px;">2. 표보다 더 큰 전압강하를 허용할 수 있는 경우 2가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">기동 시간 중의 전동기</span></p>
      <p class="ans-line">② <span class="ans">돌입전류가 큰 기타 기기</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 33</div>
</div>

<!-- ===== p.34 063~064 ===== -->
<div class="page" id="page-034">
  <div class="day-tag abs">단답비급 DAY 3</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">063.</div><hr class="q-hline">
      <p class="q-text">정크션 박스(Joint Box)와 풀 박스(Pull Box)의 용도를 쓰시오.</p>
      <p class="ans-line">1. <b>정크션 박스(Joint Box)</b> : 전선 상호간 접속 시 <span class="ans">접속 부분</span>이 외부로 <span class="ans">노출</span>되지 <span class="ans">않도록</span> 하기 위해</p>
      <p class="ans-line">2. <b>풀 박스(Pull Box)</b> : 전선의 통과를 <span class="ans">쉽게</span> 하기 위하여 <span class="ans">배관</span>의 <span class="ans">도중</span>에 설치</p>
    </div>
    <div class="q">
      <div class="q-num">064.</div><hr class="q-hline">
      <p class="q-text">부품명을 작성하시오.</p>
      <table class="tbl" style="font-size:9pt;">
        <tr><th style="width:18%;">부품명</th><th>특징</th></tr>
        <tr><td><span class="ans">로크너트</span></td><td>관과 박스를 접속할 경우 파이프 나사를 죄어 고정 시키는 데 사용되며 6각형과 기어형이 있다.</td></tr>
        <tr><td><span class="ans">부싱</span></td><td>전선 관단에 끼우고 전선을 넣거나 빼는데 있어서 <span class="ans">전선의 피복을 보호</span>하여 전선이 손상되지 않게 하는 것으로 금속제와 합성수지제의 2종류가 있다.</td></tr>
        <tr><td><span class="ans">커플링</span></td><td><span class="ans">금속관 상호 접속</span> 또는 관과 노멀밴드와의 접속에 사용되며 내면에 나사가 있으며 관의 양측을 돌리어 사용할 수 없는 경우 유니온 커플링을 사용한다.</td></tr>
        <tr><td><span class="ans">새들</span></td><td>노출배관에서 <span class="ans">금속관을 조영재에 고정</span>시키는데 사용되며 합성수지 전선관, 가요전선관, 케이블 공사에도 사용된다.</td></tr>
        <tr><td><span class="ans">노멀 밴드</span></td><td>배관의 <span class="ans">직각 굴곡</span>에 사용하며 양단에 나사가 나있어 관과 접속에는 커플링을 사용한다.</td></tr>
        <tr><td><span class="ans">링 리듀서</span></td><td>금속관을 아웃렛 박스에 노크아웃에 취부할 때 <span class="ans">노크아웃의 구멍이 관의 구멍보다 클 때</span> 사용된다.</td></tr>
        <tr><td><span class="ans">스위치 박스</span></td><td>매입형의 스위치나 콘센트를 <span class="ans">고정</span>하는데 사용되며 1개용, 2개용, 3개용 등이 있다.</td></tr>
        <tr><td><span class="ans">아웃렛 박스</span></td><td>전선관 공사에 있어 전등 기구나 점멸기 또는 콘센트의 고정, 접속함으로 사용되며 4각 및 8각이 있다.</td></tr>
      </table>
    </div>
  </div>
  <div class="brand-l abs">34 • 전기치트키</div>
</div>

<!-- ===== p.35 065 ===== -->
<div class="page" id="page-035">
  <div class="brand abs">전기치트키</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">065.</div><hr class="q-hline">
      <p class="q-text">심야 전력용 기기를 종량제로 하는 경우 인입구 장치 배선은 다음과 같다. 물음에 답하여라.</p>
      <img src="../assets/images/manual/crops/p035_diag065.png" style="width:100%;max-height:280px;object-fit:contain;margin:8px 0;" alt="심야전력 배선도">
      <p class="q-text" style="margin-top:6px;">1. Ⓐ~Ⓔ의 명칭은?</p>
      <table class="tbl" style="font-size:9.5pt;">
        <tr><th>Ⓐ</th><th>Ⓑ</th><th>Ⓒ</th><th>Ⓓ</th><th>Ⓔ</th></tr>
        <tr>
          <td><span class="ans">타임스위치</span></td>
          <td><span class="ans">전력량계</span></td>
          <td><span class="ans">인입구 장치<br>(배선용 차단기)</span></td>
          <td><span class="ans">전력량계</span></td>
          <td><span class="ans">인입구 장치</span></td>
        </tr>
      </table>
      <p class="q-text" style="margin-top:10px;">2. 인입구 장치에서 심야 전력 기기까지 배선 공사 방법은?</p>
      <p class="ans-line"><span class="ans">합성수지관공사, 금속관공사, 금속제 가요전선관공사, 케이블공사</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 35</div>
</div>

<!-- ===== p.36 DAY4 구분 ===== -->
<div class="page" id="page-036">
  <div class="day-banner abs">DAY 4</div>
  <div class="topic-box abs">조명<br>전동기 I</div>
  <img class="abs" src="../assets/images/manual/crops/p036_day4_char.png" style="left:80px;top:500px;width:260px;" alt="">
</div>

<!-- ===== p.37 조명 066~069 ===== -->
<div class="page" id="page-037">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">조명</div>
  <div class="content" style="top:118px;">
    <div class="q">
      <div class="q-num">066.</div><hr class="q-hline">
      <p class="q-text">어느 광원의 광색이 어느 온도의 흑체의 광색과 같을 때 그 흑체의 온도를 이 광원의 무엇이라 하는지 쓰시오.</p>
      <p class="ans-line"><span class="ans">색온도</span></p>
    </div>
    <div class="q">
      <div class="q-num">067.</div><hr class="q-hline">
      <p class="q-text">빛의 분광 특성이 색의 보임에 미치는 효과를 말하며, 동일한 색을 가진 것이라도 조명하는 빛에 따라 다르게 보이는 특성을 무엇이라 하는지 쓰시오.</p>
      <p class="ans-line"><span class="ans">연색성</span></p>
    </div>
    <div class="q">
      <div class="q-num">068.</div><hr class="q-hline">
      <p class="q-text">조명의 전등 효율(Lamp Efficiency)과 발광 효율(Luminous Efficiency)에 대해 설명하시오.</p>
      <p class="ans-line">(1) 전등 효율 : 전력소비에 대한 전발산광속의 비율, $\eta = F/P$ [lm/W]</p>
      <p class="ans-line">(2) 발광 효율 : 방사속에 대한 광속의 비율, $\varepsilon = F/\varphi$ [lm/W]</p>
    </div>
    <div class="q">
      <div class="q-num">069.</div><hr class="q-hline">
      <p class="q-text">조명에서 광원이 발광하는 원리 3가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">온도 방사</span></p>
      <p class="ans-line">② <span class="ans">전기 루미네센스</span></p>
      <p class="ans-line">③ <span class="ans">전계 루미네센스</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 37</div>
</div>
"""

REPLACEMENTS = [
    # KaTeX head
    (
        "  <link href=\"https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Nanum+Myeongjo:wght@700&display=swap\" rel=\"stylesheet\">",
        "  <link href=\"https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&family=Nanum+Myeongjo:wght@700&display=swap\" rel=\"stylesheet\">\n"
        + KATEX_HEAD.rstrip(),
    ),
    # CSS overflow + mobile
    (
        "    .formula-row { display: flex; gap: 40px; flex-wrap: wrap; margin-top: 6px; }",
        "    .formula-row { display: flex; gap: 40px; flex-wrap: wrap; margin-top: 6px; }"
        + EXTRA_CSS,
    ),
    # toolbar
    (
        '<span id="pg-info">p.1–31 (DAY1~3 진행중) · 직접 전사</span>',
        '<span id="pg-info">p.1–37 (DAY1~4 진행중) · 직접 전사</span>',
    ),
    # 012 answers + formulas
    (
        '      <p class="ans-line">(1) 전압강하 &nbsp;&nbsp;&nbsp; <span class="ans">1/2배</span></p>\n'
        '      <p class="ans-line">(2) 전압강하율 &nbsp; <span class="ans">1/4배</span></p>\n'
        '      <p class="ans-line">(3) 선로손실 &nbsp;&nbsp;&nbsp; <span class="ans">1/4배</span></p>\n'
        '      <p class="ans-line">(4) 선로손실률 &nbsp; <span class="ans">1/4배</span></p>\n'
        '      <div class="formula-row formula">\n'
        '        <span>(1) e = P/V (R + X tanθ)</span>\n'
        '        <span>(2) ε = P/V² (R + X tanθ)</span>\n'
        '      </div>\n'
        '      <div class="formula-row formula">\n'
        '        <span>(3) P<sub>l</sub> = P²R / (V² cos²θ)</span>\n'
        '        <span>(4) K = PR / (V² cos²θ)</span>\n'
        '      </div>',
        '      <p class="ans-line">(1) 전압강하 &nbsp;&nbsp;&nbsp; <span class="ans">$\\frac{1}{2}$배</span></p>\n'
        '      <p class="ans-line">(2) 전압강하율 &nbsp; <span class="ans">$\\frac{1}{4}$배</span></p>\n'
        '      <p class="ans-line">(3) 선로손실 &nbsp;&nbsp;&nbsp; <span class="ans">$\\frac{1}{4}$배</span></p>\n'
        '      <p class="ans-line">(4) 선로손실률 &nbsp; <span class="ans">$\\frac{1}{4}$배</span></p>\n'
        '      <div class="formula-row formula">\n'
        '        <span>(1) $e = \\frac{P}{V}(R + X\\tan\\theta)$</span>\n'
        '        <span>(2) $\\varepsilon = \\frac{P}{V^2}(R + X\\tan\\theta)$</span>\n'
        '      </div>\n'
        '      <div class="formula-row formula">\n'
        '        <span>(3) $P_l = \\frac{P^2 R}{V^2 \\cos^2\\theta}$</span>\n'
        '        <span>(4) $K = \\frac{PR}{V^2 \\cos^2\\theta}$</span>\n'
        '      </div>',
    ),
    # 021
    (
        '      <p class="formula" style="text-align:center;margin:10px 0;">E₀ = 24.3 m₀ m₁ δ d log₁₀ D/r [kV]</p>\n'
        '      <p class="q-text">1. 기온 t[℃]에서의 기압을 b[mmHg]라고 할 때 δ = 0.386b/(273+t)로 나타내는데 이 δ는 무엇을 의미하는지 쓰시오. <span class="ans">상대 공기 밀도</span></p>\n'
        '      <p class="q-text" style="margin-top:6px;">2. m₁이 날씨에 의한 계수라면, m₀는 무엇에 의한 계수인지 쓰시오. <span class="ans">전선표면의 상태계수</span></p>',
        '      <p class="formula" style="text-align:center;margin:10px 0;">$$E_0 = 24.3\\, m_0\\, m_1\\, \\delta\\, d\\, \\log_{10}\\frac{D}{r}\\;[\\mathrm{kV}]$$</p>\n'
        '      <p class="q-text">1. 기온 $t$[℃]에서의 기압을 $b$[mmHg]라고 할 때 $\\delta = \\frac{0.386b}{273+t}$로 나타내는데 이 $\\delta$는 무엇을 의미하는지 쓰시오. <span class="ans">상대 공기 밀도</span></p>\n'
        '      <p class="q-text" style="margin-top:6px;">2. $m_1$이 날씨에 의한 계수라면, $m_0$는 무엇에 의한 계수인지 쓰시오. <span class="ans">전선표면의 상태계수</span></p>',
    ),
    # 033
    (
        '      <p class="formula">5ωL &gt; 1/(5ωC) → ωL &gt; 1/(5²ωC) = 0.04 × 1/(ωC)</p>',
        '      <p class="formula">$$5\\omega L &gt; \\frac{1}{5\\omega C} \\Rightarrow \\omega L &gt; \\frac{1}{5^2\\omega C} = 0.04 \\times \\frac{1}{\\omega C}$$</p>',
    ),
    # 049
    (
        '      <p class="q-text">배전선의 기본파 전압 실효값이 V₁[V], 고조파 전압의 실효값이 V₃[V], V₅[V], Vₙ[V] 이다. <span class="ans">THD</span>(Total Harmonics Distortion)의 정의와 계산식을 쓰시오.</p>\n'
        '      <p style="margin-top:8px;"><b>[정의]</b> 기본파의 <span class="ans">실효값에</span> 대한 <span class="ans">전고조파의</span> <span class="ans">실효값의</span> 비</p>\n'
        '      <p style="margin-top:6px;"><b>[계산식]</b> 전고조파왜율 THD = √(V₃² + V₅² + Vₙ²) / V₁</p>',
        '      <p class="q-text">배전선의 기본파 전압 실효값이 $V_1$[V], 고조파 전압의 실효값이 $V_3$[V], $V_5$[V], $V_n$[V] 이다. <span class="ans">THD</span>(Total Harmonics Distortion)의 정의와 계산식을 쓰시오.</p>\n'
        '      <p style="margin-top:8px;"><b>[정의]</b> 기본파의 <span class="ans">실효값에</span> 대한 <span class="ans">전고조파의</span> <span class="ans">실효값의</span> 비</p>\n'
        '      <p style="margin-top:6px;"><b>[계산식]</b> 전고조파왜율 $\\mathrm{THD} = \\dfrac{\\sqrt{V_3^2 + V_5^2 + V_n^2}}{V_1}$</p>',
    ),
]


def main() -> None:
    html = HTML.read_text(encoding="utf-8")

    for old, new in REPLACEMENTS:
        if old not in html:
            raise SystemExit(f"Patch target not found:\n{old[:80]}...")
        html = html.replace(old, new, 1)

    if 'id="page-032"' in html:
        print("Pages 32+ already present, skipping append")
    else:
        marker = "\n</div>\n</body>\n</html>"
        if marker not in html:
            raise SystemExit("End marker not found")
        html = html.replace(marker, NEW_PAGES + marker, 1)

    if "katex.min.js" not in html:
        html = html.replace("</body>", KATEX_SCRIPTS + "</body>", 1)

    HTML.write_text(html, encoding="utf-8")
    print(f"Patched {HTML}")


if __name__ == "__main__":
    main()
