#!/usr/bin/env python3
"""HTML transcription for manual pages 121-163."""

PAGES_121_163 = r"""
<!-- ===== p.121 292~294 ===== -->
<div class="page" id="page-121">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">292.</div><hr class="q-hline">
      <p class="q-text">UPS가 동작되면 전력 공급을 위한 축전지가 필요한데 그 때의 축전지 용량을 구하는 공식을 쓰시오. (단, 사용 기호에 대한 의미도 설명하도록 하시오.)</p>
            <p class="formula">$C = \dfrac{1}{L} \cdot K \cdot I$ [Ah]</p>
            <p class="ans-line">$C$ : <span class="ans">축전지 용량[Ah]</span></p>
            <p class="ans-line">$L$ : <span class="ans">보수율(경년용량 저하율)</span></p>
            <p class="ans-line">$K$ : <span class="ans">용량환산 시간계수</span></p>
            <p class="ans-line">$I$ : <span class="ans">방전전류[A]</span></p>
    </div>
    <div class="q">
      <div class="q-num">293.</div><hr class="q-hline">
      <p class="q-text">연축전지 설비의 초기에 전해액 비중이 저하되고, 전압계가 역전하였다. 어떤 원인으로 추정될 수 있는가?</p>
            <p class="ans-line"><span class="ans">축전지의 역접속</span></p>
    </div>
    <div class="q">
      <div class="q-num">294.</div><hr class="q-hline">
      <p class="q-text">충전장치고장, 과충전, 액면 저하로 인한 극판 노출, 교류분 전류의 유입 과대 등의 원인에 의하여 발생될 수 있는 현상은?</p>
            <p class="ans-line"><span class="ans">축전지의 현저한 온도상승 또는 소손</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 121</div>
</div>

<!-- ===== p.122 295~297 ===== -->
<div class="page" id="page-122">
  <div class="day-tag abs">단답비급 DAY 10</div>
  <div class="content">
    <div class="q">
      <div class="q-num">295.</div><hr class="q-hline">
      <p class="q-text">무정전 전원은 정전 시 사용하지만 평상 운전 시에는 예비전원으로 200[Ah]의 연축전지 100개가 설치되었다. 부동충전 시에 발생하는 가스, 그리고 충전이 부족할 경우 극판에 발생하는 현상 등에 대하여 설명하시오.</p>
            <p class="ans-line">① 충전 시 발생되는 가스 : <span class="ans">수소가스</span></p>
            <p class="ans-line">② 현상 : <span class="ans">설페이션 현상</span></p>
    </div>
    <div class="q">
      <div class="q-num">296.</div><hr class="q-hline">
      <p class="q-text">연축전지 사용중 고장현상이 다음과 같을 때 이의 추정 원인을 쓰시오.</p>
            <p class="ans-line">1. 전체 셀의 전압 불균일이 크고 비중이 낮다. : <span class="ans">충전 부족으로 장시간 방치한 경우</span></p>
            <p class="ans-line">2. 전체 셀의 비중이 높다. : <span class="ans">증류수가 부족한 경우</span></p>
            <p class="ans-line">3. 전해액 변색, 충전하지 않고 그냥 두어도 다량으로 가스가 발생한다. : <span class="ans">전해액 불순물의 혼입</span></p>
    </div>
    <div class="q">
      <div class="q-num">297.</div><hr class="q-hline">
      <p class="q-text">묽은 황산의 농도는 표준이고, 액면이 저하하여 극판이 노출되어 있다. 어떤 조치를 하여야 하는가?</p>
            <p class="ans-line"><span class="ans">증류수 보충</span></p>
    </div>
  </div>
  <div class="brand-l abs">122 • 전기치트키</div>
</div>

<!-- ===== p.123 memo ===== -->
<div class="page" id="page-123">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 123</div>
</div>

<!-- ===== p.124 DAY 11 ===== -->
<div class="page" id="page-124">
  <div class="day-banner abs">DAY 11</div>
  <div class="topic-box abs">UPS<br>고장 및 사고</div>
</div>

<!-- ===== p.125 298~299 ===== -->
<div class="page" id="page-125">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">UPS</div>
  <div class="content" style="top:108px;">
    <div class="q">
      <div class="q-num">298.</div><hr class="q-hline">
      <p class="q-text">UPS를 우리말로 하면 어떤 것을 뜻하는가?</p>
            <p class="ans-line"><span class="ans">무정전 전원 공급 장치</span></p>
    </div>
    <div class="q">
      <div class="q-num">299.</div><hr class="q-hline">
      <p class="q-text">다음은 컴퓨터 등의 중요한 부하에 대한 무정전 전원공급을 위한 그림이다. "(가)"~"(마)"에 적당한 전기 시설물의 명칭을 쓰시오.</p>
            <!--IMG:p125_diag299-->
            <p class="ans-line">(가) <span class="ans">자동전압조정기(AVR)</span> &nbsp; (나) <span class="ans">절체용 개폐기</span></p>
            <p class="ans-line">(다) <span class="ans">정류기(컨버터)</span> &nbsp; (라) <span class="ans">역변환장치(인버터)</span> &nbsp; (마) <span class="ans">축전지</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 125</div>
</div>

<!-- ===== p.126 300 ===== -->
<div class="page" id="page-126">
  <div class="day-tag abs">단답비급 DAY 11</div>
  <div class="content">
    <div class="q">
      <div class="q-num">300.</div><hr class="q-hline">
      <p class="q-text">현재 비상 전원으로 쓰이는 UPS의 원리에 대하여 개략의 블록다이어그램을 그려서 설명하시오.</p>
            <!--IMG:p126_diag300-->
            <p><b>• 설명</b></p>
            <p class="ans-line">UPS 설비는 <span class="ans">직류 전원장치</span>와 <span class="ans">사이리스터(컨버터, 인버터)</span>를 조합한 것으로서 <span class="ans">평상시</span>에는 <span class="ans">상용</span> 전원을 <span class="ans">정류기(컨버터)</span>를 통해 <span class="ans">직류</span>로 변환하여 <span class="ans">축전지</span>를 <span class="ans">충전</span>한다. 이때 <span class="ans">정류된 직류</span>는 <span class="ans">인버터</span>에 의해 <span class="ans">교류</span>로 변환되어 <span class="ans">절체 스위치</span>를 통하여 부하에 전원을 공급한다. <span class="ans">상용전원 정전시</span>에는 <span class="ans">축전지</span>의 <span class="ans">직류</span>를 <span class="ans">인버터</span>에 의하여 안정된 <span class="ans">교류</span>로 다시 변환하여 부하에 전력을 공급한다. <span class="ans">비상발전기(비상전원)</span>는 축전지 용량이 부족한 경우 운전한다.</p>
    </div>
  </div>
  <div class="brand-l abs">126 • 전기치트키</div>
</div>

<!-- ===== p.127 301~302 ===== -->
<div class="page" id="page-127">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">301.</div><hr class="q-hline">
      <p class="q-text">UPS 장치 시스템의 중심부분을 구성하는 CVCF의 기본 회로를 보고 다음 각 물음에 답하시오.</p>
            <p class="ans-line">(1) UPS 장치는 어떤 장치인가? <span class="ans">무정전 전원 공급 장치</span></p>
            <p class="ans-line">(2) CVCF는 무엇을 뜻하는가? <span class="ans">정전압 정주파수 장치</span></p>
            <p class="ans-line">(3) 회로의 ①, ②에 해당되는 것은? <span class="ans">① 컨버터 ② 인버터</span></p>
    </div>
    <div class="q">
      <div class="q-num">302.</div><hr class="q-hline">
      <p class="q-text">UPS에서 AC→DC부와 DC→AC부로 변환하는 명칭을 각각 무엇이라 부르는가?</p>
            <p class="ans-line">① AC→DC : <span class="ans">컨버터</span></p>
            <p class="ans-line">② DC→AC : <span class="ans">인버터</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 127</div>
</div>

<!-- ===== p.128 303 ===== -->
<div class="page" id="page-128">
  <div class="day-tag abs">단답비급 DAY 11</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">303.</div><hr class="q-hline">
      <p class="q-text">컴퓨터나 마이크로프로세서에 사용하기 위하여 무정전전원장치(UPS)를 구성하려고 한다. 다음 각 물음에 답하시오.</p>
            <!--IMG:p128_diag303-->
            <p class="ans-line">(1) 그림의 ①~④에 들어갈 기기 또는 명칭을 쓰고 그 역할에 대하여 간단히 설명하시오.</p>
            <table class="tbl">
              <tr><th>명칭</th><th>역할</th></tr>
              <tr><td><span class="ans">컨버터</span></td><td><span class="ans">교류</span>를 <span class="ans">직류</span>로 변환</td></tr>
              <tr><td><span class="ans">축전지</span></td><td>충전장치에 의해 변환된 <span class="ans">직류 전력</span>을 저장</td></tr>
              <tr><td><span class="ans">인버터</span></td><td><span class="ans">직류</span>를 사용 주파수의 <span class="ans">교류</span> 전압으로 변환</td></tr>
              <tr><td><span class="ans">동기절체 스위치</span></td><td>상용전원 <span class="ans">정전 시 인버터 회로</span>로 <span class="ans">절체</span>되어 부하에 <span class="ans">무정전</span>으로 <span class="ans">전력</span>을 <span class="ans">공급</span>하기 위한 장치</td></tr>
            </table>
            <p class="ans-line">(2) Bypass Transformer를 설치하여 회로를 구성하는 이유를 설명하시오.</p>
            <p class="ans-line">① 회로의 <span class="ans">절연</span></p>
            <p class="ans-line">② UPS나 축전지의 <span class="ans">점검 및 고장</span> 시에도 부하에 <span class="ans">정상적</span>으로 <span class="ans">전력</span>을 <span class="ans">공급</span>하기 위함</p>
    </div>
  </div>
  <div class="brand-l abs">128 • 전기치트키</div>
</div>

<!-- ===== p.129 304~305 ===== -->
<div class="page" id="page-129">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">304.</div><hr class="q-hline">
      <p class="q-text">전원장치인 UPS, CVCF, VVVF 장치에 대한 비교표를 다음과 같이 구성할 때 빈칸을 채우시오. 단, 출력전원에 대하여 가능은 ○, 불가능은 ×로 표시하시오.</p>
            <table class="tbl">
              <tr><th>구분</th><th>UPS</th><th>CVCF</th><th>VVVF</th></tr>
              <tr><td>우리말 명칭</td><td><span class="ans">무정전 전원공급장치</span></td><td><span class="ans">정전압 정주파수 장치</span></td><td><span class="ans">가변전압 가변주파수 장치</span></td></tr>
              <tr><td>주회로 방식</td><td><span class="ans">인버터</span></td><td><span class="ans">인버터</span></td><td><span class="ans">인버터</span></td></tr>
              <tr><td>컨버터 스위칭</td><td><span class="ans">위상 또는 제어</span></td><td><span class="ans">PWM 제어</span></td><td><span class="ans">위상 또는 제어</span></td></tr>
              <tr><td>인버터 스위칭</td><td><span class="ans">PWM 제어</span></td><td><span class="ans">PWM 제어</span></td><td><span class="ans">PWM 제어</span></td></tr>
              <tr><td>컨버터 디바이스</td><td><span class="ans">SCR</span></td><td><span class="ans">IGBT</span></td><td><span class="ans">SCR</span></td></tr>
              <tr><td>인버터 디바이스</td><td><span class="ans">IGBT</span></td><td><span class="ans">IGBT</span></td><td><span class="ans">IGBT</span></td></tr>
              <tr><td>무정전</td><td><span class="ans">○</span></td><td><span class="ans">×</span></td><td><span class="ans">×</span></td></tr>
              <tr><td>정전압 정주파수</td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">×</span></td></tr>
              <tr><td>가변전압 가변주파수</td><td><span class="ans">×</span></td><td><span class="ans">×</span></td><td><span class="ans">○</span></td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">305.</div><hr class="q-hline">
      <p class="q-text">전류형 인버터와 전압형 인버터의 회로상의 차이점을 2가지씩 쓰시오.</p>
            <table class="tbl">
              <tr><th>전류형 인버터</th><th>전압형 인버터</th></tr>
              <tr><td>1. <span class="ans">DC 측에 대용량 리액터(L)를 설치한다.</span></td><td>1. <span class="ans">DC 측에 대용량 콘덴서(C)를 설치한다.</span></td></tr>
              <tr><td>2. <span class="ans">인버터부에 SCR을 사용한다.</span></td><td>2. <span class="ans">전압 제어용으로 사용한다.</span></td></tr>
            </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 129</div>
</div>

<!-- ===== p.130 306~307 ===== -->
<div class="page" id="page-130">
  <div class="day-tag abs">단답비급 DAY 11</div>
  <div class="content">
    <div class="q">
      <div class="q-num">306.</div><hr class="q-hline">
      <p class="q-text">전류형 인버터와 전압형 인버터의 출력 파형 상의 차이점을 설명하시오.</p>
            <table class="tbl">
              <tr><th>구분</th><th>전압</th><th>전류</th></tr>
              <tr><td>전류형 인버터</td><td><span class="ans">정현파</span></td><td><span class="ans">구형파</span></td></tr>
              <tr><td>전압형 인버터</td><td><span class="ans">구형파</span></td><td><span class="ans">정현파</span></td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">307.</div><hr class="q-hline">
      <p class="q-text">사용 중인 UPS의 2차측에 단락사고 등이 발생했을 경우 UPS와 고장회로를 분리하는 방식 3가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">배선용 차단기</span>에 의한 보호</p>
            <p class="ans-line">② <span class="ans">속단퓨즈</span>에 의한 보호</p>
            <p class="ans-line">③ <span class="ans">반도체 차단기</span>에 의한 보호</p>
    </div>
  </div>
  <div class="brand-l abs">130 • 전기치트키</div>
</div>

<!-- ===== p.131 308~310 ===== -->
<div class="page" id="page-131">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">고장 및 사고</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">308.</div><hr class="q-hline">
      <p class="q-text">일반용 전기설비 및 자가용 전기설비에 있어서 과전류(과부하)의 종류 2가지와 각각에 대한 용어의 정의를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">과부하</span> 전류 : <span class="ans">전기적인 고장 없이 부하전류 증가로 인해 발생한</span> 과전류</p>
            <p class="ans-line">② <span class="ans">단락</span> 전류 : <span class="ans">정상 운전상태에서 전위차가 있는 충전된 도체 사이가 임피던스가 0인 고장에 기인한</span> 전류</p>
    </div>
    <div class="q">
      <div class="q-num">309.</div><hr class="q-hline">
      <p class="q-text">인체가 전기설비에 접촉되어 감전 재해가 발생하였을 때 감전 피해의 위험도를 결정하는 요인 4가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">통전전류의 크기</span> &nbsp; ② <span class="ans">통전시간</span> &nbsp; ③ <span class="ans">통전경로</span> &nbsp; ④ <span class="ans">전원의 종류</span></p>
    </div>
    <div class="q">
      <div class="q-num">310.</div><hr class="q-hline">
      <p class="q-text">다음은 인체에 전류가 흘러 감전된 정도를 설명한 것이다. ( ) 안에 알맞은 용어를 쓰시오.</p>
            <p class="ans-line">1. ( <span class="ans">감지</span> ) 전류</p>
            <p class="ans-line">2. ( <span class="ans">경련</span> ) 전류</p>
            <p class="ans-line">3. ( <span class="ans">심실세동</span> ) 전류</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 131</div>
</div>

<!-- ===== p.132 311~317 ===== -->
<div class="page" id="page-132">
  <div class="day-tag abs">단답비급 DAY 11</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">311.</div><hr class="q-hline">
      <p class="q-text">전기화재 발생원인 5가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">누전/지락</span> &nbsp; ② <span class="ans">접속불량에 의한 단락</span> &nbsp; ③ <span class="ans">절연열화에 의한 단락</span></p>
            <p class="ans-line">④ <span class="ans">압착손상에 의한 단락</span> &nbsp; ⑤ <span class="ans">과부하/과전류</span></p>
    </div>
    <div class="q">
      <div class="q-num">312.</div><hr class="q-hline">
      <p class="q-text">케이블의 트리현상이란 무엇인가 쓰고 종류 3가지를 쓰시오.</p>
            <p class="ans-line">트리현상 : <span class="ans">고체절연체 속에서 나뭇가지 모양의 방전흔적을 남기는 절연열화 현상</span></p>
            <p class="ans-line">종류 : <span class="ans">수트리, 전기적트리, 화학적트리</span></p>
    </div>
    <div class="q">
      <div class="q-num">313.</div><hr class="q-hline">
      <p class="q-text">변압기, 발전기, 모선 또는 이를 지지하는 애자는 어느 전류에 의하여 생기는 기계적 충격에 견디는 강도를 가져야 하는가?</p>
            <p class="ans-line"><span class="ans">단락전류</span></p>
    </div>
    <div class="q">
      <div class="q-num">314.</div><hr class="q-hline">
      <p class="q-text">단락전류를 계산하는 것은 주로 어떤 요소에 적용하고자 하는 것인지 그 적용 요소에 대하여 3가지만 설명하시오.</p>
            <p class="ans-line">① <span class="ans">차단기의 차단용량 결정</span> &nbsp; ② <span class="ans">보호 계전기의 정정</span> &nbsp; ③ <span class="ans">기기에 가해지는 전자력의 추정</span></p>
    </div>
    <div class="q">
      <div class="q-num">315.</div><hr class="q-hline">
      <p class="q-text">다음과 같은 사고종류에 대한 보호장치 및 보호조치를 작성하시오.</p>
            <table class="tbl">
              <tr><th>항목</th><th>사고종류</th><th>보호장치 및 보호조치</th></tr>
              <tr><td rowspan="3">고압 배전선로</td><td>접지사고</td><td><span class="ans">접지계전기</span></td></tr>
              <tr><td>과부하, 단락</td><td><span class="ans">과전류 계전기</span></td></tr>
              <tr><td>뇌해</td><td>피뢰기, 가공지선</td></tr>
              <tr><td>주상 변압기</td><td>과부하, 단락</td><td>고압 퓨즈</td></tr>
              <tr><td rowspan="2">저압 배전선로</td><td>고저압 혼촉</td><td><span class="ans">제2종 접지</span></td></tr>
              <tr><td>과부하, 단락</td><td>저압 퓨즈</td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">316.</div><hr class="q-hline">
      <p class="q-text">1선 지락 고장 시 접지계통별 고장전류의 경로를 답란에 쓰시오.</p>
            <table class="tbl">
              <tr><th>접지계통</th><th>고장전류 경로</th></tr>
              <tr><td>단일 접지계통</td><td><span class="ans">선로 → 고장점 → 대지 → 접지점 → 선로</span></td></tr>
              <tr><td>중성점 접지계통</td><td><span class="ans">선로 → 고장점 → 대지 → 중성점 → 선로</span></td></tr>
              <tr><td>다중 접지계통</td><td><span class="ans">선로 → 고장점 → 대지 → 다중 접지선과 병렬로 → 중성점 → 선로</span></td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">317.</div><hr class="q-hline">
      <p class="q-text">1선 지락사고 시 건전상의 대지 전위의 변화를 간단히 설명하시오.</p>
            <p class="ans-line">1선 지락사고 시 <span class="ans">건전상의 대지 전위</span>는 <span class="ans">상승</span>한다.</p>
    </div>
  </div>
  <div class="brand-l abs">132 • 전기치트키</div>
</div>

<!-- ===== p.133 memo ===== -->
<div class="page" id="page-133">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 133</div>
</div>

<!-- ===== p.134 ===== -->
<div class="page" id="page-134">
  <div class="brand abs">전기치트키</div>
  <div class="content"></div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 134</div>
</div>

<!-- ===== p.135 DAY 12 ===== -->
<div class="page" id="page-135">
  <div class="day-banner abs">DAY 12</div>
  <div class="topic-box abs">접지<br>절연</div>
</div>

<!-- ===== p.136 318~320 ===== -->
<div class="page" id="page-136">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">접지</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">318.</div><hr class="q-hline">
      <p class="q-text">접지공사의 목적을 3가지만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">누전에 의한 감전사고 방지</span></p>
            <p class="ans-line">② 이상전압 발생 시 <span class="ans">대지전위 상승</span>을 <span class="ans">억제</span>하여 기기 보호</p>
            <p class="ans-line">③ 지락사고 시 <span class="ans">보호계전기</span>의 <span class="ans">동작</span>을 <span class="ans">신속, 확실</span>하게 하기 위하여</p>
    </div>
    <div class="q">
      <div class="q-num">319.</div><hr class="q-hline">
      <p class="q-text">변압기 중성점 접지(계통접지)의 목적 3가지만 쓰시오.</p>
            <p class="ans-line">① 지락고장 시 <span class="ans">건전상의 대지전위 상승 억제</span></p>
            <p class="ans-line">② 뇌, 아크지락, 기타에 의한 <span class="ans">이상전압</span>의 <span class="ans">억제</span> 및 발생 방지</p>
            <p class="ans-line">③ 지락고장 시 접지 <span class="ans">계전기</span>의 <span class="ans">동작</span>을 <span class="ans">확실</span>하게 함</p>
    </div>
    <div class="q">
      <div class="q-num">320.</div><hr class="q-hline">
      <p class="q-text">아래 그림과 같이 시행한 계통접지와 기기접지의 기능을 설명하시오.</p>
            <table class="tbl">
              <tr><th>계통접지</th><th>기기접지</th></tr>
              <tr><td><!--IMG:p135_sys_gnd--></td><td><!--IMG:p135_eq_gnd--></td></tr>
              <tr><td><span class="ans">고압전로와 저압전로가 혼촉되었을 때 감전이나 화재방지</span></td><td><span class="ans">누전되고 있는 기기에 접촉 시 감전방지</span></td></tr>
            </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 136</div>
</div>

<!-- ===== p.137 321~324 ===== -->
<div class="page" id="page-137">
  <div class="day-tag abs">단답비급 DAY 12</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">321.</div><hr class="q-hline">
      <p class="q-text">접지저항의 결정요인인 접지저항 요소 3가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">접지도체와 접지전극 자체의 저항</span></p>
            <p class="ans-line">② <span class="ans">접지전극 표면과 토양 사이의 접촉저항</span></p>
            <p class="ans-line">③ <span class="ans">접지전극 주위 토양의 저항</span></p>
    </div>
    <div class="q">
      <div class="q-num">322.</div><hr class="q-hline">
      <p class="q-text">접지공사에서 접지저항을 저감시키는 방법을 5가지만 쓰시오.</p>
            <p><b>[물리적 방법]</b></p>
            <p class="ans-line">① <span class="ans">접지극을 깊게 한다.</span> &nbsp; ② <span class="ans">접지극을 병렬 접속한다.</span></p>
            <p class="ans-line">③ <span class="ans">심타공법</span>으로 시공한다. &nbsp; ④ <span class="ans">접지봉의 매설개수를 많게 한다.</span></p>
            <p><b>[화학적 방법]</b></p>
            <p class="ans-line">⑤ <span class="ans">접지저항 저감재</span>를 사용한다.</p>
    </div>
    <div class="q">
      <div class="q-num">323.</div><hr class="q-hline">
      <p class="q-text">대지 저항률을 낮추기 위한 저감재의 구비조건 4가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">환경에 무해하며, 안전</span>할 것</p>
            <p class="ans-line">② 전기적으로 <span class="ans">양도체</span>이고, <span class="ans">전극을 부식</span>시키지 않을 것</p>
            <p class="ans-line">③ <span class="ans">지속성</span>이 있을 것</p>
            <p class="ans-line">④ <span class="ans">작업성</span>이 좋을 것</p>
    </div>
    <div class="q">
      <div class="q-num">324.</div><hr class="q-hline">
      <p class="q-text">중성점 접지 저항기의 기능을 쓰시오.</p>
            <p class="ans-line"><span class="ans">지락사고 시 지락전류 억제 및 건전상 대지전위 상승 억제</span></p>
    </div>
  </div>
  <div class="brand-l abs">137 • 전기치트키</div>
</div>

<!-- ===== p.138 325~326 ===== -->
<div class="page" id="page-138">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">325.</div><hr class="q-hline">
      <p class="q-text">배전용 변전소의 접지 공사를 하고자 한다. 주요한 접지 개소를 5가지만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">옥외철구 및 제어반 외함 접지</span></p>
            <p class="ans-line">② <span class="ans">피뢰기 접지</span> &nbsp; ③ <span class="ans">피뢰침 접지</span></p>
            <p class="ans-line">④ <span class="ans">계기용 변성기 및 2차측 접지</span> &nbsp; ⑤ <span class="ans">변압기 중성점 접지</span></p>
    </div>
    <div class="q">
      <div class="q-num">326.</div><hr class="q-hline">
      <p class="q-text">중성점 직접 접지계통에 인접한 통신선의 전자유도 장해 경감에 관한 대책을 경제성이 높은 것부터 설명하시오.</p>
            <p class="ans-line">1. 근본 대책 : <span class="ans">전자유도 전압의 억제</span></p>
            <p><b>2. 전력선측 대책(5가지)</b></p>
            <p class="ans-line">① <span class="ans">송전선로를 통신선으로부터 멀리 떨어져 건설</span></p>
            <p class="ans-line">② <span class="ans">접지 장소를 적당히 선정해서 기유도 전류의 분포를 조절</span></p>
            <p class="ans-line">③ <span class="ans">고속도 지락보호 계전 방식을 채용</span></p>
            <p class="ans-line">④ <span class="ans">차폐선을 설치</span> &nbsp; ⑤ <span class="ans">지중전선로 방식을 채용</span></p>
            <p><b>3. 통신선측 대책(5가지)</b></p>
            <p class="ans-line">① <span class="ans">절연변압기를 설치하여 구간을 분리</span></p>
            <p class="ans-line">② <span class="ans">연피케이블 사용</span> &nbsp; ③ <span class="ans">통신선에 우수한 피뢰기 사용</span></p>
            <p class="ans-line">④ <span class="ans">배류코일 설치</span> &nbsp; ⑤ <span class="ans">전력선과 교차 시 직각 교차</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 138</div>
</div>

<!-- ===== p.139 327~328 ===== -->
<div class="page" id="page-139">
  <div class="day-tag abs">단답비급 DAY 12</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">327.</div><hr class="q-hline">
      <p class="q-text">비접지 3상 3선식 배전방식과 비교하여, 3상 4선식 다중접지(직접접지) 배전방식의 장점 및 단점을 각각 4가지씩 쓰시오.</p>
            <p><b>[장점]</b></p>
            <p class="ans-line">① 1선 <span class="ans">지락</span> 시 건전상의 <span class="ans">대지전위 상승</span>이 <span class="ans">낮다</span>.</p>
            <p class="ans-line">② <span class="ans">보호계전기</span>의 <span class="ans">동작</span>이 <span class="ans">확실</span>하다.</p>
            <p class="ans-line">③ 변압기 <span class="ans">단절연이 가능</span>하다.</p>
            <p class="ans-line">④ <span class="ans">피뢰기</span>의 <span class="ans">제한 전압</span>을 낮게 할 수 있다.</p>
            <p><b>[단점]</b></p>
            <p class="ans-line">① <span class="ans">지락전류가 크다</span>.</p>
            <p class="ans-line">② 통신선 <span class="ans">유도장해가 크다</span>.</p>
            <p class="ans-line">③ <span class="ans">지락전류</span>가 <span class="ans">저역률 대전류</span>이므로 <span class="ans">과도 안정도가 나빠진다</span>.</p>
            <p class="ans-line">④ <span class="ans">차단기</span>가 <span class="ans">빈번하게</span> <span class="ans">동작</span>하여 차단기 <span class="ans">수명이 단축</span>된다.</p>
    </div>
    <div class="q">
      <div class="q-num">328.</div><hr class="q-hline">
      <p class="q-text">독립접지와 비교하여 공통접지의 장점과 단점을 각각 3가지만 쓰시오.</p>
            <p><b>1. 공통접지의 장점</b></p>
            <p class="ans-line">① 접지극의 연접으로 <span class="ans">합성저항 감소</span></p>
            <p class="ans-line">② 접지극의 연접으로 <span class="ans">접지극 신뢰도 향상</span></p>
            <p class="ans-line">③ 접지극의 <span class="ans">수량 감소</span></p>
            <p><b>2. 공통접지의 단점</b></p>
            <p class="ans-line">① 계통 이상전압 발생 시 <span class="ans">파급영향이 크다</span>.</p>
            <p class="ans-line">② 다른 기기 계통으로부터 <span class="ans">노이즈 유입</span></p>
            <p class="ans-line">③ 피뢰침용과 공용이므로 <span class="ans">뇌서지</span>에 대한 <span class="ans">영향</span>을 받을 수 있다.</p>
    </div>
  </div>
  <div class="brand-l abs">139 • 전기치트키</div>
</div>

<!-- ===== p.140 329 ===== -->
<div class="page" id="page-140">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">329.</div><hr class="q-hline">
      <p class="q-text">그림을 보고 다음 각 물음에 답하시오.</p>
            <!--IMG:p139_line_gnd--> <!--IMG:p139_portable_gnd-->
            <p class="ans-line">1. 접지용구를 사용하여 접지를 하고자 할 때 접지 순서 및 접지 개소에 대하여 설명하시오.</p>
            <p class="ans-line">접지순서 : <span class="ans">대지에 먼저 연결</span>한 후 선로에 연결</p>
            <p class="ans-line">접지개소 : 선로측 A와 부하측 B <span class="ans">양측에 설치</span></p>
            <p class="ans-line">2. 부하측에서 휴전 작업을 할 때의 조작 순서를 설명하시오.</p>
            <p class="ans-line"><span class="ans">CB(OFF)</span> → <span class="ans">DS2(OFF)</span> → <span class="ans">DS1(OFF)</span></p>
            <p class="ans-line">3. 휴전 작업이 끝난 후 부하측에 전력을 공급하는 조작 순서를 설명하시오. 단, 접지되지 않은 상태에서 작업한다고 가정한다.</p>
            <p class="ans-line"><span class="ans">DS2(ON)</span> → <span class="ans">DS1(ON)</span> → <span class="ans">CB(ON)</span></p>
            <p class="ans-line">4. 긴급할 때 DS로 개폐 가능한 전류의 종류를 2가지만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">무부하 충전전류</span> &nbsp; ② <span class="ans">변압기 여자전류</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 140</div>
</div>

<!-- ===== p.141 330~332 ===== -->
<div class="page" id="page-141">
  <div class="day-tag abs">단답비급 DAY 12</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">330.</div><hr class="q-hline">
      <p class="q-text">피뢰기의 접지저항 값은 몇 [Ω] 이하로 하여야 하는가?</p>
            <p class="ans-line"><span class="ans">10[Ω]</span></p>
    </div>
    <div class="q">
      <div class="q-num">331.</div><hr class="q-hline">
      <p class="q-text">다음 그림에서 ①~⑤까지의 명칭을 쓰시오.</p>
            <!--IMG:p140_diag331-->
            <table class="tbl">
              <tr><th>①</th><th>②</th><th>③</th><th>④</th><th>⑤</th></tr>
              <tr><td><span class="ans">보호도체</span></td><td><span class="ans">주 등전위 본딩 도체</span></td><td><span class="ans">보조 등전위 본딩 도체</span></td><td><span class="ans">접지도체</span></td><td><span class="ans">접지극</span></td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">332.</div><hr class="q-hline">
      <p class="q-text">① ~ ③에 알맞은 보호도체의 최소 단면적의 기준을 각각 쓰시오.</p>
            <table class="tbl">
              <tr><th>선도체의 단면적 $S$ [mm², 구리]</th><th>보호도체의 최소 단면적 [mm², 구리]</th></tr>
              <tr><td>$S \leq 16$</td><td><span class="ans">$S$</span></td></tr>
              <tr><td>$16 &lt; S \leq 35$</td><td><span class="ans">16</span></td></tr>
              <tr><td>$35 &lt; S$</td><td><span class="ans">$S/2$</span></td></tr>
            </table>
    </div>
  </div>
  <div class="brand-l abs">141 • 전기치트키</div>
</div>

<!-- ===== p.142 333~335 ===== -->
<div class="page" id="page-142">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">333.</div><hr class="q-hline">
      <p class="q-text">보호도체의 종류를 2가지만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">다심케이블의 도체</span></p>
            <p class="ans-line">② <span class="ans">충전도체와 같은 외함에 수납된 절연도체 또는 나도체</span></p>
    </div>
    <div class="q">
      <div class="q-num">334.</div><hr class="q-hline">
      <p class="q-text">다음 등전위본딩에 관한 도체의 내용이다. 빈칸에 알맞은 값은?</p>
            <p class="ans-line">가. 구리도체 ( <span class="ans">6</span> ) [mm²]</p>
            <p class="ans-line">나. 알루미늄도체 ( <span class="ans">16</span> ) [mm²]</p>
            <p class="ans-line">다. 강철 도체 ( <span class="ans">50</span> ) [mm²]</p>
    </div>
    <div class="q">
      <div class="q-num">335.</div><hr class="q-hline">
      <p class="q-text">주 접지 단자에 접속하기 위한 보호본딩도체의 단면적은 구리도체 ( ) [mm²] 또는 다른 재질의 동등한 단면적을 초과할 필요는 없다.</p>
            <p class="ans-line">( <span class="ans">25</span> ) [mm²]</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 142</div>
</div>

<!-- ===== p.143 memo ===== -->
<div class="page" id="page-143">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 143</div>
</div>

<!-- ===== p.144 336~339 ===== -->
<div class="page" id="page-144">
  <div class="day-tag abs">단답비급 DAY 12</div>
  <div class="sec-title abs">절연</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">336.</div><hr class="q-hline">
      <p class="q-text">고압 및 특고압 전로의 절연내력 시험 방법에 대해 설명하시오.</p>
            <p class="ans-line"><span class="ans">시험전압을 충전부(전로)와 대지 사이에 연속하여 10분간 가하여 절연내력을 시험하였을 때 이에 견디어야 한다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">337.</div><hr class="q-hline">
      <p class="q-text">아래 표의 ( )에 알맞은 값을 쓰시오.</p>
            <table class="tbl">
              <tr><th>권선의 종류 (최대사용전압 기준)</th><th>시험전압</th></tr>
              <tr><td>최대 사용전압 7[kV] 이하 (500[V] 미만 시 500[V])</td><td>최대사용전압 × ( <span class="ans">1.5</span> )배</td></tr>
              <tr><td>7[kV] 초과 25[kV] 이하, 중성점 접지식</td><td>최대사용전압 × ( <span class="ans">0.92</span> )배</td></tr>
              <tr><td>7[kV] 초과 60[kV] 이하 (10500[V] 미만 시 10500[V])</td><td>최대사용전압 × ( <span class="ans">1.25</span> )배</td></tr>
              <tr><td>60[kV] 초과, 중성점 비접지식</td><td>최대사용전압 × ( <span class="ans">1.25</span> )배</td></tr>
              <tr><td>60[kV] 초과, 중성점 접지식+중성점 피뢰기 (75[kV] 미만 시 75[kV])</td><td>최대사용전압 × ( <span class="ans">1.1</span> )배</td></tr>
              <tr><td>60[kV] 초과, 중성점 직접 접지식 (170[kV] 초과 중성점 피뢰기)</td><td>최대사용전압 × ( <span class="ans">0.72</span> )배</td></tr>
              <tr><td>170[kV] 초과, 중성점 직접 접지</td><td>최대사용전압 × ( <span class="ans">0.64</span> )배</td></tr>
              <tr><td>기타의 권선</td><td>최대사용전압 × 1.1배</td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">338.</div><hr class="q-hline">
      <p class="q-text">전기사용 장소의 사용전압이 저압인 전로의 절연저항은 다음 표에서 정한 값 이상이어야 한다. 빈칸에 절연저항 값을 써넣으시오.</p>
            <table class="tbl">
              <tr><th>전로의 사용전압[V]</th><th>DC 시험 전압[V]</th><th>절연저항[MΩ]</th></tr>
              <tr><td>SELV 및 PELV</td><td>250</td><td><span class="ans">0.5</span></td></tr>
              <tr><td>FELV, 500[V] 이하</td><td>500</td><td><span class="ans">1.0</span></td></tr>
              <tr><td>500[V] 초과</td><td>1000</td><td><span class="ans">1.0</span></td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">339.</div><hr class="q-hline">
      <p class="q-text">전로의 사용전압이 350[V] 이상 400[V] 미만인 경우 절연저항 값은 몇 [MΩ] 이상이어야 하는가?</p>
            <p class="ans-line"><span class="ans">1[MΩ]</span> 이상</p>
    </div>
  </div>
  <div class="brand-l abs">144 • 전기치트키</div>
</div>

<!-- ===== p.145 DAY 13 ===== -->
<div class="page" id="page-145">
  <div class="day-banner abs">DAY 13</div>
  <div class="topic-box abs">측정<br>시퀀스</div>
</div>

<!-- ===== p.146 340~343 ===== -->
<div class="page" id="page-146">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">측정</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">340.</div><hr class="q-hline">
      <p class="q-text">지중 배전선로에서 사용하는 전력케이블의 고장점 측정을 위해 사용되는 방법을 3가지만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">머레이루프법</span> &nbsp; ② <span class="ans">펄스레이더법</span> &nbsp; ③ <span class="ans">정전용량법</span></p>
    </div>
    <div class="q">
      <div class="q-num">341.</div><hr class="q-hline">
      <p class="q-text">지중 케이블의 고장점 탐지법 3가지와 각각의 사용 용도를 쓰시오.</p>
            <table class="tbl">
              <tr><th>고장점 탐지법</th><th>사용용도</th></tr>
              <tr><td>머레이루프(Murray loop)법</td><td><span class="ans">지락사고, 단락사고</span></td></tr>
              <tr><td>펄스 레이더(Pulse radar)법</td><td><span class="ans">지락사고, 3상단락, 단선사고</span></td></tr>
              <tr><td>정전브리지(Capacity bridge)법</td><td><span class="ans">단선사고</span></td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">342.</div><hr class="q-hline">
      <p class="q-text">다음과 같은 저항을 측정하는 방법이나 측정계기를 쓰시오.</p>
            <p class="ans-line">1. 굵은 나전선의 저항 : <span class="ans">켈빈더블 브리지</span></p>
            <p class="ans-line">2. 수천옴의 가는 전선의 저항 : <span class="ans">휘스톤 브리지</span></p>
            <p class="ans-line">3. 전해액의 저항 : <span class="ans">콜라우시 브리지</span></p>
            <p class="ans-line">4. 옥내 전등선의 절연저항 : <span class="ans">메거</span></p>
    </div>
    <div class="q">
      <div class="q-num">343.</div><hr class="q-hline">
      <p class="q-text">접지저항을 측정하기 위하여 사용되는 측정방법 2가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">어스 테스터(접지저항 측정기)에 의한 접지저항 측정법</span></p>
            <p class="ans-line">② <span class="ans">콜라우시 브리지에 의한 3극 접지저항 측정법</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 146</div>
</div>

<!-- ===== p.147 344~345 ===== -->
<div class="page" id="page-147">
  <div class="day-tag abs">단답비급 DAY 13</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">344.</div><hr class="q-hline">
      <p class="q-text">다음은 지중케이블의 사고점 측정법과 절연의 건전도를 측정하는 방법을 열거한 것이다. 다음 방법들을 구분하여 답하시오.</p>
            <p class="ans-line">1. 사고점 측정법 : <span class="ans">④, ⑤, ⑥</span></p>
            <p class="ans-line">2. 절연 열화 측정법 : <span class="ans">①, ②, ③</span></p>
    </div>
    <div class="q">
      <div class="q-num">345.</div><hr class="q-hline">
      <p class="q-text">그림은 전위 강하법에 의한 접지저항 측정방법이다. E, P, C가 일직선상에 있을 때, 다음 물음에 답하시오. (단, E는 반지름 r인 반구모양 전극이다.)</p>
            <!--IMG:p146_fig1--> <!--IMG:p146_fig2-->
            <p class="ans-line">1. [그림1]과 [그림2]의 측정방법 중 접지저항 값이 참값에 가까운 측정방법은? <span class="ans">[그림1]</span></p>
            <p class="ans-line">2. P/C = 0.618의 조건을 만족할 때 측정값이 참값과 같아지므로 P극을 EC 간 거리의 <span class="ans">61.8[%]</span>에 시설하면 정확한 접지저항 값을 얻을 수 있다.</p>
    </div>
  </div>
  <div class="brand-l abs">147 • 전기치트키</div>
</div>

<!-- ===== p.148 346~348 ===== -->
<div class="page" id="page-148">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">346.</div><hr class="q-hline">
      <p class="q-text">4개의 측정탐침(4-Test Probe)을 지표면에 일직선 상에 등거리로 박아서 측정장비 내에서 저주파 전류를 탐침을 통해 대지에 흘려 보내어 대지저항률을 측정하는 방법을 무엇이라 하는가?</p>
            <p class="ans-line"><span class="ans">웨너 4전극법</span></p>
    </div>
    <div class="q">
      <div class="q-num">347.</div><hr class="q-hline">
      <p class="q-text">Wenner의 4전극법에 대한 공식을 쓰고, 원리도를 그려 설명하시오.</p>
            <!--IMG:p147_wenner-->
            <p class="formula">$\rho = 2\pi a R$ (단, $a$ : 전극간격 [m], $R$ : 접지저항 [Ω])</p>
            <p class="ans-line"><span class="ans">4개의 측정 전극을 지표면에 일직선상, 일정한 간격으로 매설하고, 측정 장비 내에서 저주파 전류를 C1, C2 전극을 통해 대지에 흘려보낸 후 P1, P2 사이의 전압을 측정하여 대지저항률을 구하는 방법이다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">348.</div><hr class="q-hline">
      <p class="q-text">수전용 차단기와 과전류계전기 연동시험 시 시험전류를 가하기 전에 점검하여야 할 사항을 3가지만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">정전의 확인</span></p>
            <p class="ans-line">② <span class="ans">시험회로에 접지가 된 부분이 없는지 확인</span></p>
            <p class="ans-line">③ <span class="ans">시험용 배선의 접속상태 확인</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 148</div>
</div>

<!-- ===== p.149 349~350 ===== -->
<div class="page" id="page-149">
  <div class="day-tag abs">단답비급 DAY 13</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">349.</div><hr class="q-hline">
      <p class="q-text">과전류계전기와 수전용 차단기 연동시험 시 시험전류를 가하기 전에 준비하여야 하는 기기 3가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">물저항기</span> &nbsp; ② <span class="ans">전류계</span> &nbsp; ③ <span class="ans">사이클 카운터</span></p>
    </div>
    <div class="q">
      <div class="q-num">350.</div><hr class="q-hline">
      <p class="q-text">다음 그림은 전자식 접지 저항계를 사용하여 접지극의 접지저항을 측정하기 위한 배치도이다. 물음에 답하시오.</p>
            <!--IMG:p148_earth_tester-->
            <p class="ans-line">1. 보조 접지극을 설치하는 이유는? <span class="ans">전압과 전류를 공급하여 접지저항을 측정하기 위함</span></p>
            <p class="ans-line">2. ⑤와 ⑥의 설치 간격은? <span class="ans">⑤ 10[m], ⑥ 20[m]</span></p>
            <p class="ans-line">3. ①의 측정단자 접속은? <span class="ans">ⓐ→ⓓ, ⓑ→ⓔ, ⓒ→ⓕ</span></p>
            <p class="ans-line">4. 접지극의 매설 깊이는? <span class="ans">0.75[m] 이상</span></p>
    </div>
  </div>
  <div class="brand-l abs">149 • 전기치트키</div>
</div>

<!-- ===== p.150 351~353 ===== -->
<div class="page" id="page-150">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">시퀀스</div>
  <div class="content">
    <div class="q">
      <div class="q-num">351.</div><hr class="q-hline">
      <p class="q-text">THR의 명칭과 역할을 간단히 설명하시오.</p>
            <p class="ans-line">[명칭] <span class="ans">열동계전기</span></p>
            <p class="ans-line">[역할] 전동기 과부하 시 <span class="ans">동작</span>하여 전동기 <span class="ans">보호</span></p>
    </div>
    <div class="q">
      <div class="q-num">352.</div><hr class="q-hline">
      <p class="q-text">EOCR의 명칭과 사용목적을 쓰시오.</p>
            <p class="ans-line">[명칭] <span class="ans">전자식 과전류계전기</span></p>
            <p class="ans-line">[목적] 과전류가 흐르면 EOCR이 <span class="ans">동작</span>하여 전자접촉기를 소자시켜 전동기를 <span class="ans">보호</span>한다.</p>
    </div>
    <div class="q">
      <div class="q-num">353.</div><hr class="q-hline">
      <p class="q-text"><!--IMG:p149_timed_contact--> 의 접점 명칭을 쓰시오.</p>
            <p class="ans-line"><span class="ans">한시동작 순시복귀 a접점</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 150</div>
</div>

<!-- ===== p.151 355 ===== -->
<div class="page" id="page-151">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">355.</div><hr class="q-hline">
      <p class="q-text">릴레이 시퀀스와 무접점 시퀀스에 사용되는 전자릴레이와 무접점 릴레이를 비교할 때 전자릴레이의 장·단점을 5가지씩만 쓰시오.</p>
            <p><b>[장점]</b></p>
            <p class="ans-line">① <span class="ans">과부하 내량</span>이 크다. &nbsp; ② <span class="ans">온도 특성</span>이 좋다.</p>
            <p class="ans-line">③ 전기적 <span class="ans">잡음 없이 입·출력을 분리</span>할 수 있다. &nbsp; ④ 가격이 <span class="ans">저렴</span>하다.</p>
            <p class="ans-line">⑤ 부하가 큰 <span class="ans">전력을 인출</span>할 수 있다.</p>
            <p><b>[단점]</b></p>
            <p class="ans-line">① <span class="ans">소비 전력</span>이 크다. &nbsp; ② <span class="ans">소형화</span>에 한계가 있다. &nbsp; ③ <span class="ans">응답속도</span>가 느리다.</p>
            <p class="ans-line">④ 가동 <span class="ans">접촉부 수명</span>이 짧다. &nbsp; ⑤ <span class="ans">충격</span>에 약하다.</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 151</div>
</div>

<!-- ===== p.152 memo ===== -->
<div class="page" id="page-152">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 152</div>
</div>

<!-- ===== p.153 DAY 14 ===== -->
<div class="page" id="page-153">
  <div class="day-banner abs">DAY 14</div>
  <div class="topic-box abs">정의 및 용어·규정<br>옥내 기구 기호</div>
</div>

<!-- ===== p.154 354 ===== -->
<div class="page" id="page-154">
  <div class="day-tag abs">단답비급 DAY 14</div>
  <div class="content">
    <div class="q">
      <div class="q-num">354.</div><hr class="q-hline">
      <p class="q-text">그림은 타이머 내부 결선도이다. *표의 점선 부분에 대한 접점의 동작을 설명하시오.</p>
            <!--IMG:p153_relay8-->
            <p class="ans-line"><span class="ans">한시동작 순시복귀 a, b 접점</span>으로 타이머가 <span class="ans">여자</span>된 후 <span class="ans">설정 시간</span> 후에 동작되며, <span class="ans">소자</span>되면 즉시 <span class="ans">복귀</span>된다.</p>
    </div>
  </div>
  <div class="brand-l abs">154 • 전기치트키</div>
</div>

<!-- ===== p.155 356~357 ===== -->
<div class="page" id="page-155">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">정의 및 용어 · 규정</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">356.</div><hr class="q-hline">
      <p class="q-text">다음 주어진 전기 용어를 간단히 설명하시오.</p>
            <p class="ans-line">1. 뱅크(Bank) : <span class="ans">전로에 접속된 변압기 또는 콘덴서의 결선상 단위</span></p>
            <p class="ans-line">2. 수구(受口) : <span class="ans">소켓, 리셉터클, 콘센트 등의 총칭</span></p>
            <p class="ans-line">3. 한류퓨즈(Fuse) : <span class="ans">단락전류를 신속히 차단하며 또한 흐르는 단락전류의 값을 제한하는 성질을 가지는 퓨즈</span></p>
            <p class="ans-line">4. 접촉전압 : <span class="ans">사람이나 동물 등이 도전부에 접촉할 경우 작용하는 전압</span></p>
            <p class="ans-line">5. 중성선(中性線) : <span class="ans">다선식전로에서 전원의 중성극에 접속된 전선</span></p>
            <p class="ans-line">6. 분기회로(分歧回路) : <span class="ans">간선에서 분기하여 분기 과전류차단기를 거쳐서 부하에 이르는 사이의 배선</span></p>
            <p class="ans-line">7. 등전위본딩 : <span class="ans">등전위를 형성하기 위해 도전부 상호 간을 전기적으로 연결하는 것</span></p>
    </div>
    <div class="q">
      <div class="q-num">357.</div><hr class="q-hline">
      <p class="q-text">L1상, L2상, L3상, N상, 보호도체 ( )안에 알맞은 색을 쓰시오. (단, 상별 색이 1가지 이상인 경우 해당 색을 모두 쓰시오.)</p>
            <table class="tbl">
              <tr><th>상(문자)</th><th>L1</th><th>L2</th><th>L3</th><th>N</th><th>보호도체</th></tr>
              <tr><td>색상</td><td><span class="ans">갈색</span></td><td><span class="ans">검정색</span></td><td><span class="ans">회색</span></td><td><span class="ans">청색</span></td><td><span class="ans">녹색-노란색</span></td></tr>
            </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 155</div>
</div>

<!-- ===== p.156 358~359 ===== -->
<div class="page" id="page-156">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">358.</div><hr class="q-hline">
      <p class="q-text">한국전기설비규정에 따라 과전류차단기를 시설하지 않아도 되는 개소 3가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">접지공사의 접지도체</span></p>
            <p class="ans-line">② <span class="ans">다선식 전로의 중성선</span></p>
            <p class="ans-line">③ <span class="ans">전로의 일부에 접지공사를 한 저압 가공전선로의 접지측 전선</span></p>
    </div>
    <div class="q">
      <div class="q-num">359.</div><hr class="q-hline">
      <p class="q-text">한국전기설비규정에서 규정하는 용어의 정의를 쓰시오.</p>
            <p class="ans-line">1. PEM 도체 : <span class="ans">직류회로에서 중간도체 겸용 보호도체</span></p>
            <p class="ans-line">2. PEL 도체 : <span class="ans">직류회로에서 선도체 겸용 보호도체</span></p>
            <p class="ans-line">3. PEN 도체 : <span class="ans">교류회로에서 중성선 겸용 보호도체</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 156</div>
</div>

<!-- ===== p.157 360~361 ===== -->
<div class="page" id="page-157">
  <div class="day-tag abs">단답비급 DAY 14</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">360.</div><hr class="q-hline">
      <p class="q-text">접지도체, 보호접지, 접지시스템 중 다음 설명에 알맞게 빈칸에 작성하시오.</p>
            <table class="tbl">
              <tr><td>① ( <span class="ans">접지도체</span> )</td><td>계통, 설비 또는 기기의 한 점과 접지극 사이의 도전성 경로 또는 그 경로의 일부가 되는 도체</td></tr>
              <tr><td>② ( <span class="ans">보호접지</span> )</td><td>고장 시 감전에 대한 보호를 목적으로 기기의 한 점 또는 여러 점을 접지하는 것</td></tr>
              <tr><td>③ ( <span class="ans">접지시스템</span> )</td><td>기기나 계통을 개별적 또는 공통으로 접지하기 위하여 필요한 접속 및 장치로 구성된 설비</td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">361.</div><hr class="q-hline">
      <p class="q-text">한국전기설비규정 KEC에 따른 과전류 보호에 대한 설명으로 알맞은 내용을 쓰시오.</p>
            <p class="ans-line">중성선을 ( <span class="ans">차단</span> ) 및 ( <span class="ans">투입</span> )하는 회로의 경우에 설치하는 개폐기 및 차단기는 ( <span class="ans">차단</span> ) 시에는 중성선이 선도체보다 늦게 ( <span class="ans">차단</span> )되어야 하며, ( <span class="ans">투입</span> ) 시에는 선도체와 동시 또는 그 이전에 ( <span class="ans">투입</span> )되어야 한다.</p>
    </div>
  </div>
  <div class="brand-l abs">157 • 전기치트키</div>
</div>

<!-- ===== p.158 362~364 ===== -->
<div class="page" id="page-158">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">362.</div><hr class="q-hline">
      <p class="q-text">한국전기설비규정에 의거하여 저압전로에 사용하는 주택용 배선차단기의 과전류 트립동작시간 및 순시트립에 따른 구분을 나타낸 표이다. 표에 알맞은 말을 쓰시오.</p>
            <table class="tbl">
              <tr><th>차단기유형</th><th>순시트립 범위</th></tr>
              <tr><td>( <span class="ans">B</span> )</td><td>3$I_n$초과 ~ 5$I_n$이하</td></tr>
              <tr><td>( <span class="ans">C</span> )</td><td>5$I_n$초과 ~ 10$I_n$이하</td></tr>
              <tr><td>( <span class="ans">D</span> )</td><td>10$I_n$초과 ~ 20$I_n$이하</td></tr>
            </table>
            <table class="tbl">
              <tr><th>정격전류</th><th>시간</th><th>부동작 전류</th><th>동작전류</th></tr>
              <tr><td>63[A] 이하</td><td>60분</td><td>( <span class="ans">1.13</span> )배</td><td>( <span class="ans">1.45</span> )배</td></tr>
              <tr><td>63[A] 초과</td><td>120분</td><td>( <span class="ans">1.13</span> )배</td><td>( <span class="ans">1.45</span> )배</td></tr>
            </table>
    </div>
    <div class="q">
      <div class="q-num">363.</div><hr class="q-hline">
      <p class="q-text">고압용의 개폐기, 차단기, 피뢰기 기타 이와 유사한 기구로서 동작 시에 아크가 생기는 것은 목재의 벽 또는 천장 기타의 가연성 물체로부터 몇 [m] 이상 떼어 놓아야 하는가?</p>
            <p class="ans-line"><span class="ans">1[m]</span></p>
    </div>
    <div class="q">
      <div class="q-num">364.</div><hr class="q-hline">
      <p class="q-text">다음 빈칸에 알맞은 내용을 쓰시오.</p>
            <div class="box">
            <p>변전소(이에 준하는 곳으로서 ( <span class="ans">50</span> )[kV]를 초과하는 특고압의 전기를 변성하기 위한 것을 포함한다)의 운전에 필요한 지식 및 기능을 가진 자(이하 "기술원"이라 한다)가 그 변전소에 상주하여 감시를 하지 아니하는 변전소는 다음에 따라 시설하는 경우에 한한다.</p>
            <p>가. 사용전압은 ( <span class="ans">170</span> )[kV]이하의 변압기를 시설하는 변전소로서 기술원이 수시로 순회하거나 그 변전소를 원격감시제어하는 제어소에서 상시 감시하는 경우</p>
            </div>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 158</div>
</div>

<!-- ===== p.159 365~366 ===== -->
<div class="page" id="page-159">
  <div class="day-tag abs">단답비급 DAY 14</div>
  <div class="sec-title abs">옥내 기구 기호</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">365.</div><hr class="q-hline">
      <p class="q-text">[참고] 점멸기의 그림기호 : <!--IMG:sym_sw--></p>
            <p class="ans-line">(1) 용량 몇 [A] 이상은 전류치를 병기하는가? <span class="ans">15[A]</span></p>
            <p class="ans-line">(2) ① <!--IMG:sym_2p--> 과 ② <!--IMG:sym_4w--> : ① <span class="ans">2극 스위치</span> &nbsp; ② <span class="ans">4로 스위치</span></p>
            <p class="ans-line">(3) ① 방수형 <span class="ans">WP</span> &nbsp; ② 방폭형 <span class="ans">EX</span></p>
    </div>
    <div class="q">
      <div class="q-num">366.</div><hr class="q-hline">
      <p class="q-text">등·HID·콘센트 기호</p>
            <p class="ans-line">(1) <!--IMG:sym_outdoor--> : <span class="ans">옥외등</span></p>
            <p class="ans-line">(2) HID등 : ① <!--IMG:sym_h400-->400 <span class="ans">400[W] 수은등</span> &nbsp; ② <!--IMG:sym_m400-->400 <span class="ans">400[W] 메탈 헬라이드등</span> &nbsp; ③ <!--IMG:sym_n400-->400 <span class="ans">400[W] 나트륨등</span></p>
            <p class="ans-line">(3) 콘센트 기호 <!--IMG:sym_outlet--> : ① 천장 <!--IMG:sym_ceiling--> &nbsp; ② 바닥 <!--IMG:sym_floor--></p>
            <p class="ans-line">(4) ① <!--IMG:sym_2gang--> <span class="ans">2구 콘센트</span> &nbsp; ② <!--IMG:sym_3p_out--> <span class="ans">3극 콘센트</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 159</div>
</div>

<!-- ===== p.160 367~369 ===== -->
<div class="page" id="page-160">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">367.</div><hr class="q-hline">
      <p class="q-text">옥내배선 콘센트 기호</p>
            <table class="tbl sym-table outlet-syms">
              <tr><td>(1) <!--IMG:sym_lk--></td><td>(2) <!--IMG:sym_et--></td></tr>
              <tr><td>(3) <!--IMG:sym_el--></td><td>(4) <!--IMG:sym_e_outlet--></td></tr>
              <tr><td>(5) <!--IMG:sym_t_outlet--></td><td>(6) <!--IMG:sym_wp--></td></tr>
              <tr><td>(7) <!--IMG:sym_h_outlet--></td><td></td></tr>
            </table>
            <p class="ans-line">(1) LK <span class="ans">빠짐방지형</span> &nbsp; (2) ET <span class="ans">접지 단자붙이</span> &nbsp; (3) EL <span class="ans">누전차단기 붙이</span></p>
            <p class="ans-line">(4) E <span class="ans">접지극 붙이</span> &nbsp; (5) T <span class="ans">걸림형</span> &nbsp; (6) WP <span class="ans">방수형 콘센트</span> &nbsp; (7) H <span class="ans">의료용 콘센트</span></p>
    </div>
    <div class="q">
      <div class="q-num">368.</div><hr class="q-hline">
      <p class="q-text">개폐기 중에서 다음 기호(심벌)가 의미하는 것은 무엇인지 모두 쓰시오.</p>
            <!--IMG:sym_switch_368-->
            <p class="ans-line">① 3P 50[A] : <span class="ans">3극 50[A] 개폐기</span></p>
            <p class="ans-line">② f20[A] : <span class="ans">퓨즈 정격 20[A]</span></p>
            <p class="ans-line">③ A5 : <span class="ans">정격전류 5[A]인 전류계 붙이</span></p>
    </div>
    <div class="q">
      <div class="q-num">369.</div><hr class="q-hline">
      <p class="q-text">다음 심벌의 명칭을 쓰시오.</p>
            <table class="tbl sym-table duct-row">
              <tr>
                <td><!--IMG:sym_md--></td>
                <td><!--IMG:sym_ld--></td>
                <td><!--IMG:sym_f7--></td>
              </tr>
            </table>
            <p class="ans-line">MD <span class="ans">금속덕트</span> &nbsp; LD <span class="ans">라이팅 덕트</span> &nbsp; (F7) <span class="ans">플로어 덕트</span></p>
    </div>
  </div>
  <div class="brand-l abs">160 • 전기치트키</div>
</div>

<!-- ===== p.161 370~371 ===== -->
<div class="page" id="page-161">
  <div class="day-tag abs">단답비급 DAY 14</div>
  <div class="content">
    <div class="q">
      <div class="q-num">370.</div><hr class="q-hline">
      <p class="q-text">각 그림 기호의 명칭을 쓰시오.</p>
            <table class="tbl sym-table breaker-syms">
              <tr><th>(1)</th><th>(2)</th><th>(3)</th><th>(4)</th><th>(5)</th></tr>
              <tr>
                <td><!--IMG:sym_breaker_e--></td>
                <td><!--IMG:sym_breaker_b--></td>
                <td><!--IMG:sym_breaker_ec--></td>
                <td><!--IMG:sym_breaker_s--></td>
                <td><!--IMG:sym_breaker_g--></td>
              </tr>
            </table>
            <p class="ans-line">(1) E <span class="ans">누전차단기</span> &nbsp; (2) B <span class="ans">배선차단기</span> &nbsp; (3) EC <span class="ans">접지센터</span> &nbsp; (4) S <span class="ans">개폐기</span> &nbsp; (5) G <span class="ans">누전경보기</span></p>
    </div>
    <div class="q">
      <div class="q-num">371.</div><hr class="q-hline">
      <p class="q-text">다음과 같은 소형 변압기 심벌의 명칭을 쓰시오.</p>
            <div class="sym-grid tr-syms">
              <!--IMG:sym_tr_tb--> <!--IMG:sym_tr_tr-->
              <!--IMG:sym_tr_tn--> <!--IMG:sym_tr_tf-->
              <!--IMG:sym_tr_th-->
            </div>
            <p class="ans-line">TB <span class="ans">벨 변압기</span> &nbsp; TR <span class="ans">리모컨 변압기</span> &nbsp; TN <span class="ans">네온 변압기</span></p>
            <p class="ans-line">TF <span class="ans">형광등용 안정기</span> &nbsp; TH <span class="ans">HID램프용(고휘도 방전등용) 안정기</span></p>
    </div>
  </div>
  <div class="brand-l abs">161 • 전기치트키</div>
</div>

<!-- ===== p.162 memo ===== -->
<div class="page" id="page-162">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 162</div>
</div>

<!-- ===== p.163 372~374 ===== -->
<div class="page" id="page-163">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">부록) 감리</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">372.</div><hr class="q-hline">
      <p class="q-text">공사시방서란 무엇인지 설명하시오.</p>
            <p class="ans-line"><span class="ans">시공 과정에서 요구되는 기술적인 사항을 설명한 문서. 사용할 재료의 품질, 작업 순서, 마무리 정도 등 도면에 기재하기 곤란한 기술적 사항을 구체적으로 적는다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">373.</div><hr class="q-hline">
      <p class="q-text">감리원은 공사 완료 후 준공검사 전에 사전 시운전 등이 필요한 부분에 대하여는 공사업자에게 시운전을 위한 계획을 수립하여 시운전에 입회할 수 있다. 이에 따른 <strong>시운전 완료 후 성과물</strong>을 공사업자로부터 제출받아 검토한 후 <strong>발주자에게 인계하여야 할 사항(서류 등)을 5가지</strong>만 쓰시오.</p>
            <p class="ans-line">① <span class="ans">운전개시, 가동절차 및 방법</span></p>
            <p class="ans-line">② <span class="ans">점검항목 점검표</span></p>
            <p class="ans-line">③ <span class="ans">운전지침</span></p>
            <p class="ans-line">④ <span class="ans">기기류 단독 시운전 방법 검토 및 계획서</span></p>
            <p class="ans-line">⑤ <span class="ans">실가동 Diagram</span></p>
    </div>
    <div class="q">
      <div class="q-num">374.</div><hr class="q-hline">
      <p class="q-text">안전관리 결과 보고서에 포함되어야 하는 서류 5가지를 쓰시오.</p>
            <p class="ans-line">① <span class="ans">안전관리 조직표</span></p>
            <p class="ans-line">② <span class="ans">안전보건 관리체제</span></p>
            <p class="ans-line">③ <span class="ans">재해발생 현황</span></p>
            <p class="ans-line">④ <span class="ans">산재요양신청서 사본</span></p>
            <p class="ans-line">⑤ <span class="ans">안전교육 실적표</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 163</div>
</div>

"""
