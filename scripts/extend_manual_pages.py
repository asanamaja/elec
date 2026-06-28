#!/usr/bin/env python3
"""Extend dandap_manual.html: cover/CSS fixes, pages 50-74, diagram crops."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import fitz

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "output" / "dandap_manual.html"
CROPS = ROOT / "assets/images/manual/crops"
PDF = ROOT / "assets/pdf/source.pdf"

CROP_SPECS: dict[int, list[tuple[str, fitz.Rect]]] = {
    59: [("p060_diag126.png", fitz.Rect(70, 220, 530, 480))],
    60: [("p061_diag128.png", fitz.Rect(70, 200, 530, 470))],
    70: [("p071_diag162.png", fitz.Rect(70, 175, 530, 340))],
    72: [("p073_sym168.png", fitz.Rect(85, 125, 175, 210))],
    73: [("p074_diag170.png", fitz.Rect(55, 95, 545, 420))],
}

IMG_STYLE: dict[str, str] = {
    "p060_diag126.png": "max-height:200px",
    "p061_diag128.png": "max-height:200px",
    "p071_diag162.png": "max-height:120px",
    "p073_sym168.png": "max-height:60px;display:inline-block;width:auto",
    "p074_diag170.png": "max-height:240px",
}

PAGE_IMAGES: dict[str, list[str]] = {
    "page-060": ["p060_diag126.png"],
    "page-061": ["p061_diag128.png"],
    "page-071": ["p071_diag162.png"],
    "page-073": ["p073_sym168.png"],
    "page-074": ["p074_diag170.png"],
}

COMPACT_PAGES = {
    "page-050", "page-051", "page-054", "page-064", "page-066", "page-068",
    "page-070", "page-071", "page-072", "page-073",
}

NEW_PAGES = r"""
<!-- ===== p.50 102~105 ===== -->
<div class="page" id="page-050">
  <div class="day-tag abs">단답비급 DAY 5</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">102.</div><hr class="q-hline">
      <p class="q-text">방폭형 전동기에 대하여 설명하시오.</p>
      <p class="ans-line"><span class="ans">폭발성 가스가 있는 곳에서 사용이 적합하도록 제작된 전동기</span></p>
    </div>
    <div class="q">
      <div class="q-num">103.</div><hr class="q-hline">
      <p class="q-text">MCC(Motor Control Center)의 기기 구성에 대한 대표적인 장치를 3가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">기동장치</span></p>
      <p class="ans-line">② <span class="ans">제어 및 보조장치</span></p>
      <p class="ans-line">③ <span class="ans">차단장치</span></p>
    </div>
    <div class="q">
      <div class="q-num">104.</div><hr class="q-hline">
      <p class="q-text">전동기 소손방지를 위한 과부하 보호장치의 종류를 5가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">전동기용 퓨즈</span></p>
      <p class="ans-line">② <span class="ans">열동계전기(Thermal Relay)</span></p>
      <p class="ans-line">③ <span class="ans">전동기 보호용 배선차단기</span></p>
      <p class="ans-line">④ <span class="ans">유도형 계전기</span></p>
      <p class="ans-line">⑤ <span class="ans">정지형 계전기(전자식계전기, 디지털 계전기 등)</span></p>
    </div>
    <div class="q">
      <div class="q-num">105.</div><hr class="q-hline">
      <p class="q-text">전동기용 과부하 보호장치를 설치하지 아니하여도 되는 경우의 예를 5가지만 쓰시오.</p>
      <p class="ans-line">① 전동기의 출력이 <span class="ans">0.2[kW] 이하</span>일 경우</p>
      <p class="ans-line">② 전동기를 운전 중 <span class="ans">상시 취급자가 감시</span>할 수 있는 위치에 시설하는 경우</p>
      <p class="ans-line">③ 전동기의 구조나 부하의 성질로 보아 전동기가 손상될 수 있는 과전류가 생길 우려가 없는 경우</p>
      <p class="ans-line">④ 단상전동기로써 그 전원 측 전로에 시설하는 과전류 차단기의 정격전류가 <span class="ans">16[A](배선차단기는 20[A]) 이하</span>인 경우</p>
      <p class="ans-line">⑤ 전동기 자체에 <span class="ans">유효한 과부하 소손방지장치</span>가 있는 경우</p>
    </div>
  </div>
  <div class="brand-l abs">50 • 전기치트키</div>
