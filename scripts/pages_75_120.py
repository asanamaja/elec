#!/usr/bin/env python3
"""HTML transcription for manual pages 75-120."""

PAGES_75_120 = r"""
<!-- ===== p.75 memo ===== -->
<div class="page" id="page-075">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 75</div>
</div>

<!-- ===== p.76 DAY 7 ===== -->
<div class="page" id="page-076">
  <div class="day-banner abs">DAY 7</div>
  <div class="topic-box abs" style="line-height:2.0;">차단기<br>퓨즈<br>개폐기</div>
</div>

<!-- ===== p.77 171~173 ===== -->
<div class="page" id="page-077">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">차단기</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">171.</div><hr class="q-hline">
      <p class="q-text">차단기의 정격전압을 작성하시오.</p>
      <table class="tbl">
        <tr><th>공칭전압[$kV$]</th><th>차단기 정격전압[$kV$]</th></tr>
        <tr><td>3.3</td><td><span class="ans">3.6</span></td></tr>
        <tr><td>6.6</td><td><span class="ans">7.2</span></td></tr>
        <tr><td>22</td><td><span class="ans">24</span></td></tr>
        <tr><td>22.9</td><td><span class="ans">25.8</span></td></tr>
        <tr><td>66</td><td><span class="ans">72.5</span></td></tr>
        <tr><td>154</td><td><span class="ans">170</span></td></tr>
        <tr><td>345</td><td><span class="ans">362</span></td></tr>
        <tr><td>765</td><td><span class="ans">800</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">172.</div><hr class="q-hline">
      <p class="q-text">우리나라에서 송전계통에 사용하는 차단기의 정격전압과 정격차단시간을 나타낸 표이다. 다음 빈칸을 채우시오. (단, 사이클은 $60[Hz]$ 기준이다.)</p>
      <table class="tbl">
        <tr><th>공칭전압[$kV$]</th><td>22.9</td><td>154</td><td>345</td></tr>
        <tr><th>정격전압[$kV$]</th><td><span class="ans">25.8</span></td><td><span class="ans">170</span></td><td><span class="ans">362</span></td></tr>
        <tr><th>정격차단시간 [$c/s$]<br>(cycle은 $60[Hz]$ 기준)</th><td><span class="ans">5</span></td><td><span class="ans">3</span></td><td><span class="ans">3</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">173.</div><hr class="q-hline">
      <p class="q-text">CB의 기능을 쓰시오.</p>
      <p class="ans-line"><span class="ans">부하전류 개폐 및 고장전류 차단</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 77</div>
</div>

<!-- ===== p.78 174~178 ===== -->
<div class="page" id="page-078">
  <div class="day-tag abs">단답비급 DAY 7</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">174.</div><hr class="q-hline">
      <p class="q-text">차단기 "동작책무"란?</p>
      <p class="ans-line"><span class="ans">차단기에 부과된 1회 또는 2회 이상의 투입, 차단동작을 일정시간 간격을 두고 행하는 일련의 동작을 동작책무라 한다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">175.</div><hr class="q-hline">
      <p class="q-text">다음 차단기 약호를 보고 명칭을 쓰시오.</p>
      <p class="ans-line">(1) OCB : <span class="ans">유입</span>차단기 &nbsp; (2) ABB : <span class="ans">공기</span>차단기</p>
      <p class="ans-line">(3) GCB : <span class="ans">가스</span>차단기 &nbsp; (4) MBB : <span class="ans">자기</span>차단기</p>
    </div>
    <div class="q">
      <div class="q-num">176.</div><hr class="q-hline">
      <p class="q-text">ACB의 우리말 명칭을 쓰시오.</p>
      <p class="ans-line"><span class="ans">기중</span>차단기</p>
    </div>
    <div class="q">
      <div class="q-num">177.</div><hr class="q-hline">
      <p class="q-text">VCB의 특징 3가지를 작성하시오.</p>
      <p class="ans-line">① 짧은 <span class="ans">차단시간</span>, 우수한 <span class="ans">차단성능</span></p>
      <p class="ans-line">② 긴 <span class="ans">수명</span></p>
      <p class="ans-line">③ <span class="ans">화재</span>에 대한 <span class="ans">안전성</span>이 우수함</p>
    </div>
    <div class="q">
      <div class="q-num">178.</div><hr class="q-hline">
      <p class="q-text">GCB 내에 사용되는 가스의 명칭을 쓰시오.</p>
      <p class="ans-line"><span class="ans">$SF_6$</span></p>
    </div>
  </div>
  <div class="brand-l abs">78 • 전기치트키</div>
</div>

<!-- ===== p.79 179~181 ===== -->
<div class="page" id="page-079">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">179.</div><hr class="q-hline">
      <p class="q-text">특고압 및 저압 차단기 종류 3가지의 영문 약호와 한글 명칭을 쓰시오.</p>
      <p><b>1. 특고압 차단기</b></p>
      <p class="ans-line">① <span class="ans">OCB(유입차단기)</span> &nbsp; ② <span class="ans">VCB(진공차단기)</span> &nbsp; ③ <span class="ans">GCB(가스차단기)</span></p>
      <p><b>2. 저압 차단기</b></p>
      <p class="ans-line">① <span class="ans">MCCB(배선용차단기)</span> &nbsp; ② <span class="ans">ELB(누전차단기)</span> &nbsp; ③ <span class="ans">ACB(기중차단기)</span></p>
    </div>
    <div class="q">
      <div class="q-num">180.</div><hr class="q-hline">
      <p class="q-text">차단기는 보호 계전기의 4가지 요소에 의해 동작되도록 하는데 그 4가지 요소를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">단일 전류 요소</span> &nbsp; ② <span class="ans">단일 전압 요소</span></p>
      <p class="ans-line">③ <span class="ans">전압 전류 요소</span> &nbsp; ④ <span class="ans">2전류 요소</span></p>
    </div>
    <div class="q">
      <div class="q-num">181.</div><hr class="q-hline">
      <p class="q-text">차단기의 트립방식을 4가지 쓰고 각 방식을 간단히 설명하시오.</p>
      <table class="tbl">
        <tr><th>구분</th><th>설명</th></tr>
        <tr><td><span class="ans">직류 트립방식</span></td><td><span class="ans">고장 시 제어용 직류 전원에 의해 트립</span></td></tr>
        <tr><td><span class="ans">콘덴서 트립방식</span></td><td><span class="ans">고장 시 충전된 콘덴서의 에너지에 의해 트립</span></td></tr>
        <tr><td><span class="ans">전류 트립방식</span></td><td><span class="ans">고장 시 변류기 2차 전류에 의해 트립</span></td></tr>
        <tr><td><span class="ans">부족전압 트립방식</span></td><td><span class="ans">고장 시 전압의 저하에 의해 트립</span></td></tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 79</div>
</div>

<!-- ===== p.80 182~185 ===== -->
<div class="page" id="page-080">
  <div class="day-tag abs">단답비급 DAY 7</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">182.</div><hr class="q-hline">
      <p class="q-text">기호의 명칭을 구체적으로 쓰시오.</p>
      <!--IMG:p080_diag182-->
      <p class="ans-line"><span class="ans">인출형 (플러그인 타입) 차단기</span></p>
    </div>
    <div class="q">
      <div class="q-num">183.</div><hr class="q-hline">
      <p class="q-text">사용전압이 $22.9[kV]$라고 할 때 차단기의 트립 전원은 어떤 방식이 바람직한가?</p>
      <p class="ans-line"><span class="ans">직류(DC) 또는 콘덴서(CTD) 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">184.</div><hr class="q-hline">
      <p class="q-text">$66[kV]$ 이상의 수전설비에서 사용하는 차단기는 어떤 트립 전원 방식을 사용하여야 하는가?</p>
      <p class="ans-line"><span class="ans">직류(DC) 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">185.</div><hr class="q-hline">
      <p class="q-text">욕실 등 인체가 물에 젖어 있는 상태에서 물을 사용하는 장소에 콘센트를 시설하는 경우에 설치하여야 하는 저압 차단기의 정확한 명칭을 쓰시오.</p>
      <p class="ans-line"><span class="ans">인체감전보호용 누전차단기(정격감도전류 $15[mA]$ 이하, 동작시간 $0.03$초 이하의 전류동작형)</span></p>
    </div>
  </div>
  <div class="brand-l abs">80 • 전기치트키</div>
</div>

<!-- ===== p.81 186 ===== -->
<div class="page" id="page-081">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">186.</div><hr class="q-hline">
      <p class="q-text">누전 차단기의 시설 예에 대한 표의 빈 칸에 ○, △, □를 표현하시오.</p>
      <p class="q-text" style="font-size:9pt;">누전차단기의 시설 구분에 대한 표시 기호는 다음과 같다.<br>
      ○ : 누전차단기를 시설하는 곳<br>
      △ : 주택에 기계기구를 시설하는 경우에는 누전차단기를 시설할 곳<br>
      □ : 주택 구내 또는 도로에 접한 면에 룸에어컨디셔너, 아이스 박스, 진열장, 자동판매기 등 전동기를 부품으로 한 기계기구를 시설하는 경우에는 누전차단기를 시설하는 것이 바람직한 곳</p>
      <table class="tbl">
        <tr>
          <th rowspan="2">기계기구의<br>시설장소<br><br>전로의<br>대지전압</th>
          <th colspan="2">옥내</th>
          <th colspan="2">옥외</th>
          <th rowspan="2">물기가<br>있는<br>장소</th>
        </tr>
        <tr>
          <th>건조한<br>장소</th>
          <th>습기가<br>많은<br>장소</th>
          <th>우선 내</th>
          <th>우선 외</th>
        </tr>
        <tr>
          <td>$150[V]$ 이하</td>
          <td>-</td><td>-</td><td>-</td>
          <td><span class="ans">□</span></td>
          <td><span class="ans">□</span></td>
          <td><span class="ans">○</span></td>
        </tr>
        <tr>
          <td>$150[V]$ 초과<br>$300[V]$ 이하</td>
          <td><span class="ans">△</span></td>
          <td><span class="ans">○</span></td>
          <td><span class="ans">○</span></td>
          <td><span class="ans">○</span></td>
          <td><span class="ans">○</span></td>
        </tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 81</div>
</div>

<!-- ===== p.82 187~188 ===== -->
<div class="page" id="page-082">
  <div class="day-tag abs">단답비급 DAY 7</div>
  <div class="sec-title abs" style="top:72px;">퓨즈</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">187.</div><hr class="q-hline">
      <p class="q-text">퓨즈 정격사항에 대하여 주어진 표의 빈칸에 쓰시오.</p>
      <table class="tbl">
        <tr><th>계통전압 [$kV$]</th><th>퓨즈 정격전압 [$kV$]</th><th>최대 설계전압 [$kV$]</th></tr>
        <tr><td>6.6</td><td><span class="ans">7.2</span></td><td>8.25</td></tr>
        <tr><td>13.2</td><td>15</td><td><span class="ans">15.5</span></td></tr>
        <tr><td>22 또는 22.9</td><td><span class="ans">23</span></td><td>25.8</td></tr>
        <tr><td>66</td><td>69</td><td><span class="ans">72.5</span></td></tr>
        <tr><td>154</td><td><span class="ans">161</span></td><td>169</td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">188.</div><hr class="q-hline">
      <p class="q-text">다음은 전력퓨즈의 용단 및 동작특성에 관한 표이다. 괄호 안에 알맞은 내용을 쓰시오.</p>
      <table class="tbl">
        <tr><th>정격전류의 배수</th><th>불용단시간</th><th>용단시간</th></tr>
        <tr><td>4배</td><td>(① <span class="ans">300</span>)초 이내</td><td>-</td></tr>
        <tr><td>6.3배</td><td>-</td><td>(③ <span class="ans">60</span>)초 이내</td></tr>
        <tr><td>8배</td><td>0.5초 이내</td><td>-</td></tr>
        <tr><td>10배</td><td>(② <span class="ans">0.2</span>)초 이내</td><td>-</td></tr>
        <tr><td>12.5배</td><td>-</td><td>0.5초 이내</td></tr>
        <tr><td>19배</td><td>-</td><td>(④ <span class="ans">0.1</span>)초 이내</td></tr>
      </table>
    </div>
  </div>
  <div class="brand-l abs">82 • 전기치트키</div>
</div>

<!-- ===== p.83 189~193 ===== -->
<div class="page" id="page-083">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">189.</div><hr class="q-hline">
      <p class="q-text">전력퓨즈의 역할은 무엇인가 간단히 쓰시오.</p>
      <p class="ans-line">① <span class="ans">부하전류</span>를 안전하게 <span class="ans">통전</span>한다.</p>
      <p class="ans-line">② 일정치 이상의 <span class="ans">과전류</span>는 <span class="ans">차단</span>하여 전로나 기기를 보호한다.</p>
    </div>
    <div class="q">
      <div class="q-num">190.</div><hr class="q-hline">
      <p class="q-text">퓨즈의 성능(특성) 3가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">용단</span> 특성</p>
      <p class="ans-line">② <span class="ans">전차단</span> 특성</p>
      <p class="ans-line">③ <span class="ans">단시간 허용</span> 특성</p>
    </div>
    <div class="q">
      <div class="q-num">191.</div><hr class="q-hline">
      <p class="q-text">PF(한류퓨즈)의 단점 4가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">재투입</span>을 할 수 없다.</p>
      <p class="ans-line">② <span class="ans">과도전류</span>에서 <span class="ans">용단</span>될 수도 있다.</p>
      <p class="ans-line">③ 차단 시에 <span class="ans">과전압</span>이 발생한다.</p>
      <p class="ans-line">④ <span class="ans">동작시간</span>과 <span class="ans">전류특성</span>을 자유로이 조정할 수 없다.</p>
    </div>
    <div class="q">
      <div class="q-num">192.</div><hr class="q-hline">
      <p class="q-text">전력퓨즈(PF)의 가장 큰 단점은 무엇인가?</p>
      <p class="ans-line"><span class="ans">재투입</span>을 할 수 없다.</p>
    </div>
    <div class="q">
      <div class="q-num">193.</div><hr class="q-hline">
      <p class="q-text">전력퓨즈(PF)를 구입하고자 할 때 고려해야 할 주요사항을 4가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">정격전압</span> &nbsp; ② <span class="ans">정격전류</span></p>
      <p class="ans-line">③ <span class="ans">정격차단전류</span> &nbsp; ④ <span class="ans">사용장소</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 83</div>
</div>

<!-- ===== p.84 194~197 ===== -->
<div class="page" id="page-084">
  <div class="day-tag abs">단답비급 DAY 7</div>
  <div class="sec-title abs" style="top:72px;">개폐기 1</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">194.</div><hr class="q-hline">
      <p class="q-text">단로기의 정격전압을 작성하시오.</p>
      <table class="tbl">
        <tr><th>공칭전압[$kV$]</th><th>단로기 정격전압[$kV$]</th></tr>
        <tr><td>3.3</td><td><span class="ans">3.6</span></td></tr>
        <tr><td>6.6</td><td><span class="ans">7.2</span></td></tr>
        <tr><td>22</td><td><span class="ans">24</span></td></tr>
        <tr><td>22.9</td><td><span class="ans">25.8</span></td></tr>
        <tr><td>66</td><td><span class="ans">72.5</span></td></tr>
        <tr><td>154</td><td><span class="ans">170</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">195.</div><hr class="q-hline">
      <p class="q-text">긴급할 때 DS로 개폐 가능한 전류의 종류를 2가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">무부하 충전전류</span></p>
      <p class="ans-line">② <span class="ans">변압기 여자전류</span></p>
    </div>
    <div class="q">
      <div class="q-num">196.</div><hr class="q-hline">
      <p class="q-text">수전전압이 $66[kV]$ 이상인 경우 인입구 개폐기로 DS 대신 어떤 것을 사용하여야 하는가?</p>
      <p class="ans-line"><span class="ans">LS(선로개폐기)</span></p>
    </div>
    <div class="q">
      <div class="q-num">197.</div><hr class="q-hline">
      <p class="q-text">인입구 개폐기로 DS 대신 사용하는 기기의 명칭과 약호를 쓰시오.</p>
      <p class="ans-line">• 명칭 : <span class="ans">자동 고장 구분개폐기</span></p>
      <p class="ans-line">• 약호 : <span class="ans">ASS</span></p>
    </div>
  </div>
  <div class="brand-l abs">84 • 전기치트키</div>
</div>

<!-- ===== p.85 198~200 ===== -->
<div class="page" id="page-085">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">198.</div><hr class="q-hline">
      <p class="q-text">다음 기기의 명칭을 쓰시오.</p>
      <p class="q-text" style="font-size:9pt;">1. 가공 배전선로 사고의 대부분은 조류 및 수목에 의한 접촉, 강풍, 낙뢰 등에 의한 플래시오버 사고로서 이런 사고 발생 시 신속하게 고장구간을 차단하고 사고점의 아크를 소멸 시킨 후 즉시 재투입이 가능한 개폐장치이다.</p>
      <p class="ans-line"><span class="ans">리클로저</span></p>
      <p class="q-text" style="font-size:9pt;">2. 보안상 책임 분계점에서 보수 점검 시 전로를 개폐하기 위하여 시설하는 것으로 반드시 무부하 상태에서 개방하여야 한다. 근래에는 ASS를 사용하며, $66[kV]$ 이상의 경우에는 이를 사용한다.</p>
      <p class="ans-line"><span class="ans">선로 개폐기(LS)</span></p>
    </div>
    <div class="q">
      <div class="q-num">199.</div><hr class="q-hline">
      <p class="q-text">설치장소에 따른 자동고장 구분개폐기(ASS)의 정격을 작성하시오.</p>
      <table class="tbl">
        <tr><th>정격전압</th><th>정격전류</th><th>설치장소</th></tr>
        <tr>
          <td rowspan="2"><span class="ans">25.8[kV]</span></td>
          <td><span class="ans">200[A]</span></td>
          <td style="font-size:8.5pt;">$22.9[kV-Y]$ 전기사업자 배전계통에서<br>• 부하용량 $4000[kVA]$(특수부하 $2000[kVA]$) 이하의 분기점<br>• 부하용량 $7000[kVA]$ 이하의 수전실 인입구</td>
        </tr>
        <tr>
          <td><span class="ans">400[A]</span></td>
          <td style="font-size:8.5pt;">$22.9[kV-Y]$ 전기사업자 배전계통에서 부하용량 $8000[kVA]$(특수부하 $4000[kVA]$) 이하의 분기점 또는 수전실 인입구</td>
        </tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">200.</div><hr class="q-hline">
      <p class="q-text">과부하 시 자동으로 개폐할 수 있는 고장 구분 개폐기는?</p>
      <p class="ans-line"><span class="ans">자동고장 구분개폐기(ASS)</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 85</div>
</div>

<!-- ===== p.86 201~204 ===== -->
<div class="page" id="page-086">
  <div class="day-tag abs">단답비급 DAY 7</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">201.</div><hr class="q-hline">
      <p class="q-text">용량 $300[kVA]$ 이하에서 ASS 대신 사용할 수 있는 것은?</p>
      <p class="ans-line"><span class="ans">인터럽트 스위치(INT.SW)</span></p>
    </div>
    <div class="q">
      <div class="q-num">202.</div><hr class="q-hline">
      <p class="q-text">ASS의 LOCK 전류값과 LOCK 전류의 기능을 쓰시오.</p>
      <p class="ans-line">① LOCK 전류값 : <span class="ans">$800[A] \pm 10[\%]$</span></p>
      <p class="ans-line">② 과전류 LOCK 기능 : <span class="ans">LOCK 전류 이상의 전류가 흐르면 ASS는 LOCK 되며, 후비보호장치에 의해 고장전류가 제거된 후 ASS가 개방된다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">203.</div><hr class="q-hline">
      <p class="q-text">간이 수변전설비에서는 1차측 개폐기로 ASS(Auto Section Switch)나 인터럽트 스위치를 사용하고 있다. 이 두 스위치의 차이점을 비교 설명하시오.</p>
      <p class="ans-line">1. <span class="ans">ASS (Automatic Section Switch) : 무전압 시 개방이 가능, 과부하 시 자동개방, 돌입전류 억제기능을 갖고 있음</span></p>
      <p class="ans-line">2. <span class="ans">인터럽트 스위치(Interrupter Switch) : 수동 조작만 가능, 과부하 시 자동개폐할 수 없음, 돌입전류 억제기능을 갖고 있지 않음, 용량 $300[kVA]$ 이하에서 ASS 대신에 주로 사용</span></p>
    </div>
    <div class="q">
      <div class="q-num">204.</div><hr class="q-hline">
      <p class="q-text">$22.9[kV]$에서 사용하는 기중부하개폐기(IS)와 자동부하전환개폐기(ALTS)의 정격전압과 정격전류를 쓰시오.</p>
      <p class="ans-line">• 정격전압 : <span class="ans">$25.8[kV]$</span></p>
      <p class="ans-line">• 정격전류 : <span class="ans">$600[A]$</span></p>
    </div>
  </div>
  <div class="brand-l abs">86 • 전기치트키</div>
</div>

<!-- ===== p.87 205~207 ===== -->
<div class="page" id="page-087">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">205.</div><hr class="q-hline">
      <p class="q-text">ALTS의 명칭과 사용 용도를 쓰시오.</p>
      <p class="ans-line"><span class="ans">[명칭] 자동부하 전환개폐기</span></p>
      <p class="ans-line"><span class="ans">[용도] $22.9[kV-Y]$ 배전선로에 사용되는 개폐기로 수용가에 이중전원을 확보하여 주전원 정전 시 예비전원으로 자동 절체되어 무정전 전원공급을 수행한다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">206.</div><hr class="q-hline">
      <p class="q-text">AISS의 명칭을 쓰고, 기능을 2가지 쓰시오.</p>
      <p class="ans-line"><span class="ans">[명칭] 기중 절연형 자동고장 구분개폐기</span></p>
      <p class="ans-line"><span class="ans">[기능] ① 고장구간을 자동으로 개방하여 사고확대를 방지</span></p>
      <p class="ans-line"><span class="ans">② 전부하 상태에서 자동(또는 수동)으로 개방하여 과부하 보호</span></p>
    </div>
    <div class="q">
      <div class="q-num">207.</div><hr class="q-hline">
      <p class="q-text">LBS에 대하여 다음 물음에 답하시오.</p>
      <p class="q-text">1. 우리말 명칭을 쓰시오.</p>
      <p class="ans-line"><span class="ans">부하개폐기</span></p>
      <p class="q-text">2. 기능과 역할에 대해 간단히 설명하시오.</p>
      <p class="ans-line"><span class="ans">[기능] 정상상태의 무부하 전류 및 부하전류를 개폐할 수 있으나, 고장전류는 차단할 수 없음.</span></p>
      <p class="ans-line"><span class="ans">[역할] 개폐 빈도가 낮은 송배전 및 수변전 설비의 인입구 개폐</span></p>
      <p class="q-text">3. 같은 용도로 사용되는 기기를 2종류만 쓰시오.</p>
      <p class="ans-line"><span class="ans">① 기중 부하개폐기 ② 자동고장 구분개폐기</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 87</div>
</div>

<!-- ===== p.88 208 ===== -->
<div class="page" id="page-088">
  <div class="day-tag abs">단답비급 DAY 7</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">208.</div><hr class="q-hline">
      <p class="q-text">저압 전로중에 개폐기를 시설하는 경우에는 부하용량에 적합한 크기의 개폐기를 각 극에 설치하여야 한다. 그러나 분기 개폐기에는 생략하여도 되는 경우가 있다. 다음 도면에서 생략하여도 되는 부분은 어느 개소인지를 모두 지적(영문 표기)하시오.</p>
      <p>1.</p>
      <!--IMG:p088_diag208_1-->
      <p class="ans-line">답 : <span class="ans">E, H, J</span></p>
      <p>2.</p>
      <!--IMG:p088_diag208_2-->
      <p class="ans-line">답 : <span class="ans">D, E</span></p>
    </div>
  </div>
  <div class="brand-l abs">88 • 전기치트키</div>
</div>

<!-- ===== p.89 memo ===== -->
<div class="page" id="page-089">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 89</div>
</div>

<!-- ===== p.90 DAY 8 ===== -->
<div class="page" id="page-090">
  <div class="day-banner abs">DAY 8</div>
  <div class="topic-box abs" style="line-height:2.0;">개폐기 2<br>피뢰기</div>
</div>
<!-- ===== p.91 209 ===== -->
<div class="page" id="page-091">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">개폐기 2</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">209.</div><hr class="q-hline">
      <p class="q-text">다음 개폐기의 종류를 나열한 것이다. 기기의 특징에 알맞은 명칭을 빈칸에 쓰시오.</p>
      <table class="tbl" style="font-size:8.5pt;">
        <tr><th>명칭</th><th>특징</th></tr>
        <tr><td><span class="ans">단로기(DS)</span></td><td>• 전로의 접속을 바꾸거나 끊는 목적으로 사용<br>• <b>전류의 차단능력은 없음</b><br>• 무전류 상태에서 전로 개폐<br>• 변압기, 차단기 등의 보수점검을 위한 회로 분리용 및 전력계통 변환을 위한 회로분리용으로 사용</td></tr>
        <tr><td><span class="ans">부하개폐기(LBS)</span></td><td>• 평상시 <b>부하전류의 개폐는 가능하나 이상 시(과부하, 단락) 보호기능은 없음</b><br>• 개폐 빈도가 적은 부하의 개폐용 스위치로 사용<br>• <b>전력 Fuse와 사용</b> 시 결상방지 목적으로 사용</td></tr>
        <tr><td><span class="ans">전자접촉기(MC)</span></td><td>• 평상시 부하전류 혹은 과부하전류까지 안전하게 개폐<br>• 부하의 개폐, 제어가 주목적이고, 개폐 빈도가 많음<br>• 부하의 조작, 제어용 스위치로 이용<br>• 전력 Fuse와의 조합에 의한 Combination Switch로 널리 사용</td></tr>
        <tr><td><span class="ans">차단기(CB)</span></td><td>• 평상시 전류 및 사고 시 대전류를 지장 없이 개폐<br>• <b>회로보호가 주목적</b>이며 기구, 제어회로가 Tripping 우선으로 되어 있음<br>• 주회로 보호용 사용</td></tr>
        <tr><td><span class="ans">전력퓨즈(PF)</span></td><td>• 일정치 이상의 과부하전류에서 단락전류까지 대전류 차단<br>• 전로의 개폐 능력은 없다.<br>• 고압개폐기와 조합하여 사용</td></tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 91</div>
</div>

<!-- ===== p.92 210~211 ===== -->
<div class="page" id="page-092">
  <div class="day-tag abs">단답비급 DAY 8</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">210.</div><hr class="q-hline">
      <p class="q-text">각종 개폐기와의 기능 비교표의 관계(동작)되는 해당란에 ○표로 표시하시오.</p>
      <table class="tbl">
        <tr><th rowspan="2">기능</th><th colspan="2">회로분리</th><th colspan="2">사고차단</th></tr>
        <tr><th>무부하</th><th>부하</th><th>과부하</th><th>단락</th></tr>
        <tr><td>퓨즈</td><td><span class="ans">○</span></td><td></td><td></td><td><span class="ans">○</span></td></tr>
        <tr><td>차단기</td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td></tr>
        <tr><td>개폐기</td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td></td></tr>
        <tr><td>단로기</td><td><span class="ans">○</span></td><td></td><td></td><td></td></tr>
        <tr><td>전자접촉기</td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td></td><td></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">211.</div><hr class="q-hline">
      <p class="q-text">다음의 표와 같은 전력개폐장치의 정상전류와 이상전류 시의 통전, 개·폐 등의 가능 유무를 빈칸에 표시하시오. (단, ○ : 가능, △ : 때에 따라 가능, × : 불가능)</p>
      <table class="tbl">
        <tr><th rowspan="2">기구명칭</th><th colspan="3">정상전류</th><th colspan="3">이상전류</th></tr>
        <tr><th>통전</th><th>개</th><th>폐</th><th>통전</th><th>투입</th><th>차단</th></tr>
        <tr><td>차단기</td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td></tr>
        <tr><td>퓨즈</td><td><span class="ans">○</span></td><td><span class="ans">×</span></td><td><span class="ans">×</span></td><td><span class="ans">×</span></td><td><span class="ans">×</span></td><td><span class="ans">○</span></td></tr>
        <tr><td>단로기</td><td><span class="ans">○</span></td><td><span class="ans">△</span></td><td><span class="ans">×</span></td><td><span class="ans">○</span></td><td><span class="ans">×</span></td><td><span class="ans">×</span></td></tr>
        <tr><td>개폐기</td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">○</span></td><td><span class="ans">△</span></td><td><span class="ans">×</span></td></tr>
      </table>
    </div>
  </div>
  <div class="brand-l abs">92 • 전기치트키</div>
</div>

<!-- ===== p.93 212~215 ===== -->
<div class="page" id="page-093">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">212.</div><hr class="q-hline">
      <p class="q-text">가스절연 개폐장치(GIS)의 장점 4가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">소형화</span>할 수 있다.</p>
      <p class="ans-line">② 충전부가 완전히 <span class="ans">밀폐</span>되어 <span class="ans">안전성</span>이 높다.</p>
      <p class="ans-line">③ 대기 중의 오염물의 영향을 받지 않기 때문에 <span class="ans">신뢰성</span>이 높다.</p>
      <p class="ans-line">④ <span class="ans">소음</span>이 적다.</p>
    </div>
    <div class="q">
      <div class="q-num">213.</div><hr class="q-hline">
      <p class="q-text">가스절연 개폐장치(GIS)에 사용되는 가스는 어떤 가스인가?</p>
      <p class="ans-line"><span class="ans">$SF_6$ 가스 (육불화황가스)</span></p>
    </div>
    <div class="q">
      <div class="q-num">214.</div><hr class="q-hline">
      <p class="q-text">가스절연개폐기에 사용되는 가스의 장점을 4가지 쓰시오.</p>
      <p class="ans-line">① <span class="ans">무색, 무취, 무독성</span></p>
      <p class="ans-line">② <span class="ans">소호 능력</span> 우수</p>
      <p class="ans-line">③ <span class="ans">절연내력</span> 높음</p>
      <p class="ans-line">④ <span class="ans">난연성, 불활성</span></p>
    </div>
    <div class="q">
      <div class="q-num">215.</div><hr class="q-hline">
      <p class="q-text">가스절연개폐기에 사용하는 가스는 공기에 비하여 절연내력이 몇 배 정도 좋은가?</p>
      <p class="ans-line"><span class="ans">2~3배</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 93</div>
</div>

<!-- ===== p.94 216~220 ===== -->
<div class="page" id="page-094">
  <div class="day-tag abs">단답비급 DAY 8</div>
  <div class="sec-title abs" style="top:72px;">피뢰기</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">216.</div><hr class="q-hline">
      <p class="q-text">피뢰기 기능과 역할을 쓰시오.</p>
      <p class="ans-line"><span class="ans">이상전압 내습 시 이를 대지로 방전하여 전력설비 기기를 보호하고 속류를 차단한다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">217.</div><hr class="q-hline">
      <p class="q-text">피뢰기의 정격전압은 어떤 전압을 말하는가?</p>
      <p class="ans-line"><span class="ans">속류를 차단할 수 있는 교류 최고전압</span></p>
    </div>
    <div class="q">
      <div class="q-num">218.</div><hr class="q-hline">
      <p class="q-text">피뢰기의 제한전압은 어떤 전압을 말하는가?</p>
      <p class="ans-line"><span class="ans">피뢰기 방전 중 피뢰기 단자에 남게 되는 충격전압</span></p>
    </div>
    <div class="q">
      <div class="q-num">219.</div><hr class="q-hline">
      <p class="q-text">피뢰기의 기능상 필요한 구비조건 4가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">속류 차단능력</span>이 클 것</p>
      <p class="ans-line">② <span class="ans">제한전압</span>이 낮을 것</p>
      <p class="ans-line">③ <span class="ans">상용주파 방전 개시전압</span>이 높을 것</p>
      <p class="ans-line">④ <span class="ans">충격 방전 개시전압</span>이 낮을 것</p>
    </div>
    <div class="q">
      <div class="q-num">220.</div><hr class="q-hline">
      <p class="q-text">피뢰기를 설치해야하는 장소에 대한 기준 4가지를 쓰시오.</p>
      <p class="ans-line" style="font-size:8.5pt;">① <span class="ans">발전소·변전소</span> 또는 이에 준하는 장소의 <span class="ans">가공전선로 인입구 및 인출구</span></p>
      <p class="ans-line" style="font-size:8.5pt;">② 특고압 가공전선로에 접속하는 배전용 변압기의 <span class="ans">고압측 및 특고압측</span></p>
      <p class="ans-line" style="font-size:8.5pt;">③ 고압 및 특고압 가공전선로로부터 공급을 받는 <span class="ans">수용장소의 인입구</span></p>
      <p class="ans-line" style="font-size:8.5pt;">④ <span class="ans">가공전선로와 지중전선로가 접속</span>되는 곳</p>
    </div>
  </div>
  <div class="brand-l abs">94 • 전기치트키</div>
</div>

<!-- ===== p.95 221~222 ===== -->
<div class="page" id="page-095">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">221.</div><hr class="q-hline">
      <p class="q-text">피뢰기와 서지흡수기의 정격전압을 작성하시오.</p>
      <table class="tbl">
        <tr><th>공칭전압[$kV$]</th><th colspan="2">피뢰기 정격전압[$kV$]</th><th>서지흡수기 정격전압[$kV$]</th></tr>
        <tr><th></th><th>변전소</th><th>배전선로</th><th></th></tr>
        <tr><td>3.3</td><td><span class="ans">7.5</span></td><td><span class="ans">7.5</span></td><td><span class="ans">4.5</span></td></tr>
        <tr><td>6.6</td><td><span class="ans">7.5</span></td><td><span class="ans">7.5</span></td><td><span class="ans">7.5</span></td></tr>
        <tr><td>22</td><td><span class="ans">24</span></td><td>-</td><td>-</td></tr>
        <tr><td>22.9</td><td><span class="ans">21</span></td><td><span class="ans">18</span></td><td><span class="ans">18</span></td></tr>
        <tr><td>66</td><td><span class="ans">72</span></td><td>-</td><td>-</td></tr>
        <tr><td>154</td><td><span class="ans">144</span></td><td>-</td><td>-</td></tr>
        <tr><td>345</td><td><span class="ans">288</span></td><td>-</td><td>-</td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">222.</div><hr class="q-hline">
      <p class="q-text">일반적인 시설장소별 적용할 피뢰기의 공칭방전 전류를 쓰시오.</p>
      <table class="tbl" style="font-size:8pt;">
        <tr><th>공칭방전전류</th><th>설치장소</th><th>적용조건</th></tr>
        <tr>
          <td><span class="ans">$10{,}000[A]$</span></td>
          <td>변전소</td>
          <td>$154[kV]$ 이상의 계통<br>$66[kV]$ 및 그 이하의 계통에서 Bank 용량이 $3000[kVA]$를 초과하거나 특히 중요한 곳<br>장거리 송전케이블(배전선로 인출용 단거리 케이블은 제외) 및 정전축전기 Bank를 개폐하는 곳<br>배전선로 인출 측(배전 간선 인출용 장거리 케이블은 제외)</td>
        </tr>
        <tr>
          <td><span class="ans">$5{,}000[A]$</span></td>
          <td>변전소</td>
          <td>$66[kV]$ 및 그 이하의 계통에서 Bank 용량이 $3000[kVA]$ 이하인 곳</td>
        </tr>
        <tr>
          <td><span class="ans">$2{,}500[A]$</span></td>
          <td>선로</td>
          <td>배전선로</td>
        </tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 95</div>
</div>

<!-- ===== p.96 223~224 ===== -->
<div class="page" id="page-096">
  <div class="day-tag abs">단답비급 DAY 8</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">223.</div><hr class="q-hline">
      <p class="q-text">현재 사용되고 있는 교류용 피뢰기의 구조는 무엇과 무엇으로 구성되어 있는가?</p>
      <p class="ans-line"><span class="ans">직렬 갭과 특성요소</span></p>
    </div>
    <div class="q">
      <div class="q-num">224.</div><hr class="q-hline">
      <p class="q-text">화살표로 표시된 각 부분의 명칭을 쓰시오.</p>
      <!--IMG:p096_diag224-->
      <table class="tbl">
        <tr><td>①</td><td>②</td><td>③</td><td>④</td><td>⑤</td><td>⑥</td><td>⑦</td></tr>
        <tr>
          <td><span class="ans">특성요소</span></td>
          <td><span class="ans">주갭</span></td>
          <td><span class="ans">측로갭</span></td>
          <td><span class="ans">분로저항</span></td>
          <td><span class="ans">소호코일</span></td>
          <td><span class="ans">특성요소</span></td>
          <td><span class="ans">특성요소</span></td>
        </tr>
      </table>
    </div>
  </div>
  <div class="brand-l abs">96 • 전기치트키</div>
</div>

<!-- ===== p.97 225~228 ===== -->
<div class="page" id="page-097">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">225.</div><hr class="q-hline">
      <p class="q-text">피뢰기 DISC.의 기능을 간단히 설명하시오.</p>
      <p class="ans-line"><span class="ans">피뢰기 고장 시 개방되어 피뢰기를 대지로부터 분리</span></p>
    </div>
    <div class="q">
      <div class="q-num">226.</div><hr class="q-hline">
      <p class="q-text">BIL이란 무엇인가?</p>
      <p class="ans-line"><span class="ans">기준충격절연강도</span></p>
    </div>
    <div class="q">
      <div class="q-num">227.</div><hr class="q-hline">
      <p class="q-text">전력계통의 절연협조에 대하여 그 의미를 상세히 설명하시오.</p>
      <p class="ans-line"><span class="ans">계통 내의 각 기기, 기구 및 애자 등 상호 간에 적정한 절연 강도를 지니게 함으로써 계통을 경제적으로 설계할 수 있게 한 것</span></p>
    </div>
    <div class="q">
      <div class="q-num">228.</div><hr class="q-hline">
      <p class="q-text">선로애자, 결합콘덴서, 피뢰기, 변압기에 대한 기준 충격 절연강도를 비교하여 절연협조가 어떻게 되어야 하는지를 설명하시오.</p>
      <p class="ans-line"><span class="ans">선로애자 &gt; 결합콘덴서 &gt; 변압기 &gt; 피뢰기</span></p>
      <!--IMG:p097_diag228-->
      <p class="q-text" style="font-size:8.5pt;text-align:center;">$154[kV]$ 송전계통의 절연협조</p>
      <p class="ans-line" style="font-size:8.5pt;"><span class="ans">선로애자 $1030[kV]$ &gt; 결합콘덴서 $900[kV]$ &gt; 기기부싱 $825[kV]$ &gt; 변압기 $750[kV]$ &gt; 피뢰기 $460[kV]$</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 97</div>
</div>

<!-- ===== p.98 229~232 ===== -->
<div class="page" id="page-098">
  <div class="day-tag abs">단답비급 DAY 8</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">229.</div><hr class="q-hline">
      <p class="q-text">LA의 제1보호대상은 무엇인가?</p>
      <p class="ans-line"><span class="ans">변압기</span></p>
    </div>
    <div class="q">
      <div class="q-num">230.</div><hr class="q-hline">
      <p class="q-text">피뢰기와 같은 구조로 되어 있으나 적용 전압 범위만을 조정하여 적용시키는 일종의 옥내 피뢰기로써 선로에 발생할 수 있는 개폐 서지, 순간 과도전압 등의 이상전압이 2차 기기에 악영향을 주는 것을 막기 위해 설치하는 것으로 대부분 큐비클에 내장 설치되어 건식류의 변압기나 기기계통을 보호하는 것은 어떤 것인가?</p>
      <p class="ans-line"><span class="ans">서지흡수기(Surge Absorber)</span></p>
    </div>
    <div class="q">
      <div class="q-num">231.</div><hr class="q-hline">
      <p class="q-text">다음은 전압등급 $3[kV]$인 SA의 시설 적용을 나타낸 표이다. 빈칸에 적용 또는 불필요를 구분하여 쓰시오.</p>
      <table class="tbl">
        <tr><th>차단기 종류</th><th>전동기</th><th colspan="3">변압기</th><th>콘덴서</th></tr>
        <tr><th></th><th></th><th>유입식</th><th>몰드식</th><th>건식</th><th></th></tr>
        <tr><td>VCB</td><td><span class="ans">적용</span></td><td><span class="ans">불필요</span></td><td><span class="ans">적용</span></td><td><span class="ans">적용</span></td><td><span class="ans">불필요</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">232.</div><hr class="q-hline">
      <p class="q-text">VCB를 설치하고 몰드변압기를 사용할 때 보호기기의 명칭과 설치위치를 쓰시오.</p>
      <p class="ans-line">[명칭] <span class="ans">서지 흡수기</span></p>
      <p class="ans-line">[설치위치] <span class="ans">진공 차단기 2차측과 몰드형 변압기 1차측 사이에 설치</span></p>
    </div>
  </div>
  <div class="brand-l abs">98 • 전기치트키</div>
</div>

<!-- ===== p.99 memo ===== -->
<div class="page" id="page-099">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 99</div>
</div>

<!-- ===== p.100 DAY 9 ===== -->
<div class="page" id="page-100">
  <div class="day-banner abs">DAY 9</div>
  <div class="topic-box abs" style="line-height:1.9;">부하특성<br>계전기<br>수변전설비 I</div>
</div>
<!-- ===== p.101 233~237 ===== -->
<div class="page" id="page-101">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">부하특성</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">233.</div><hr class="q-hline">
      <p class="q-text">수용률의 의미를 쓰시오.</p>
      <p class="ans-line">수용설비가 <span class="ans">동시에 사용</span>되는 정도를 나타낸다.</p>
    </div>
    <div class="q">
      <div class="q-num">234.</div><hr class="q-hline">
      <p class="q-text">수용률의 정의를 쓰시오.</p>
      <p class="ans-line"><span class="ans">최대수요전력</span>과 <span class="ans">설비용량</span>과의 <span class="ans">비</span></p>
      <p class="ans-line">$\text{수용률} = \dfrac{\text{최대수요전력}}{\text{부하설비용량}} \times 100\ [\%]$</p>
    </div>
    <div class="q">
      <div class="q-num">235.</div><hr class="q-hline">
      <p class="q-text">어떤 기간 중에 수용설비의 최대수요전력[$kW$]과 설비용량의 합[$kW$]의 비를 나타내는 말은 무엇인가?</p>
      <p class="ans-line"><span class="ans">수용률</span></p>
    </div>
    <div class="q">
      <div class="q-num">236.</div><hr class="q-hline">
      <p class="q-text">부등률의 의미를 쓰시오.</p>
      <p class="ans-line">각 부하가 <span class="ans">최대전력</span>을 나타내는 <span class="ans">시간대</span>가 각각 <span class="ans">다른 정도</span></p>
    </div>
    <div class="q">
      <div class="q-num">237.</div><hr class="q-hline">
      <p class="q-text">부등률의 정의를 쓰시오.</p>
      <p class="ans-line">각 부하군의 <span class="ans">최대수요전력의 합</span>과 <span class="ans">합성최대수요전력</span>에 대한 <span class="ans">비</span></p>
      <p class="ans-line">$\text{부등률} = \dfrac{\text{각각 최대수요전력의 합계}}{\text{합성 최대수요전력}} \geq 1$</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 101</div>
</div>

<!-- ===== p.102 238~242 ===== -->
<div class="page" id="page-102">
  <div class="day-tag abs">단답비급 DAY 9</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">238.</div><hr class="q-hline">
      <p class="q-text">부등률이 크다는 것은 어떤 것을 의미하는가?</p>
      <p class="ans-line"><span class="ans">최대수요전력을 일으키는 기기의 사용 시간대가 서로 다르다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">239.</div><hr class="q-hline">
      <p class="q-text">부하율의 의미를 쓰시오.</p>
      <p class="ans-line"><span class="ans">어떤 기간 중 부하의 변동 정도를 나타내는 것</span></p>
    </div>
    <div class="q">
      <div class="q-num">240.</div><hr class="q-hline">
      <p class="q-text">부하율의 정의를 쓰시오.</p>
      <p class="ans-line"><span class="ans">공급 설비가 얼마나 유효하게 사용되고 있는지를 나타낸다.</span></p>
      <p class="ans-line">$\text{부하율} = \dfrac{\text{평균수요전력}}{\text{최대수요전력}} \times 100\ [\%]$</p>
    </div>
    <div class="q">
      <div class="q-num">241.</div><hr class="q-hline">
      <p class="q-text">부하율이 적다는 것은 무엇을 의미하는지 2가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">공급설비를 유효하게 사용하지 못한다.</span></p>
      <p class="ans-line">② <span class="ans">평균수요전력과 최대수요전력과의 차가 커지게 되므로 부하설비의 가동률이 저하된다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">242.</div><hr class="q-hline">
      <p class="q-text">부하의 최대수요전력(Peak Power)을 억제하는 방법 3가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">부하의 피크 컷(Peak Cut) 제어</span></p>
      <p class="ans-line">② <span class="ans">부하의 피크 시프트(Peak Shift) 제어</span></p>
      <p class="ans-line">③ <span class="ans">자가용 발전설비 가동에 의한 피크 제어</span></p>
    </div>
  </div>
  <div class="brand-l abs">102 • 전기치트키</div>
</div>

<!-- ===== p.103 243~244 ===== -->
<div class="page" id="page-103">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">계전기</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">243.</div><hr class="q-hline">
      <p class="q-text">다음 각 계전기의 이름을 작성하시오.</p>
      <p class="ans-line">(1) OCR : <span class="ans">과전류 계전기</span> &nbsp; (2) OVR : <span class="ans">과전압 계전기</span></p>
      <p class="ans-line">(3) UVR : <span class="ans">부족전압 계전기</span> &nbsp; (4) GR : <span class="ans">지락 계전기</span></p>
      <p class="ans-line">(5) DGR : <span class="ans">방향 지락 계전기</span> &nbsp; (6) PWR : <span class="ans">전력 계전기</span></p>
    </div>
    <div class="q">
      <div class="q-num">244.</div><hr class="q-hline">
      <p class="q-text">계전기의 명칭을 쓰시오.</p>
      <table class="tbl" style="font-size:8.5pt;">
        <tr><th>기구 번호</th><th>기구 명칭</th><th>설명(내용)</th></tr>
        <tr><td>27</td><td><span class="ans">부족전압</span> 계전기</td><td>전압이 부족할 때 동작하는 것</td></tr>
        <tr><td>44</td><td><span class="ans">거리</span> 계전기</td><td>단락 또는 지락 고장점까지의 거리에 의하여 동작하는 것</td></tr>
        <tr><td>47</td><td><span class="ans">결상 또는 역상</span> 계전기</td><td>결상 또는 역상 전압일 때 동작하는 것</td></tr>
        <tr><td>50</td><td><span class="ans">선택 지락</span> 계전기 또는 <span class="ans">선택 단락</span> 계전기</td><td>단락 또는 지락회로를 선택하는 것</td></tr>
        <tr><td>51</td><td><span class="ans">과전류</span> 계전기 또는 <span class="ans">지락 과전류</span> 계전기</td><td>과전류 또는 지락과전류로 동작하는 것</td></tr>
        <tr><td>52</td><td><span class="ans">교류 차단기</span></td><td>회로를 차단하는 것</td></tr>
        <tr><td>59</td><td><span class="ans">과전압</span> 계전기</td><td>과전압으로 동작하는 것</td></tr>
        <tr><td>64</td><td><span class="ans">지락 과전압</span> 계전기</td><td>지락을 전압에 의하여 검출하는 것</td></tr>
        <tr><td>67</td><td><span class="ans">지락 방향</span> 계전기</td><td>지락 방향에 의하여 동작하는 것</td></tr>
        <tr><td>87</td><td><span class="ans">비율 차동</span> 계전기</td><td>단락 또는 지락차전류에 의하여 동작하는 것</td></tr>
      </table>
      <p style="font-size:8pt;margin-top:4px;">※ 87T : 주변압기 차동계전기, 87G : 발전기용 차동계전기</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 103</div>
</div>

<!-- ===== p.104 245~248 ===== -->
<div class="page" id="page-104">
  <div class="day-tag abs">단답비급 DAY 9</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">245.</div><hr class="q-hline">
      <p class="q-text">다음 계전기의 역할을 쓰시오.</p>
      <p class="ans-line">1. <span class="ans">과전류 계전기</span> : 설정값보다 큰 전류가 흐르면 동작</p>
      <p class="ans-line">2. <span class="ans">과전압 계전기</span> : 설정값보다 큰 전압이 인가되면 동작</p>
      <p class="ans-line">3. <span class="ans">부족전압 계전기</span> : 설정값보다 낮은 전압이 인가되면 동작</p>
    </div>
    <div class="q">
      <div class="q-num">246.</div><hr class="q-hline">
      <p class="q-text">전류 차동 계전 방식에 대하여 설명하시오.</p>
      <p class="ans-line"><span class="ans">모선의 각 회로에 CT를 설치하고 과전류 계전기를 설치하여, 고장 시 CT 2차측에 흐르는 전류와 유입하는 전류의 차가 서로 달라지는 것을 이용해서 고장 검출을 하는 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">247.</div><hr class="q-hline">
      <p class="q-text">전압 차동 계전 방식에 대하여 설명하시오.</p>
      <p class="ans-line"><span class="ans">각 회로의 CT 2차측 회로를 병렬로 연결하고 임피던스가 큰 전압 계전기를 접속하여, 고장 시 계전기에 큰 전압이 인가되어 동작하는 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">248.</div><hr class="q-hline">
      <p class="q-text">위상 비교 계전 방식에 대하여 설명하시오.</p>
      <p class="ans-line"><span class="ans">모선에 접속된 각 회선의 전류 위상을 비교함으로써 모선 내 고장인지 외 고장인지를 판별하는 방식</span></p>
    </div>
  </div>
  <div class="brand-l abs">104 • 전기치트키</div>
</div>

<!-- ===== p.105 249~252 ===== -->
<div class="page" id="page-105">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">249.</div><hr class="q-hline">
      <p class="q-text">방향 비교 계전 방식에 대하여 설명하시오.</p>
      <p class="ans-line"><span class="ans">모선에 접속된 각 회선의 방향 계전기(또는 거리 계전기)를 이용하여 어느 회선으로부터 고장점의 방향이 모선 쪽인지 아니면 모선 반대 방향인지를 판정하는 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">250.</div><hr class="q-hline">
      <p class="q-text">전력설비 점검 시 보호계전 계통의 보호계전기 오동작 원인 3가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">보호계전기의 결함</span></p>
      <p class="ans-line">② <span class="ans">변류기의 포화</span></p>
      <p class="ans-line">③ <span class="ans">개폐기의 개폐 서지</span></p>
    </div>
    <div class="q">
      <div class="q-num">251.</div><hr class="q-hline">
      <p class="q-text">아날로그형 계전기에 비교할 때 디지털형 계전기의 장점 5가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">고성능, 다기능화</span> 가능</p>
      <p class="ans-line">② <span class="ans">소형화</span> 할 수 있다.</p>
      <p class="ans-line">③ <span class="ans">신뢰도</span>가 높다.</p>
      <p class="ans-line">④ <span class="ans">융통성</span>이 좋다.</p>
      <p class="ans-line">⑤ <span class="ans">보수 점검</span>이 용이하다.</p>
    </div>
    <div class="q">
      <div class="q-num">252.</div><hr class="q-hline">
      <p class="q-text">보호계전기의 기억작용(Memory Action)이란 무엇인지 설명하시오.</p>
      <p class="ans-line"><span class="ans">계전기의 입력이 급변했을 때 변화 전의 전압을 계전기에 일정 시간 동안 잔류시키게 하는 것</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 105</div>
</div>

<!-- ===== p.106 253~255 ===== -->
<div class="page" id="page-106">
  <div class="day-tag abs">단답비급 DAY 9</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">253.</div><hr class="q-hline">
      <p class="q-text">지락사고 시 계전기가 동작하기 위하여 영상전류를 검출하는 방법 3가지를 서술하시오.</p>
      <p class="ans-line">① <span class="ans">영상변류기(ZCT)</span>에 의한 검출</p>
      <p class="ans-line">② <span class="ans">Y결선의 잔류회로</span>에 의한 검출</p>
      <p class="ans-line">③ <span class="ans">3권선 변류기</span>를 이용한 검출</p>
    </div>
    <div class="q">
      <div class="q-num">254.</div><hr class="q-hline">
      <p class="q-text">다음 상태에서 영상변류기(ZCT)의 영상전류 검출에 대해 설명하시오.</p>
      <p class="ans-line">1. 정상상태(평형부하) : 영상전류가 <span class="ans">검출되지 않는다.</span></p>
      <p class="ans-line">2. 지락상태 : 영상전류가 <span class="ans">검출된다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">255.</div><hr class="q-hline">
      <p class="q-text">고압 전동기의 조작용 배전반에는 어떤 계전기를 설치하는 것이 가장 적당한가?</p>
      <p class="ans-line"><span class="ans">과부하 보호 계전기, 결상 보호 계전기</span></p>
    </div>
  </div>
  <div class="brand-l abs">106 • 전기치트키</div>
</div>

<!-- ===== p.107 256 ===== -->
<div class="page" id="page-107">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">수변전 설비 1</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">256.</div><hr class="q-hline">
      <p class="q-text">다음 설비들의 명칭과 용도를 쓰시오.</p>
      <table class="tbl" style="font-size:7.5pt;">
        <tr><th>기호</th><th>명칭</th><th>용도</th></tr>
        <tr><td>MOF</td><td><span class="ans">전력수급용 계기용 변성기</span></td><td><span class="ans">고전압 대전류</span>를 <span class="ans">저전압 소전류</span>로 변성하여 <span class="ans">전력량계에 공급</span></td></tr>
        <tr><td>PT</td><td><span class="ans">계기용 변압기</span></td><td><span class="ans">고전압</span>을 <span class="ans">저전압</span>으로 변성</td></tr>
        <tr><td>CT</td><td><span class="ans">계기용 변류기</span></td><td><span class="ans">대전류</span>를 <span class="ans">소전류</span>로 변성</td></tr>
        <tr><td>ZCT</td><td><span class="ans">영상 변류기</span></td><td>지락사고 시 <span class="ans">영상전류 검출</span></td></tr>
        <tr><td>VS</td><td><span class="ans">전압계용 전환개폐기</span></td><td><span class="ans">1대의 전압계</span>로 <span class="ans">3상 각 상의 전압</span>을 읽기 위한 개폐기</td></tr>
        <tr><td>AS</td><td><span class="ans">전류계용 전환개폐기</span></td><td><span class="ans">1대의 전류계</span>로 <span class="ans">3상 각 상의 전류</span>를 읽기 위한 개폐기</td></tr>
        <tr><td>CB</td><td><span class="ans">차단기</span></td><td><span class="ans">부하전류 개폐</span> 및 <span class="ans">고장전류 차단</span>을 하기 위한 장치</td></tr>
        <tr><td>OCB</td><td><span class="ans">유입 차단기</span></td><td><span class="ans">부하전류 개폐</span> 및 <span class="ans">고장전류 차단</span></td></tr>
        <tr><td>DS</td><td><span class="ans">단로기</span></td><td><span class="ans">무부하 전류 개폐</span></td></tr>
        <tr><td>PF</td><td><span class="ans">전력용 퓨즈</span></td><td><span class="ans">부하전류 통전, 단락전류 차단</span></td></tr>
        <tr><td>OCR</td><td><span class="ans">과전류 계전기</span></td><td><span class="ans">정격전류 이상</span>이 흐르면 <span class="ans">동작</span></td></tr>
        <tr><td>GR</td><td><span class="ans">지락 계전기</span></td><td>사고 발생 시 <span class="ans">지락전류에 의해 동작</span></td></tr>
        <tr><td>SGR</td><td><span class="ans">선택 지락 계전기</span></td><td><span class="ans">다회선 배전선로</span>에서 지락사고 시 <span class="ans">지락 회선을 선택하여 차단</span></td></tr>
        <tr><td>LA</td><td><span class="ans">피뢰기</span></td><td><span class="ans">이상전압</span>을 <span class="ans">대지로 방전</span>하고, <span class="ans">속류</span>를 <span class="ans">차단</span></td></tr>
        <tr><td>CH</td><td><span class="ans">케이블 헤드</span></td><td>수변전계통에서 <span class="ans">가공 전선로</span>와 <span class="ans">지중 전선로</span>를 <span class="ans">접속</span>하며 단말 및 케이블 <span class="ans">보호</span>용도</td></tr>
        <tr><td>SC</td><td><span class="ans">전력용 콘덴서</span></td><td>부하의 <span class="ans">역률</span>을 <span class="ans">개선</span>하기 위하여 사용</td></tr>
        <tr><td>TC</td><td><span class="ans">트립 코일</span></td><td>보호 <span class="ans">계전기 신호</span>에 의해 <span class="ans">차단기 개로</span></td></tr>
        <tr><td>CLR</td><td><span class="ans">전류 제한 저항기</span></td><td><span class="ans">단락전류 제한</span></td></tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 107</div>
</div>

<!-- ===== p.108 257 ===== -->
<div class="page" id="page-108">
  <div class="day-tag abs">단답비급 DAY 9</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">257.</div><hr class="q-hline">
      <p class="q-text">그림은 큐비클식 고압 수전반을 표시하고 있다.</p>
      <!--IMG:p108_cubicle_l--> <!--IMG:p108_cubicle_r-->
      <p class="q-text">(1) ⑧번 기기의 명칭을 우리말로 쓰시오.</p>
      <p class="ans-line"><span class="ans">전력용 콘덴서</span></p>
      <p class="q-text">(2) ⑧번 기기의 명칭은 진상용 콘덴서로서 정격은 $3\phi$ $300[kVA]$이다. 이때 진상용 콘덴서 용량은 수전설비 용량에 포함되어야 하는지의 여부를 밝히고 만약 포함된다면 몇 $[kVA]$가 포함되는지를 밝히시오.</p>
      <p class="ans-line"><span class="ans">포함되지 않는다.</span></p>
      <p class="q-text">(3) ⑤번의 CH는 무슨 뜻인지 명칭을 기입하시오.</p>
      <p class="ans-line"><span class="ans">케이블 헤드</span></p>
    </div>
  </div>
  <div class="brand-l abs">108 • 전기치트키</div>
</div>

<!-- ===== p.109 258~260 ===== -->
<div class="page" id="page-109">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">258.</div><hr class="q-hline">
      <p class="q-text">다음 그림과 같이 영상변류기를 당해 케이블에 설치하는 경우의 케이블 차폐층의 접지선은 어떻게 시설하는 것이 알맞은가? 접지선을 추가로 그리시오.</p>
      <!--IMG:p109_q258_diag-->
      <p class="ans-line"><span class="ans">관통하여 접지한다</span></p>
    </div>
    <div class="q">
      <div class="q-num">259.</div><hr class="q-hline">
      <p class="q-text">분류리액터(S.R)의 설치 목적은 무엇인가?</p>
      <p class="ans-line"><span class="ans">페란티 현상 방지</span></p>
    </div>
    <div class="q">
      <div class="q-num">260.</div><hr class="q-hline">
      <p class="q-text">다음 리액터에 대한 명칭을 쓰시오.</p>
      <table class="tbl">
        <tr><th>기능</th><th>명칭</th></tr>
        <tr><td>단락전류 제한</td><td><span class="ans">한류 리액터</span></td></tr>
        <tr><td>페란티 현상 방지</td><td><span class="ans">분로 리액터</span></td></tr>
        <tr><td>변압기 중성점 접지 소호</td><td><span class="ans">소호 리액터</span></td></tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 109</div>
</div>

<!-- ===== p.110 261~263 ===== -->
<div class="page" id="page-110">
  <div class="day-tag abs">단답비급 DAY 9</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">261.</div><hr class="q-hline">
      <p class="q-text">$22.9[kV]$, $1{,}000[kVA]$ 폐쇄형 큐비클식 변전실을 수변전실에 하려고 한다. 다음 물음에 답하시오.</p>
      <p class="q-text">(1) 변전실의 유효높이는 몇 $[m]$인가?</p>
      <p class="ans-line"><span class="ans">$4.5[m]$</span></p>
      <p class="q-text">(2) 추정 면적은 몇 $[m^2]$인가? (단, 추정계수는 $1.4$이다.)</p>
      <p class="ans-line"><span class="ans">$1.4 \times \sqrt{1000} = 44.27[m^2]$</span></p>
    </div>
    <div class="q">
      <div class="q-num">262.</div><hr class="q-hline">
      <p class="q-text">수전설비의 배전반 등의 최소 유지거리 (단위 : m)</p>
      <table class="tbl">
        <tr><th>기기명</th><th>앞면 또는 조작 계측면</th><th>뒷면 또는 점검면</th><th>열상호간 (점검하는 면)</th><th>기타의 면</th></tr>
        <tr><td>특고압 배전반</td><td><span class="ans">1.5</span></td><td><span class="ans">1.2</span></td><td><span class="ans">2.0</span></td><td>-</td></tr>
        <tr><td>고압 배전반</td><td><span class="ans">1.5</span></td><td><span class="ans">0.6</span></td><td><span class="ans">1.2</span></td><td>-</td></tr>
        <tr><td>저압 배전반</td><td><span class="ans">1.5</span></td><td><span class="ans">0.6</span></td><td><span class="ans">1.2</span></td><td>-</td></tr>
        <tr><td>변압기 등</td><td><span class="ans">0.6</span></td><td><span class="ans">0.6</span></td><td><span class="ans">1.2</span></td><td><span class="ans">0.3</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">263.</div><hr class="q-hline">
      <p class="q-text">수변전 설비에서 에너지 절약을 위한 합리적인 설계방안 5가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">고효율 변압기</span> 채용</p>
      <p class="ans-line">② <span class="ans">전력부하 제어 시스템</span>을 채택</p>
      <p class="ans-line">③ <span class="ans">전력용 콘덴서</span>를 설치하여 역률 개선</p>
      <p class="ans-line">④ <span class="ans">우수한 역률기기</span>의 선정</p>
      <p class="ans-line">⑤ <span class="ans">변압기의 운전대수 제어</span>가 가능하도록 뱅크를 구성하여 효율적인 운전을 통한 손실을 최소화</p>
    </div>
  </div>
  <div class="brand-l abs">110 • 전기치트키</div>
</div>

<!-- ===== p.111 264 ===== -->
<div class="page" id="page-111">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">264.</div><hr class="q-hline">
      <p class="q-text">수변전 설비의 기본설계에 있어서 검토할 주요 사항을 5가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">부하설비 용량의 추정</span></p>
      <p class="ans-line">② <span class="ans">수전전압 및 수전방식</span></p>
      <p class="ans-line">③ <span class="ans">주회로의 결선방식</span></p>
      <p class="ans-line">④ <span class="ans">변전설비의 형식</span></p>
      <p class="ans-line">⑤ <span class="ans">감시 및 제어방식</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 111</div>
</div>

<!-- ===== p.112 DAY 10 ===== -->
<div class="page" id="page-112">
  <div class="day-banner abs">DAY 10</div>
  <div class="topic-box abs" style="line-height:2.0;">수변전설비 2<br>축전지</div>
</div>

<!-- ===== p.113 265~266 ===== -->
<div class="page" id="page-113">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">수변전 설비 2</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">265.</div><hr class="q-hline">
      <p class="q-text">기호, 명칭, 용도 및 역할에 대해 쓰시오.</p>
      <table class="tbl" style="font-size:8.5pt;">
        <tr><th>약호</th><th>명칭</th><th>용도 및 역할</th></tr>
        <tr><td>DS</td><td><span class="ans">단로기</span></td><td><span class="ans">무부하 전류 개폐</span></td></tr>
        <tr><td>PF</td><td><span class="ans">전력퓨즈</span></td><td><span class="ans">부하 전류는 안전하게 통전하고, 사고 전류를 차단</span></td></tr>
        <tr><td>CB</td><td><span class="ans">교류차단기</span></td><td><span class="ans">고장전류 차단 및 부하 개폐</span></td></tr>
        <tr><td>PT</td><td><span class="ans">계기용변압기</span></td><td><span class="ans">고전압을 저전압으로 변성</span></td></tr>
        <tr><td>CT</td><td><span class="ans">변류기</span></td><td><span class="ans">대전류를 소전류로 변성</span></td></tr>
        <tr><td>ZCT</td><td><span class="ans">영상변류기</span></td><td><span class="ans">지락사고 시 영상전류 검출</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">266.</div><hr class="q-hline">
      <p class="q-text">각 심벌에 대한 명칭을 쓰시오.</p>
      <table class="tbl">
        <tr><th>심벌</th><th>명칭</th><th>심벌</th><th>명칭</th></tr>
        <tr><td>LA</td><td><span class="ans">피뢰기</span></td><td>VTT</td><td><span class="ans">전압시험용 단자</span></td></tr>
        <tr><td>PF</td><td><span class="ans">전력퓨즈</span></td><td>CTT</td><td><span class="ans">전류시험용 단자</span></td></tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 113</div>
</div>

<!-- ===== p.114 267~269 ===== -->
<div class="page" id="page-114">
  <div class="day-tag abs">단답비급 DAY 10</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">267.</div><hr class="q-hline">
      <p class="q-text">PF-S형 큐비클은 큐비클의 주차단 장치로서 어떤 종류의 전력퓨즈와 무엇을 조합한 것인가?</p>
      <p class="ans-line">① 전력퓨즈의 종류 : <span class="ans">한류형 퓨즈</span></p>
      <p class="ans-line">② 조합하여 설치하는 것 : <span class="ans">고압 개폐기</span></p>
    </div>
    <div class="q">
      <div class="q-num">268.</div><hr class="q-hline">
      <p class="q-text">각 부분 ①~⑦에 대한 명칭을 쓰고, 보호 기능 구성상 ⑤~⑦의 부분들 검출부, 판정부, 동작부로 나누어 표현하시오.</p>
      <!--IMG:p114_diag268-->
      <p class="ans-line">① <span class="ans">차단기</span> &nbsp; ② <span class="ans">변류기</span> &nbsp; ③ <span class="ans">계기용 변압기</span> &nbsp; ④ <span class="ans">보호용 계전기</span></p>
      <p class="ans-line">⑤ <span class="ans">동작부</span> &nbsp; ⑥ <span class="ans">검출부</span> &nbsp; ⑦ <span class="ans">판정부</span></p>
    </div>
    <div class="q">
      <div class="q-num">269.</div><hr class="q-hline">
      <p class="q-text">ULTC의 구조상의 종류 2가지를 쓰시오.</p>
      <p class="ans-line">① <span class="ans">병렬 전환식</span></p>
      <p class="ans-line">② <span class="ans">단일 전환식</span></p>
    </div>
  </div>
  <div class="brand-l abs">114 • 전기치트키</div>
</div>

<!-- ===== p.115 270 ===== -->
<div class="page" id="page-115">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">270.</div><hr class="q-hline">
      <!--IMG:p115_diag270-->
      <p class="q-text">위 간이 수전 설비 수전실의 전반을 Cubicle Type으로 할 경우 고압반(HV : High voltage)과 저압반(LV : Low voltage)은 몇 개의 면으로 구성되는지 구분하고, 수용되는 기기의 명칭을 쓰시오.</p>
      <table class="tbl">
        <tr><th>구 분</th><th>면수</th><th>수용기기</th></tr>
        <tr><td>고압반</td><td><span class="ans">2</span></td><td><span class="ans">제1면 : ASS, PF, LA, MOF / 제2면 : COS(PF)</span></td></tr>
        <tr><td>저압반</td><td><span class="ans">2</span></td><td><span class="ans">제1면 : TR1, ACB / 제2면 : TR2, MCCB</span></td></tr>
      </table>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 115</div>
</div>

<!-- ===== p.116 271~275 ===== -->
<div class="page" id="page-116">
  <div class="day-tag abs">단답비급 DAY 10</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">271.</div><hr class="q-hline">
      <p class="q-text">$22.9[kV-Y]$용의 LA는 어떤 붙임이 된 것을 사용해야 하는가?</p>
      <p class="ans-line"><span class="ans">Disconnector 또는 Isolator 붙임형</span></p>
    </div>
    <div class="q">
      <div class="q-num">272.</div><hr class="q-hline">
      <p class="q-text">인입선을 지중선으로 시설하는 경우로서 공동주택 등 사고 시 정전 피해가 큰 수전설비 인입선은 예비 지중선을 포함하여 몇 회선으로 시설하는 것이 바람직한가?</p>
      <p class="ans-line"><span class="ans">2회선</span></p>
    </div>
    <div class="q">
      <div class="q-num">273.</div><hr class="q-hline">
      <p class="q-text">$22.9[kV-Y]$ 지중 인입선에는 어떤 케이블을 사용하여야 하는가?</p>
      <p class="ans-line"><span class="ans">CNCV-W 케이블(수밀형) 또는 TR CNCV-W 케이블(트리억제형)</span></p>
    </div>
    <div class="q">
      <div class="q-num">274.</div><hr class="q-hline">
      <p class="q-text">지중인입선의 경우에 전력구·공동구·덕트·건물구내 등 화재의 우려가 있는 장소에서는 어떤 케이블을 사용하는 것이 바람직한가?</p>
      <p class="ans-line"><span class="ans">FR CNCO-W(난연성) 케이블</span></p>
    </div>
    <div class="q">
      <div class="q-num">275.</div><hr class="q-hline">
      <p class="q-text">$300[kVA]$ 이하인 경우는 PF 대신 어떤 것을 사용할 수 있는가? 또 이것의 비대칭 차단전류 용량은 몇 $[kA]$ 이상의 것을 사용하여야 하는가?</p>
      <p class="ans-line"><span class="ans">COS(비대칭 차단전류 $10[kA]$ 이상의 것)</span></p>
    </div>
  </div>
  <div class="brand-l abs">116 • 전기치트키</div>
</div>

<!-- ===== p.117 276~278 ===== -->
<div class="page" id="page-117">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">276.</div><hr class="q-hline">
      <p class="q-text">다음 빈칸에 알맞은 값을 작성하시오.</p>
      <p class="q-text" style="border:1px solid #ccc;border-radius:8px;padding:8px;font-size:9pt;">MOF의 과전류강도는 기기 설치점에서 단락전류에 의하여 계산 적용하되, $22.9[kV]$급으로서 $60[A]$ 이하의 MOF 최소 과전류강도는 전기사업자규격에 의한 (<span class="ans">75</span>)배로 하고, 계산한 값이 75배 이상인 경우에는 (<span class="ans">150</span>)배를 적용하며, $60[A]$ 초과 시 MOF의 과전류강도는 (<span class="ans">40</span>)배로 적용한다.</p>
    </div>
    <div class="q">
      <div class="q-num">277.</div><hr class="q-hline">
      <p class="q-text">교류용 적산전력계의 잠동(creeping) 현상에 대하여 설명하고 잠동을 막기 위한 유효한 방법을 2가지만 쓰시오.</p>
      <p class="ans-line">1. 잠동현상 : 무부하 상태에서 <span class="ans">정격 전압의 $110[\%]$</span>를 인가했을 때 계기의 원판이 <span class="ans">1회전 이상 회전</span>하는 현상</p>
      <p class="ans-line">2. 방지대책 : ① 원판에 작은 <span class="ans">구멍을 뚫는다</span>. ② 원판에 작은 <span class="ans">철편을 붙인다</span>.</p>
    </div>
    <div class="q">
      <div class="q-num">278.</div><hr class="q-hline">
      <p class="q-text">적산전력계가 구비해야 할 특성을 5가지만 쓰시오.</p>
      <p class="ans-line">① 옥내 및 옥외에 <span class="ans">설치가 적당할</span> 것</p>
      <p class="ans-line">② <span class="ans">온도나 주파수</span> 변화에 <span class="ans">보상이 되도록</span> 할 것</p>
      <p class="ans-line">③ <span class="ans">기계적 강도</span>가 클 것</p>
      <p class="ans-line">④ <span class="ans">부하 특성</span>이 좋을 것</p>
      <p class="ans-line">⑤ <span class="ans">과부하 내량</span>이 클 것</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 117</div>
</div>

<!-- ===== p.118 279~282 ===== -->
<div class="page" id="page-118">
  <div class="day-tag abs">단답비급 DAY 10</div>
  <div class="sec-title abs" style="top:72px;">축전지</div>
  <div class="content compact" style="top:108px;">
    <div class="q">
      <div class="q-num">279.</div><hr class="q-hline">
      <p class="q-text">축전지 설비의 구성요소를 4가지로 구분하시오.</p>
      <p class="ans-line">① <span class="ans">축전지</span> &nbsp; ② <span class="ans">충전장치</span> &nbsp; ③ <span class="ans">보안장치</span> &nbsp; ④ <span class="ans">제어장치</span></p>
    </div>
    <div class="q">
      <div class="q-num">280.</div><hr class="q-hline">
      <p class="q-text">정류기가 축전지의 충전에만 사용되지 않고 평상시 다른 직류부하의 전원으로 병렬하여 사용되는 충전방식은 어떤 충전방식인가?</p>
      <p class="ans-line"><span class="ans">부동충전방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">281.</div><hr class="q-hline">
      <p class="q-text">축전지와 부하를 충전기에 병렬로 접속하여 사용하는 충전방식은 어떤 충전방식인가?</p>
      <p class="ans-line"><span class="ans">부동충전방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">282.</div><hr class="q-hline">
      <p class="q-text">그림은 축전지 충전회로이다. 다음 물음에 답하시오.</p>
      <!--IMG:p118_diag282-->
      <p class="q-text">1. 충전방식은?</p>
      <p class="ans-line"><span class="ans">부동충전방식</span></p>
      <p class="q-text">2. 이 방식의 역할(특징)을 쓰시오.</p>
      <p class="ans-line"><span class="ans">평상시에는 정류기가 상용 부하의 전력을 공급하고 축전지의 자기방전을 보충함과 동시에, 상용 전원 정전 시에는 축전지가 부하의 전력을 공급하도록 하는 방식</span></p>
    </div>
  </div>
  <div class="brand-l abs">118 • 전기치트키</div>
</div>

<!-- ===== p.119 283~287 ===== -->
<div class="page" id="page-119">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">283.</div><hr class="q-hline">
      <p class="q-text">균등충전방식에 대해 간단히 설명하시오.</p>
      <p class="ans-line"><span class="ans">각 전해조에서 일어나는 특성 차이를 수정하기 위하여 1~3개월마다 1회, 정전압 충전하여 각 전해조의 용량을 균일화하기 위하여 행하는 충전방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">284.</div><hr class="q-hline">
      <p class="q-text">보통충전방식에 대해 간단히 설명하시오.</p>
      <p class="ans-line"><span class="ans">필요할 때마다 표준 시간율로 소정의 충전을 하는 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">285.</div><hr class="q-hline">
      <p class="q-text">세류충전방식에 대해 간단히 설명하시오.</p>
      <p class="ans-line"><span class="ans">축전지의 자기방전을 보충하기 위하여 부하를 OFF한 상태에서 미소전류로 부동 충전하는 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">286.</div><hr class="q-hline">
      <p class="q-text">급속충전방식에 대해 간단히 설명하시오.</p>
      <p class="ans-line"><span class="ans">짧은 시간에 보통 충전전류의 2~3배의 전류로 충전하는 방식</span></p>
    </div>
    <div class="q">
      <div class="q-num">287.</div><hr class="q-hline">
      <p class="q-text">축전지의 과방전 및 방치상태, 가벼운 sulfation(설페이션) 현상 등이 생겼을 때 기능 회복을 위해 실시하는 충전 방식은?</p>
      <p class="ans-line"><span class="ans">회복충전</span></p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 119</div>
</div>

<!-- ===== p.120 288~291 ===== -->
<div class="page" id="page-120">
  <div class="day-tag abs">단답비급 DAY 10</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">288.</div><hr class="q-hline">
      <p class="q-text">연축전지는 알칼리 축전지를 비교할 때, 알칼리 축전지의 장점 2가지와 단점 1가지를 쓰시오.</p>
      <p class="ans-line">[장점] ① <span class="ans">수명이 길다.</span> ② <span class="ans">진동과 충격에 강하다.</span></p>
      <p class="ans-line">[단점] ③ <span class="ans">공칭전압이 낮다.</span></p>
    </div>
    <div class="q">
      <div class="q-num">289.</div><hr class="q-hline">
      <p class="q-text">알칼리 축전지의 공칭전압은 몇 $[V/\text{cell}]$인가?</p>
      <p class="ans-line"><span class="ans">$1.2$</span></p>
    </div>
    <div class="q">
      <div class="q-num">290.</div><hr class="q-hline">
      <p class="q-text">표의 빈칸에 연축전지와 알칼리 축전지의 특성을 비교하시오.</p>
      <table class="tbl">
        <tr><th>구분</th><th>연축전지</th><th>알칼리 축전지</th></tr>
        <tr><td>공칭전압[$V/\text{cell}$]</td><td><span class="ans">2.0</span></td><td><span class="ans">1.2</span></td></tr>
        <tr><td>과 충·방전에 의한 전기적 강도</td><td><span class="ans">약하다</span></td><td><span class="ans">강하다</span></td></tr>
        <tr><td>수명</td><td><span class="ans">3~5년</span></td><td><span class="ans">10년</span></td></tr>
      </table>
    </div>
    <div class="q">
      <div class="q-num">291.</div><hr class="q-hline">
      <p class="q-text">축전지 용량은 $C = \dfrac{1}{L}KI\ [Ah]$로 계산한다. 공식에서 문자 $L$, $K$, $I$는 무엇을 의미하는지 쓰시오.</p>
      <p class="ans-line">$L$ : <span class="ans">보수율</span></p>
      <p class="ans-line">$K$ : <span class="ans">용량환산 시간 계수</span></p>
      <p class="ans-line">$I$ : <span class="ans">방전전류[$A$]</span></p>
    </div>
  </div>
  <div class="brand-l abs">120 • 전기치트키</div>
</div>
"""
