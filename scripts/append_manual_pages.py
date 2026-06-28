#!/usr/bin/env python3
"""Append transcribed pages to dandap_manual.html (before closing scripts)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"

PAGES_38_43 = r"""
<!-- ===== p.38 070~073 ===== -->
<div class="page" id="page-038">
  <div class="day-tag abs">단답비급 DAY 4</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">070.</div><hr class="q-hline">
      <p class="q-text">조명설계 시 사용되는 용어 중 감광보상률이란 무엇을 의미하는지 설명하시오.</p>
      <p class="ans-line"><span class="ans">조명설계를 할 때 광속의 감소를 미리 예상하여 소요 광속에 여유를 두는 정도</span></p>
    </div>
    <div class="q">
      <div class="q-num">071.</div><hr class="q-hline">
      <p class="q-text">조명기구에서 기구 배광에 따른 조명방식의 종류 5가지를 쓰시오.</p>
      <p class="ans-line"><span class="ans">직접조명, 반직접조명, 전반확산조명, 반간접조명, 간접조명</span></p>
    </div>
    <div class="q">
      <div class="q-num">072.</div><hr class="q-hline">
      <p class="q-text">설계자가 크기, 형상 등 전체적인 조화를 생각하여 형광등 기구를 벽면 상방 모서리에 숨겨서 설치하는 방식으로 기구로부터의 빛이 직접 벽면을 조명하는 건축화 조명을 무슨 조명이라 하는가?</p>
      <p class="ans-line"><span class="ans">코니스 조명</span></p>
    </div>
    <div class="q">
      <div class="q-num">073.</div><hr class="q-hline">
      <p class="q-text">적외선 전구에 대한 다음 각 물음에 답하시오.</p>
      <p class="ans-line">(1) 주로 어떤 용도에 사용되는가? <span class="ans">표면 가열</span></p>
      <p class="ans-line">(2) 주로 몇 [W] 정도의 크기로 사용되는가? <span class="ans">250[W]</span></p>
      <p class="ans-line">(3) 효율은 몇 [%] 정도 되는가? <span class="ans">75[%]</span></p>
      <p class="ans-line">(4) 필라멘트의 온도는 절대온도로 몇 [°K] 정도 되는가? <span class="ans">2500[°K]</span></p>
      <p class="ans-line">(5) 적외선 전구에서 가장 많이 나오는 빛의 파장은 몇 [μm]인가? <span class="ans">1~3[μm]</span></p>
    </div>
  </div>
  <div class="brand-l abs">38 • 전기치트키</div>
</div>

<!-- ===== p.39 074~076 ===== -->
<div class="page" id="page-039">
  <div class="brand abs">전기치트키</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">074.</div><hr class="q-hline">
      <p class="q-text">HID Lamp에 대한 다음 각 물음에 답하시오.</p>
      <p class="ans-line">1. 이 램프는 어떠한 램프를 말하는가? <span class="ans">고휘도 방전램프</span></p>
      <p class="ans-line">2. 가장 많이 사용되는 등기구의 종류를 3가지만 쓰시오.</p>
      <p class="ans-line" style="margin-left:12px;">① <span class="ans">고압 수은등</span> &nbsp; ② <span class="ans">고압 나트륨등</span> &nbsp; ③ <span class="ans">메탈 핼라이드 램프</span></p>
    </div>
    <div class="q">
      <div class="q-num">075.</div><hr class="q-hline">
      <p class="q-text">기존 형광램프는 관형이 32[mm], 28[mm], 25.5[mm]가 있는데 T-5램프는 15.5[mm]로 작아진 최신형 세관형 램프를 말한다. 이 램프의 특징 5가지를 서술하시오.</p>
      <div class="formula-row" style="font-size:9.5pt;">
        <span>① <span class="ans">연색성 우수</span></span>
        <span>② <span class="ans">광속 유지율 우수</span></span>
        <span>③ <span class="ans">낮은 전력소모</span></span>
        <span>④ <span class="ans">적은 열발생</span></span>
        <span>⑤ <span class="ans">긴 수명</span></span>
        <span>⑥ <span class="ans">환경친화적</span></span>
      </div>
    </div>
    <div class="q">
      <div class="q-num">076.</div><hr class="q-hline">
      <p class="q-text">일반적으로 사용되고 있는 열음극 형광등과 비교하여 슬림라인(Slim line) 형광등의 장점 5가지와 단점 3가지를 쓰시오.</p>
      <p><b>[장점]</b></p>
      <p class="ans-line">① 양광주가 길고 <span class="ans">효율이 좋다.</span></p>
      <p class="ans-line">② <span class="ans">순시기동</span>으로 점등이 빠르다.</p>
      <p class="ans-line">③ 점등관등 <span class="ans">기동장치가 불필요</span>하다.</p>
      <p class="ans-line">④ 점등 불량으로 인한 <span class="ans">고장이 없다.</span></p>
      <p class="ans-line">⑤ 전압 변동에 의한 <span class="ans">수명의 단축이 없다.</span></p>
      <p style="margin-top:4px;"><b>[단점]</b></p>
      <p class="ans-line">① 전압이 높아 <span class="ans">위험하다.</span></p>
      <p class="ans-line">② 점등 장치가 <span class="ans">비싸다.</span></p>
      <p class="ans-line">③ 기동 시 <span class="ans">음극이 손상</span>되기 쉽다.</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 39</div>