</div>

<!-- ===== p.51 106~109 ===== -->
<div class="page" id="page-051">
  <div class="brand abs">전기치트키</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">106.</div><hr class="q-hline">
      <p class="q-text">3상 교류 전동기 보호를 위한 장치의 종류를 5가지만 쓰시오. (단, 과부하 보호는 제외한다.)</p>
      <p class="ans-line">① <span class="ans">단상 보호</span> &nbsp; ② <span class="ans">지락 보호</span> &nbsp; ③ <span class="ans">결상 보호</span></p>
      <p class="ans-line">④ <span class="ans">역상 보호</span> &nbsp; ⑤ <span class="ans">회전자 구속 보호</span></p>
    </div>
    <div class="q">
      <div class="q-num">107.</div><hr class="q-hline">
      <p class="q-text">전동기의 진동이 발생하는 원인을 5가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">회전자의 정적·동적 불평형</span></p>
      <p class="ans-line">② <span class="ans">회전자의 편심</span></p>
      <p class="ans-line">③ <span class="ans">베어링 불량</span></p>
      <p class="ans-line">④ <span class="ans">상대 기기와의 직결 불량 및 설치 불량</span></p>
      <p class="ans-line">⑤ <span class="ans">회전자의 회전 시 변동</span></p>
    </div>
    <div class="q">
      <div class="q-num">108.</div><hr class="q-hline">
      <p class="q-text">전동기 소음을 크게 3가지로 분류하고 각각에 대하여 설명하시오.</p>
      <p class="ans-line">① <span class="ans">기계적 소음</span> : 브러시, 베어링 등에 의한 진동으로 발생</p>
      <p class="ans-line">② <span class="ans">전자적 소음</span> : 철심의 주기적인 전자력에 의해 진동하여 발생</p>
      <p class="ans-line">③ <span class="ans">통풍 소음</span> : 팬의 회전에 따른 공기 마찰, 풍절에 의해 발생</p>
    </div>
    <div class="q">
      <div class="q-num">109.</div><hr class="q-hline">
      <p class="q-text">에너지 절약을 위한 동력설비의 대응방안 중 5가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">고효율 전동기</span> 채용</p>
      <p class="ans-line">② <span class="ans">부하 역률개선</span></p>
      <p class="ans-line">③ <span class="ans">VVVF 시스템</span> 채용</p>
      <p class="ans-line">④ <span class="ans">에너지 절약형 공조기기 system</span> 채택</p>
      <p class="ans-line">⑤ <span class="ans">부하에 맞는 적정용량의 전동기</span> 선정</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 51</div>
</div>

