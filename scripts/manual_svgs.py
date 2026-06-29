#!/usr/bin/env python3
"""Inline SVG / HTML for manual slots that are tables (not photos)."""
from __future__ import annotations

TABLE_STYLE = (
    "width:100%;border-collapse:collapse;font-size:8.5pt;margin:8px 0;"
    "table-layout:fixed;"
)
CELL = "border:1px solid #888;padding:4px 3px;text-align:center;vertical-align:middle;"
TH = CELL + "background:#e8e8e8;font-weight:700;"


def svg_p029_tbl053() -> str:
    return f"""<table class="tbl manual-table" style="{TABLE_STYLE}">
<thead>
<tr><th style="{TH}" rowspan="2">전선의 시설장소</th>
<th style="{TH}" colspan="2">옥내</th><th style="{TH}" colspan="2">옥측·옥외</th></tr>
<tr><th style="{TH}">노출장소</th><th style="{TH}">은폐장소</th>
<th style="{TH}">노출장소</th><th style="{TH}">은폐장소</th></tr>
</thead>
<tbody>
<tr><td style="{CELL}">금속관 공사</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">△</td><td style="{CELL}">×</td></tr>
<tr><td style="{CELL}">합성수지관 공사</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">△</td><td style="{CELL}">×</td></tr>
<tr><td style="{CELL}">케이블 공사</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">△</td><td style="{CELL}">×</td></tr>
<tr><td style="{CELL}">버스덕트 공사</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">×</td><td style="{CELL}">×</td></tr>
<tr><td style="{CELL}">캡타이어 케이블 공사</td><td style="{CELL}">○</td><td style="{CELL}">△</td><td style="{CELL}">×</td><td style="{CELL}">×</td></tr>
</tbody></table>"""


def svg_p029_tbl054() -> str:
    moist = "습기가 많은 장소 또는 물기가 있는 장소"
    return f"""<table class="tbl manual-table" style="{TABLE_STYLE}">
<thead>
<tr><th style="{TH}" rowspan="4">공사 종류</th>
<th style="{TH}" colspan="6">옥내</th><th style="{TH}" colspan="2">옥측·옥외</th></tr>
<tr><th style="{TH}" colspan="2">노출 장소</th><th style="{TH}" colspan="4">은폐 장소</th>
<th style="{TH}" rowspan="3">우선 내</th><th style="{TH}" rowspan="3">우선 외</th></tr>
<tr><th style="{TH}" rowspan="2">건조한 장소</th><th style="{TH}" rowspan="2">{moist}</th>
<th style="{TH}" colspan="2">점검 가능한 장소</th><th style="{TH}" colspan="2">점검 불가능한 장소</th></tr>
<tr><th style="{TH}">건조한 장소</th><th style="{TH}">{moist}</th>
<th style="{TH}">건조한 장소</th><th style="{TH}">{moist}</th></tr>
</thead>
<tbody>
<tr><td style="{CELL}"><span class="ans">케이블 공사</span></td>
<td style="{CELL}"><span class="ans">○</span></td><td style="{CELL}"><span class="ans">○</span></td>
<td style="{CELL}"><span class="ans">○</span></td><td style="{CELL}"><span class="ans">○</span></td>
<td style="{CELL}"><span class="ans">○</span></td><td style="{CELL}"><span class="ans">○</span></td>
<td style="{CELL}"><span class="ans">○</span></td><td style="{CELL}"><span class="ans">○</span></td></tr>
</tbody></table>"""


def svg_p041_tbl081() -> str:
    return f"""<table class="tbl manual-table" style="{TABLE_STYLE}">
<thead>
<tr><th style="{TH}">기호</th><th style="{TH}">명칭</th><th style="{TH}">기호</th><th style="{TH}">명칭</th></tr>
</thead>
<tbody>
<tr><td style="{CELL}">○</td><td style="{CELL}">백열전등</td><td style="{CELL}">◎</td><td style="{CELL}">형광등</td></tr>
<tr><td style="{CELL}">□</td><td style="{CELL}">투광등</td><td style="{CELL}">◇</td><td style="{CELL}">옥외등</td></tr>
<tr><td style="{CELL}">△</td><td style="{CELL}">수은등</td><td style="{CELL}">▽</td><td style="{CELL}">네온등</td></tr>
</tbody></table>"""


def svg_p044_tbl089() -> str:
    return f"""<table class="tbl manual-table" style="{TABLE_STYLE}">
<thead><tr>
<th style="{TH}">기호</th><th style="{TH}">명칭</th>
<th style="{TH}">기호</th><th style="{TH}">명칭</th>
<th style="{TH}">기호</th><th style="{TH}">명칭</th>
</tr></thead>
<tbody>
<tr><td style="{CELL}">0</td><td style="{CELL}">일반용</td>
<td style="{CELL}">1</td><td style="{CELL}">난연성</td>
<td style="{CELL}">2</td><td style="{CELL}">내열성</td></tr>
</tbody></table>"""


def svg_p045_tbl092() -> str:
    return f"""<table class="tbl manual-table" style="{TABLE_STYLE}">
<thead>
<tr><th style="{TH}" rowspan="2">전동기 용량</th>
<th style="{TH}" colspan="4">기동방법</th></tr>
<tr><th style="{TH}">직입</th><th style="{TH}">Y-△</th><th style="{TH}">리액터</th><th style="{TH}">기동보상기</th></tr>
</thead>
<tbody>
<tr><td style="{CELL}">7.5kW 이하</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">○</td></tr>
<tr><td style="{CELL}">7.5~15kW</td><td style="{CELL}">△</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">○</td></tr>
<tr><td style="{CELL}">15kW 초과</td><td style="{CELL}">×</td><td style="{CELL}">○</td><td style="{CELL}">○</td><td style="{CELL}">○</td></tr>
</tbody></table>"""


SVG_SLOTS: dict[str, list[str]] = {
    "page-029": [svg_p029_tbl053(), svg_p029_tbl054()],
    "page-041": [svg_p041_tbl081()],
    "page-044": [svg_p044_tbl089()],
    "page-045": [svg_p045_tbl092()],
}