</div>

<!-- ===== p.40 077~079 ===== -->
<div class="page" id="page-040">
  <div class="day-tag abs">단답비급 DAY 4</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">077.</div><hr class="q-hline">
      <p class="q-text">조명 설비의 깜박임 현상을 줄일 수 있는 조치는 다음의 경우 어떻게 하여야 하는가?</p>
      <p class="ans-line">1. 백열전등의 경우 : <span class="ans">직류</span>를 사용하여 점등한다.</p>
      <p class="ans-line">2. 3상 전원인 경우 : 전체 램프를 <span class="ans">$\frac{1}{3}$씩 3군</span>으로 나눠 각 군의 <span class="ans">위상</span>이 <span class="ans">$120°$</span>가 되도록 접속하고 개개의 빛을 혼합한다.</p>
      <p class="ans-line">3. 전구가 2개씩인 방전등 기구 : 2등용으로 하나는 <span class="ans">콘덴서</span>, 다른 하나는 <span class="ans">코일</span>을 설치하여 <span class="ans">위상차</span>를 발생시켜 점등한다.</p>
    </div>
    <div class="q">
      <div class="q-num">078.</div><hr class="q-hline">
      <p class="q-text">조명설비에서 전력을 절약하는 효율적인 방법에 대해 8가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">고효율</span> 등기구 채용</p>
      <p class="ans-line">② <span class="ans">고역률</span> 등기구 채용</p>
      <p class="ans-line">③ <span class="ans">고조도 저휘도 반사갓</span> 채용</p>
      <p class="ans-line">④ 적절한 <span class="ans">조광제어</span> 실시</p>
      <p class="ans-line">⑤ 등기구의 적절한 <span class="ans">보수 및 유지관리</span></p>
      <p class="ans-line">⑥ <span class="ans">재실감지기</span> 채용</p>
      <p class="ans-line">⑦ 창측 조명기구 <span class="ans">개별 점등</span></p>
      <p class="ans-line">⑧ 등기구의 <span class="ans">격등 제어</span></p>
    </div>
    <div class="q">
      <div class="q-num">079.</div><hr class="q-hline">
      <p class="q-text">양호한 전반조명이라면 등간격은 등 높이의 몇 배 이하로 해야 하는가?</p>
      <p class="ans-line"><span class="ans">1.5배</span></p>
    </div>
  </div>
  <div class="brand-l abs">40 • 전기치트키</div>
</div>

<!-- ===== p.41 080~082 ===== -->
<div class="page" id="page-041">
  <div class="brand abs">전기치트키</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">080.</div><hr class="q-hline">
      <p class="q-text">도로 조명설계에 있어 성능상 고려해야 할 중요 사항 5가지만 쓰시오.</p>
      <p class="ans-line">1. 높은 <span class="ans">조도</span>로 <span class="ans">충분히 밝게</span> 조명할 수 있을 것</p>
      <p class="ans-line">2. <span class="ans">균일</span>한 <span class="ans">노면휘도</span>를 확보할 것</p>
      <p class="ans-line">3. 조명기구 등의 Glare(눈부심)가 <span class="ans">적을</span> 것</p>
      <p class="ans-line">4. <span class="ans">유도성</span></p>
      <p class="ans-line">5. <span class="ans">조명방법</span></p>
    </div>
    <div class="q">
      <div class="q-num">081.</div><hr class="q-hline">
      <p class="q-text">아래 조명의 명칭에 따른 기호를 그리시오.</p>
      <img src="../assets/images/manual/crops/p041_tbl081.png" style="width:100%;max-height:280px;object-fit:contain;margin:6px 0;" alt="조명 기호 표">
    </div>
    <div class="q">
      <div class="q-num">082.</div><hr class="q-hline">
      <p class="q-text">주파수 60[Hz]에 사용하는 형광방전등을 50[Hz]에서 사용한다면 광속과 점등시간은 어떻게 변화되는지를 설명하시오.</p>
      <p class="ans-line">1. 광속 : <span class="ans">증가</span></p>
      <p class="ans-line">2. 점등시간 : <span class="ans">늦음</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 41</div>