<!-- ===== p.52 110~113 ===== -->
<div class="page" id="page-052">
  <div class="day-tag abs">단답비급 DAY 5</div>
  <div class="sec-title abs" style="top:72px;">발전기</div>
  <div class="content" style="top:108px;">
    <div class="q">
      <div class="q-num">110.</div><hr class="q-hline">
      <p class="q-text">발전기실 위치를 선정할 때 고려해야 할 사항을 4가지만 쓰시오.</p>
      <p class="ans-line">1. <span class="ans">기기의 반입</span>이 용이할 것</p>
      <p class="ans-line">2. <span class="ans">급배기 환기</span>를 충분히 할 수 있을 것</p>
      <p class="ans-line">3. <span class="ans">배기 배출구</span>에 가급적 가까이 위치할 것</p>
      <p class="ans-line">4. <span class="ans">급배수</span>가 용이할 것</p>
    </div>
    <div class="q">
      <div class="q-num">111.</div><hr class="q-hline">
      <p class="q-text">발전기실 건물의 높이를 결정하는 데 반드시 고려해야 할 사항 2가지를 작성하시오.</p>
      <p class="ans-line">1. 발전기의 <span class="ans">설치 및 유지보수</span>가 용이할 것</p>
      <p class="ans-line">2. 발전기 <span class="ans">부속설비</span>의 높이 및 설치 위치</p>
    </div>
    <div class="q">
      <div class="q-num">112.</div><hr class="q-hline">
      <p class="q-text">자가용 전기설비의 중요 검사(시험) 사항을 3가지만 쓰시오.</p>
      <p class="ans-line">① <span class="ans">접지저항</span> 측정 &nbsp; ② <span class="ans">절연저항</span> 측정 &nbsp; ③ <span class="ans">내전압</span> 시험</p>
    </div>
    <div class="q">
      <div class="q-num">113.</div><hr class="q-hline">
      <p class="q-text">비상용 동기발전기의 병렬운전 조건을 4가지 쓰시오.</p>
      <p class="ans-line">1. 기전력의 <span class="ans">크기</span>가 같을 것</p>
      <p class="ans-line">2. 기전력의 <span class="ans">위상</span>이 같을 것</p>
      <p class="ans-line">3. 기전력의 <span class="ans">파형</span>이 같을 것</p>
      <p class="ans-line">4. 기전력의 <span class="ans">주파수</span>가 같을 것</p>
    </div>
  </div>
  <div class="brand-l abs">52 • 전기치트키</div>
</div>

<!-- ===== p.53 114~115 ===== -->
<div class="page" id="page-053">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">114.</div><hr class="q-hline">
      <p class="q-text">자가용 전기 설비에 발전 시설이 구비되어 있을 경우 자가용 수용가에 설치되어야 할 계전기는 어떤 계전기인가? 5가지를 작성하시오.</p>
      <p class="ans-line">1. <span class="ans">과전류 계전기</span></p>
      <p class="ans-line">2. <span class="ans">과전압 계전기</span></p>
      <p class="ans-line">3. <span class="ans">부족전압 계전기</span></p>
      <p class="ans-line">4. <span class="ans">주파수 계전기</span></p>
      <p class="ans-line">5. <span class="ans">비율 차동 계전기</span></p>
    </div>
    <div class="q">
      <div class="q-num">115.</div><hr class="q-hline">
      <p class="q-text">예비전원으로 시설하는 고압 발전기에서 부하에 이르는 전로에는 발전기의 가까운 곳에 반드시 시설되어야 할 것들 4가지를 쓰고, 시설기준(방법 또는 유의점)을 설명하시오.</p>
      <p><b>1. 시설되어야 할 것</b></p>
      <p class="ans-line">1. <span class="ans">개폐기</span> &nbsp; 2. <span class="ans">과전류 차단기</span> &nbsp; 3. <span class="ans">전압계</span> &nbsp; 4. <span class="ans">전류계</span></p>
      <p style="margin-top:4px;"><b>2. 시설방법</b></p>
      <p class="ans-line">1. 각 극에 <span class="ans">개폐기 및 과전류 차단기</span>를 설치할 것.</p>
      <p class="ans-line">2. 전압계는 각 상의 전압을 읽을 수 있도록 시설할 것.</p>
      <p class="ans-line">3. 전류계는 각 선(중성선은 제외한다)의 전류를 읽을 수 있도록 시설할 것.</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 53</div>
</div>

<!-- ===== p.54 116~117 ===== -->
<div class="page" id="page-054">
  <div class="day-tag abs">단답비급 DAY 5</div>
  <div class="content compact">
    <div class="q">
      <div class="q-num">116.</div><hr class="q-hline">
      <p class="q-text">발전기에는 다음의 경우에 자동적으로 이를 전로로부터 차단하는 장치를 시설하여야 한다. 괄호에 알맞은 값을 쓰시오.</p>
      <div class="box" style="font-size:9.3pt;line-height:1.5;">
        <p>가. 발전기에 과전류나 과전압이 생긴 경우</p>
        <p>나. 용량이 ( <span class="ans">① 500</span> ) [kVA] 이상의 발전기를 구동하는 수차의 압유장치의 유압 또는 전동식 가이드밴드 제어장치, 전동식 니이들 제어장치 또는 전동식 디플렉터 제어장치의 전원전압이 현저히 저하한 경우</p>
        <p>다. 용량이 ( <span class="ans">② 100</span> ) [kVA] 이상의 발전기를 구동하는 풍차(風車)의 압유장치의 유압, 압축 공기장치의 공기압 또는 전동식 블레이드 제어장치의 전원전압이 현저히 저하한 경우</p>
        <p>라. 용량이 ( <span class="ans">③ 2,000</span> ) [kVA] 이상인 수차 발전기의 스러스트 베어링의 온도가 현저히 상승한 경우</p>
        <p>마. 용량이 ( <span class="ans">④ 10,000</span> ) [kVA] 이상인 발전기의 내부에 고장이 생긴 경우</p>
        <p>바. 정격출력이 ( <span class="ans">⑤ 10,000</span> ) [kW]를 초과하는 증기터빈은 그 스러스트 베어링이 현저하게 마모되거나 그의 온도가 현저히 상승한 경우</p>
      </div>
    </div>
    <div class="q">
      <div class="q-num">117.</div><hr class="q-hline">
      <p class="q-text">다음 상용전원과 예비전원 운전 시 유의하여야 할 사항이다. ( )안에 알맞은 내용을 쓰시오.</p>
      <div class="box" style="font-size:9.5pt;">
        <p>상용전원과 예비전원 사이에는 병렬운전을 하지 않는 것이 원칙이므로 수전용 차단기와 발전용 차단기 사이에는 전기적 또는 기계적 ( <span class="ans">인터록</span> )을 시설해야 하며 ( <span class="ans">전환 개폐기</span> )를 사용해야 한다.</p>
      </div>
    </div>
  </div>
  <div class="brand-l abs">54 • 전기치트키</div>
</div>

<!-- ===== p.55 118~119 ===== -->
<div class="page" id="page-055">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <div class="q">
      <div class="q-num">118.</div><hr class="q-hline">
      <p class="q-text">동기발전기를 병렬로 접속하여 운전하는 경우에 생기는 <span class="ans">횡류</span> 3가지를 쓰고, 각각의 작용에 대하여 설명하시오.</p>
      <p class="ans-line">1. <span class="ans">무효순환전류</span> : <span class="ans">역률</span>을 변화시켜 <span class="ans">무효전력</span>을 <span class="ans">분담</span>시킴</p>
      <p class="ans-line">2. <span class="ans">동기화 전류</span> : <span class="ans">유효전력</span>을 <span class="ans">발생</span>시켜 <span class="ans">부하전력</span>을 <span class="ans">분담</span>시킴</p>
      <p class="ans-line">3. <span class="ans">고조파 무효순환전류</span> : 권선의 <span class="ans">저항손</span>이 <span class="ans">증가</span>하여 <span class="ans">과열</span>의 원인이 됨</p>
    </div>
    <div class="q">
      <div class="q-num">119.</div><hr class="q-hline">
      <p class="q-text">단락비가 큰 교류 발전기는 일반적으로</p>
      <p class="ans-line">기계의 치수가 ( <span class="ans">크다</span> )</p>
      <p class="ans-line">가격이 ( <span class="ans">높다</span> )</p>
      <p class="ans-line">풍손, 마찰손, 철손이 ( <span class="ans">크다</span> )</p>
      <p class="ans-line">효율은 ( <span class="ans">낮다</span> )</p>
      <p class="ans-line">전압변동률은 ( <span class="ans">작다</span> )</p>
      <p class="ans-line">안정도는 ( <span class="ans">높다</span> )</p>
      <p class="ans-line">자속수는 ( <span class="ans">증가</span> )</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 55</div>