</div>

<!-- ===== p.42 083 ===== -->
<div class="page" id="page-042">
  <div class="day-tag abs">단답비급 DAY 4</div>
  <div class="content" style="top:72px;">
    <div class="q">
      <div class="q-num">083.</div><hr class="q-hline">
      <p class="q-text">눈부심을 일으키는 원인 5가지만 쓰시오.</p>
      <p class="ans-line">1. 광원을 <span class="ans">오랫동안 주시</span>할 때</p>
      <p class="ans-line">2. 눈에 입사하는 <span class="ans">광속의 과다</span></p>
      <p class="ans-line">3. <span class="ans">고휘도</span>의 광원</p>
      <p class="ans-line">4. <span class="ans">순응</span>의 결핍</p>
      <p class="ans-line">5. 물체와 그 주위 사이의 <span class="ans">고휘도 대비</span></p>
    </div>
  </div>
  <div class="brand-l abs">42 • 전기치트키</div>
</div>

<!-- ===== p.43 전동기1 084~087 ===== -->
<div class="page" id="page-043">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">전동기 1</div>
  <div class="content" style="top:118px;">
    <div class="q">
      <div class="q-num">084.</div><hr class="q-hline">
      <p class="q-text">단상 유도전동기는 반드시 기동장치가 필요하다. 기동장치가 필요한 이유를 설명하시오.</p>
      <p class="ans-line"><span class="ans">단상 유도전동기는 스스로 회전자계가 생기지 않아 보조권선에 의해 회전자계를 발생시켜 기동한다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">085.</div><hr class="q-hline">
      <p class="q-text">단상 유도전동기의 기동방식에 따라 분류할 때 그 종류를 4가지 쓰시오.</p>
      <div class="formula-row">
        <span>① <span class="ans">반발 기동형</span></span>
        <span>② <span class="ans">콘덴서 기동형</span></span>
        <span>③ <span class="ans">분상 기동형</span></span>
        <span>④ <span class="ans">세이딩 코일형</span></span>
      </div>
    </div>
    <div class="q">
      <div class="q-num">086.</div><hr class="q-hline">
      <p class="q-text">콘덴서 기동형 단상 유도전동기의 기동원리를 쓰시오.</p>
      <p class="ans-line"><span class="ans">주권선(운전권선) 전류와 보조권선(가동권선) 전류의 위상차</span>에 의한 <span class="ans">회전자계</span>에 의해 기동하는 단상 유도 전동기이다.</p>
    </div>
    <div class="q">
      <div class="q-num">087.</div><hr class="q-hline">
      <p class="q-text">다음에 주어진 단상 유도전동기의 종류에 따른 보기의 전동기 역회전 방법을 골라 짝지으시오.</p>
      <div class="formula-row" style="font-size:9.5pt;align-items:flex-start;">
        <div><b>【종류】</b><br>1. 반발 기동형<br>2. 분상 기동형<br>3. 세이딩 코일형</div>
        <div><b>【보기】</b><br>ㄱ. 역회전이 불가능하다<br>ㄴ. 기동권선의 접속을 반대로 한다.<br>ㄷ. 브러시 위치를 이동한다.</div>
      </div>
      <p class="ans-line" style="margin-top:6px;"><span class="ans">① - ㄷ, &nbsp; ② - ㄴ, &nbsp; ③ - ㄱ</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 43</div>
</div>
"""

PAGES_44_49 = r"""
<!-- ===== p.44 088~091 ===== -->
<div class="page" id="page-044">
  <div class="day-tag abs">단답비급 DAY 4</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">088.</div><hr class="q-hline">
      <p class="q-text">분상 기동형 단상 유도 전동기의 회전 방향을 바꾸려면 어떻게 하면 되는가?</p>
      <p class="ans-line"><span class="ans">기동권선의 접속을 반대로 바꾸어 준다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">089.</div><hr class="q-hline">
      <p class="q-text">단상 유도 전동기의 절연을 E종 절연물로 하였을 경우 허용 최고 온도는 몇 [°C]인가? <span class="ans">120[°C]</span></p>
      <img src="../assets/images/manual/crops/p044_tbl089.png" style="width:100%;max-height:90px;object-fit:contain;margin:6px 0;" alt="절연등급 표">
    </div>
    <div class="q">
      <div class="q-num">090.</div><hr class="q-hline">
      <p class="q-text">유도전동기를 정·역운전할 때, 정회전 전자접촉기와 역회전 전자접촉기가 동시에 작동하지 못하도록 보조회로에서 전기적으로 안전하게 구성하는 것을 무엇이라 하는가?</p>
      <p class="ans-line"><span class="ans">인터록</span></p>
    </div>
    <div class="q">
      <div class="q-num">091.</div><hr class="q-hline">
      <p class="q-text">수중 펌프용 전동기의 MCC반에 대하여 물음에 답하시오.</p>
      <p class="ans-line">1. 현장 조작반에서 MCC까지 전선은 어떤 종류의 케이블을 사용하는 것이 적합한지 쓰시오.</p>
      <p class="ans-line"><span class="ans">CCV($0.6/1$[kV] 제어용 가교폴리에틸렌 절연 비닐시스 케이블)</span></p>
      <p class="ans-line" style="margin-top:4px;">2. 어떤 종류의 차단기를 사용하는 것이 가장 적합한지 쓰시오.</p>
      <p class="ans-line"><span class="ans">누전차단기</span></p>
    </div>
  </div>
  <div class="brand-l abs">44 • 전기치트키</div>
</div>

<!-- ===== p.45 092~093 ===== -->
<div class="page" id="page-045">
  <div class="brand abs">전기치트키</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">092.</div><hr class="q-hline">
      <p class="q-text">유도 전동기는 농형과 권선형으로 구분되는데 각 형식별 기동법을 아래 빈칸에 쓰시오.</p>
      <img src="../assets/images/manual/crops/p045_tbl092.png" style="width:100%;max-height:340px;object-fit:contain;margin:6px 0;" alt="기동법 표">
      <p class="ans-line" style="font-size:9.5pt;">① <span class="ans">직입기동</span> &nbsp; ② <span class="ans">$Y$-$\Delta$기동</span> &nbsp; ③ <span class="ans">기동보상기법</span></p>
      <p class="ans-line" style="font-size:9.5pt;">④ <span class="ans">2차 저항 기동법</span> &nbsp; ⑤ <span class="ans">2차 임피던스 기동법</span></p>
    </div>
    <div class="q">
      <div class="q-num">093.</div><hr class="q-hline">
      <p class="q-text">3상 농형 유도전동기의 제동방법 중에서 역상제동에 대하여 설명하시오.</p>
      <p class="ans-line"><span class="ans">회전 중에 있는 전동기의 1차 권선의 3단자 중 임의의 2단자의 접속을 바꿔 전동기의 회전과 역방향의 토크를 발생시켜 제동하는 방법</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 45</div>
</div>

<!-- ===== p.46 094~098 ===== -->
<div class="page" id="page-046">
  <div class="day-tag abs">단답비급 DAY 4</div>
  <div class="content" style="top:58px;">
    <div class="q">
      <div class="q-num">094.</div><hr class="q-hline">
      <p class="q-text"><b>Y-Δ 기동</b>에 대하여 <b>설명</b>하시오.</p>
      <p class="ans-line"><span class="ans">기동전압 $\frac{1}{\sqrt{3}}$ 배로 감소, 기동전류를 $\frac{1}{3}$ 배로 감소시켜 기동특성을 개선한 기동법</span></p>
    </div>
    <div class="q">
      <div class="q-num">095.</div><hr class="q-hline">
      <p class="q-text"><b>Y-Δ 기동 시</b>와 <b>전전압 기동 시</b>의 <b>기동 전류</b>를 <b>비교 설명</b>하시오.</p>
      <p class="ans-line"><span class="ans">Y-Δ 기동전류는 전전압 기동 전류의 $\frac{1}{3}$배이다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">096.</div><hr class="q-hline">
      <p class="q-text">전동기를 운전할 때 <b>Y-Δ 기동</b>에 대한 <b>기동 및 운전</b>에 대한 <b>조작 요령</b>을 <b>설명</b>하시오.</p>
      <p class="ans-line"><span class="ans">Y결선으로 기동한 후 설정 시간이 지나면 Δ결선으로 운전한다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">097.</div><hr class="q-hline">
      <p class="q-text">3상 농형 유도전동기의 기동방식 중 <b>리액터 기동방식</b>에 대하여 <b>설명</b>하시오.</p>
      <p class="ans-line"><span class="ans">기동 시 유도전동기에 직렬로 리액터를 설치하여 전동기에 인가되는 전압을 감압시켜 기동하는 방법</span></p>
    </div>
    <div class="q">
      <div class="q-num">098.</div><hr class="q-hline">
      <p class="q-text">전동기의 <b>기동 보상기</b> <b>기동제어</b>는 어떤 기동 방법인지 그 <b>방법</b>을 <b>상세히 설명</b>하시오.</p>
      <p class="ans-line"><span class="ans">기동 시 전동기에 대한 인가전압을 단권 변압기로 감압하여 공급함으로써 기동전류를 억제하고 기동 완료 후 전전압을 가하는 방식</span></p>
    </div>
  </div>
  <div class="brand-l abs">46 • 전기치트키</div>