</div>

<!-- ===== p.56 120~121 ===== -->
<div class="page" id="page-056">
  <div class="day-tag abs">단답비급 DAY 5</div>
  <div class="sec-title abs" style="top:72px;font-size:12pt;">태양광</div>
  <div class="content" style="top:108px;">
    <div class="q">
      <div class="q-num">120.</div><hr class="q-hline">
      <p class="q-text">태양광 발전의 장단점은 무엇인가?</p>
      <p><b>[장점 (4가지)]</b></p>
      <p class="ans-line">1. 에너지원이 <span class="ans">청정, 영구적</span></p>
      <p class="ans-line">2. 필요한 장소에서 <span class="ans">필요한 발전량 발전</span> 가능</p>
      <p class="ans-line">3. <span class="ans">유지보수가 용이</span>하며 <span class="ans">무인화</span> 가능</p>
      <p class="ans-line">4. <span class="ans">확산광(산란광)</span>도 이용할 수 있음</p>
      <p style="margin-top:4px;"><b>[단점 (4가지)]</b></p>
      <p class="ans-line">1. 에너지 밀도가 낮아 <span class="ans">큰 설치면적</span> 필요</p>
      <p class="ans-line">2. 흐린 날씨에는 <span class="ans">발전능력 저하</span></p>
      <p class="ans-line">3. 전력생산량이 <span class="ans">지역의 일사량</span>에 의존</p>
      <p class="ans-line">4. 설치비용이 <span class="ans">고가</span>이며 고가임</p>
    </div>
    <div class="q">
      <div class="q-num">121.</div><hr class="q-hline">
      <p class="q-text">연료전지의 특징 3가지를 쓰시오.</p>
      <p class="ans-line">1. <span class="ans">발전효율이 높음</span></p>
      <p class="ans-line">2. <span class="ans">단위출력 당 무게가 적음</span></p>
      <p class="ans-line">3. <span class="ans">환경상 문제가 없어 수용가 근처에 설치</span>할 수 있음</p>
    </div>
  </div>
  <div class="brand-l abs">56 • 전기치트키</div>
</div>

<!-- ===== p.57 memo ===== -->
<div class="page" id="page-057">
  <div class="brand abs">전기치트키</div>
  <div class="content">
    <p class="memo-label">memo</p>
    <hr class="memo-line">
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 57</div>
</div>

<!-- ===== p.58 DAY 6 ===== -->
<div class="page" id="page-058">
  <div class="day-banner abs">DAY 6</div>
  <div class="topic-box abs">변압기</div>
</div>

<!-- ===== p.59 122~124 ===== -->
<div class="page" id="page-059">
  <div class="brand abs">전기치트키</div>
  <div class="sec-title abs">변압기</div>
  <div class="content" style="top:118px;">
    <div class="q">
      <div class="q-num">122.</div><hr class="q-hline">
      <p class="q-text">변압기 병렬운전 조건 4가지를 쓰고, 조건이 맞지 않은 경우 어떤 현상이 나타나는지 쓰시오.</p>
      <p class="ans-line">1. <span class="ans">극성</span>이 같을 것 $\rightarrow$ 큰 <span class="ans">순환전류</span>가 흘러 권선 <span class="ans">소손</span></p>
      <p class="ans-line">2. <span class="ans">정격전압(권수비)</span>이 같을 것 $\rightarrow$ <span class="ans">순환전류</span>가 흘러 권선 <span class="ans">가열</span></p>
      <p class="ans-line">3. <span class="ans">%임피던스</span>가 같을 것 $\rightarrow$ <span class="ans">부하 분담</span>이 <span class="ans">균형</span>을 이루지 못함</p>
      <p class="ans-line">4. <span class="ans">내부저항</span>과 <span class="ans">누설리액턴스</span>의 비가 같을 것 $\rightarrow$ 전류 간에 <span class="ans">위상차</span>가 생겨 <span class="ans">동손</span> 증가</p>
    </div>
    <div class="q">
      <div class="q-num">123.</div><hr class="q-hline">
      <p class="q-text">단락시험, 무부하 시험으로 변압기 효율을 구하는 방법을 간단히 설명하시오.</p>
      <p class="ans-line">1. <span class="ans">단락시험</span>을 통하여 <span class="ans">동손</span> 측정</p>
      <p class="ans-line">2. <span class="ans">무부하시험</span>을 통하여 <span class="ans">철손</span> 측정</p>
      <p class="ans-line">3. 변압기의 효율 $\eta = \dfrac{\text{정격출력}}{\text{정격출력} + \text{동손} + \text{철손}} \times 100$ [%]</p>
    </div>
    <div class="q">
      <div class="q-num">124.</div><hr class="q-hline">
      <p class="q-text">변압기 최대효율 조건을 쓰시오.</p>
      <p class="ans-line">최대효율 조건은 <span class="ans">철손</span>과 <span class="ans">동손</span>이 같을 때이다.</p>
    </div>
  </div>
  <div class="foot-r abs">전기기사 실기 단답비급 • 59</div>