</div>

<!-- ===== p.47 memo ===== -->
<div class="page" id="page-047">
  <div class="brand abs">전기치트키</div>
  <div class="content" style="top:72px;">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
    <p class="abs" style="left:50%;top:45%;transform:translate(-50%,-50%);font-size:48pt;color:#eee;font-weight:700;">DAY 5</p>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 47</div>
</div>

<!-- ===== p.48 DAY5 구분 ===== -->
<div class="page" id="page-048">
  <div class="day-banner abs">DAY 5</div>
  <div class="topic-box abs" style="line-height:1.9;">전동기 2<br>발전기<br>태양광<br>전지</div>
  <img class="abs" src="../assets/images/manual/crops/p048_day5_char.png" style="left:80px;top:500px;width:260px;" alt="">
</div>

<!-- ===== p.49 전동기2 099~101 ===== -->
<div class="page" id="page-049">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">전동기 2</div>
  <div class="content" style="top:118px;">
    <div class="q">
      <div class="q-num">099.</div><hr class="q-hline">
      <p class="q-text">그림과 같이 3상 농형 유도 전동기 4대가 있다. 전동기 기동방식을 기기의 수명과 경제적인 면을 고려한다면 어떤 방식이 적합한가?</p>
      <img src="../assets/images/manual/crops/p049_diag099.png" style="width:100%;max-height:200px;object-fit:contain;margin:6px 0;" alt="전동기 4대 계통도">
      <p class="ans-line"><span class="ans">기동보상기법</span></p>
    </div>
    <div class="q">
      <div class="q-num">100.</div><hr class="q-hline">
      <p class="q-text">전기 방폭설비란 무엇을 의미하는지 설명하시오.</p>
      <p class="ans-line"><span class="ans">전기설비가 점화원이 되는 폭발을 방지하기 위한 설비</span></p>
    </div>
    <div class="q">
      <div class="q-num">101.</div><hr class="q-hline">
      <p class="q-text">전기설비의 방폭구조 종류 중 4가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">내압</span> 방폭구조</p>
      <p class="ans-line">② <span class="ans">유입</span> 방폭구조</p>
      <p class="ans-line">③ <span class="ans">압력</span> 방폭구조</p>
      <p class="ans-line">④ <span class="ans">안전증</span> 방폭구조</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 49</div>
</div>
"""


def main() -> None:
    html = HTML.read_text(encoding="utf-8")
    marker = "\n</div>\n\n<script defer src=\"https://cdn.jsdelivr.net/npm/katex"

    html = html.replace(
        "$\x0barepsilon = F/\x0barphi$",
        r"$\varepsilon = F/\varphi$",
    )

    if 'id="page-038"' not in html:
        html = html.replace(marker, PAGES_38_43 + marker, 1)
        print("Appended pages 38-43")

    if 'id="page-044"' not in html:
        html = html.replace(marker, PAGES_44_49 + marker, 1)
        print("Appended pages 44-49")

    for old, new in [
        ('<span id="pg-info">p.1–31 (DAY1~3 진행중) · 직접 전사</span>', '<span id="pg-info">p.1–49 (DAY1~5 진행중) · 직접 전사</span>'),
        ('<span id="pg-info">p.1–37 (DAY1~4 진행중) · 직접 전사</span>', '<span id="pg-info">p.1–49 (DAY1~5 진행중) · 직접 전사</span>'),
        ('<span id="pg-info">p.1–43 (DAY1~4 진행중) · 직접 전사</span>', '<span id="pg-info">p.1–49 (DAY1~5 진행중) · 직접 전사</span>'),
    ]:
        html = html.replace(old, new)

    HTML.write_text(html, encoding="utf-8")
    print(f"Updated {HTML}")


if __name__ == "__main__":
    main()