</div>
"""

# Part 2 appended via separate file to keep script manageable
from extend_manual_pages_part2 import PAGES_60_74  # noqa: E402

NEW_PAGES += PAGES_60_74


def recrop_images() -> None:
    doc = fitz.open(PDF)
    CROPS.mkdir(parents=True, exist_ok=True)
    for page_idx, items in CROP_SPECS.items():
        page = doc[page_idx]
        for name, rect in items:
            pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), clip=rect, alpha=False)
            pix.save(str(CROPS / name))
            print(f"cropped {name}")


def patch_css(html: str) -> str:
    if ".content.compact" not in html:
        html = html.replace(
            "    .content { position: absolute; left: 72px; right: 52px; top: 118px; }",
            "    .content { position: absolute; left: 72px; right: 52px; top: 118px; padding-bottom: 54px; }\n"
            "    .content.compact { font-size: 9.6pt; line-height: 1.48; }\n"
            "    .content.compact .q { margin-bottom: 14px; }\n"
            "    .content.compact .box { font-size: 9pt; padding: 6px 8px; }",
        )
    if "toc-row" in html and "margin-bottom: 8px" not in html:
        html = html.replace(
            "margin-bottom: 10px; font-size: 9pt; line-height: 1.5;",
            "margin-bottom: 8px; font-size: 8.7pt; line-height: 1.45;",
        )
        html = html.replace(
            "padding: 28px 18px 32px 18px;",
            "padding: 26px 16px 36px 16px;",
        )
    return html


def patch_cover(html: str) -> str:
    html = re.sub(
        r'\s*<div class="vtext sub-v sub-v1">[^<]*</div>\s*'
        r'<div class="vtext sub-v sub-v2">[^<]*</div>\s*',
        "\n",
        html,
    )
    html = html.replace(
        '<span id="pg-info">p.1–49 (DAY1~5 진행중) · 직접 전사</span>',
        '<span id="pg-info">p.1–74 (DAY1~6 진행중) · 직접 전사</span>',
    )
    return html


def insert_pages(html: str) -> str:
    marker = "\n</div>\n\n<script defer src="
    if marker not in html:
        raise ValueError("insert marker not found")
    if 'id="page-050"' in html:
        print("pages 50+ already present, skipping insert")
        return html
    return html.replace(marker, NEW_PAGES + marker, 1)


def inject_diagrams(html: str) -> str:
    inserts = {
        "page-060": (
            '<p class="q-text">그림은 구내에 설치할 단상변압기의 무부하 시험방법이다. 이 도면을 보고 다음 각 물음에 답하시오.</p>',
            '<p class="q-text">그림은 구내에 설치할 단상변압기의 무부하 시험방법이다. 이 도면을 보고 다음 각 물음에 답하시오.</p>\n'
            '      <img class="diag" src="../assets/images/manual/crops/p060_diag126.png" '
            'style="max-height:200px;" alt="">',
        ),
        "page-061": (
            '<p class="q-text">변압기 단락시험을 하고자 한다. 그림을 보고 다음 각 물음에 답하시오.</p>',
            '<p class="q-text">변압기 단락시험을 하고자 한다. 그림을 보고 다음 각 물음에 답하시오.</p>\n'
            '      <img class="diag" src="../assets/images/manual/crops/p061_diag128.png" '
            'style="max-height:200px;" alt="">',
        ),
        "page-071": (
            '<p class="q-text">그림과 같이 부하를 운전 중인 상태에서 변류기의 2차측의 전류계를 교체할 때에는 어떠한 순서로 작업을 하여야 하는지 쓰시오. (단, K와 L은 변류기 1차 단자, k와 l은 변류기 2차 단자, a와 b는 전류계 단자이다.)</p>',
            '<p class="q-text">그림과 같이 부하를 운전 중인 상태에서 변류기의 2차측의 전류계를 교체할 때에는 어떠한 순서로 작업을 하여야 하는지 쓰시오. (단, K와 L은 변류기 1차 단자, k와 l은 변류기 2차 단자, a와 b는 전류계 단자이다.)</p>\n'
            '      <img class="diag" src="../assets/images/manual/crops/p071_diag162.png" '
            'style="max-height:120px;" alt="">',
        ),
        "page-073": (
            '<p class="q-text">이 그림기호의 정확한 명칭을 쓰시오.</p>',
            '<img class="diag" src="../assets/images/manual/crops/p073_sym168.png" '
            'style="max-height:60px;display:inline-block;width:auto;" alt="">\n'
            '      <p class="q-text">이 그림기호의 정확한 명칭을 쓰시오.</p>',
        ),
        "page-074": (
            '<p class="q-text">다음은 모선보호 계전방식을 도면화한 것이다. 이 도면을 보고 다음 각 물음에 답하시오.</p>',
            '<p class="q-text">다음은 모선보호 계전방식을 도면화한 것이다. 이 도면을 보고 다음 각 물음에 답하시오.</p>\n'
            '      <img class="diag" src="../assets/images/manual/crops/p074_diag170.png" '
            'style="max-height:240px;" alt="">',
        ),
    }
    for page_id, (old, new) in inserts.items():
        pat = rf'(<div class="page" id="{page_id}">.*?){re.escape(old)}'
        html, n = re.subn(pat, rf"\1{new}", html, count=1, flags=re.S)
        if n != 1:
            print(f"warn: diagram insert for {page_id}: {n} replacements")
    return html


def main() -> None:
    print("Cropping new diagrams...")
    recrop_images()

    html = HTML.read_text(encoding="utf-8")
    html = patch_css(html)
    html = patch_cover(html)
    html = insert_pages(html)
    html = inject_diagrams(html)

    HTML.write_text(html, encoding="utf-8")
    print("Embedding images...")
    subprocess.run(["python3", str(ROOT / "scripts/embed_manual_assets.py")], check=True)

    final = HTML.read_text(encoding="utf-8")
    assert final.rstrip().endswith("</html>"), "HTML truncated!"
    n_pages = len(re.findall(r'id="page-\d+"', final))
    n_b64 = len(re.findall(r"data:image/png;base64,", final))
    print(f"Done: {HTML.stat().st_size // 1024}KB, {n_pages} pages, {n_b64} embedded images")


if __name__ == "__main__":
    main()
