# elec — 개인 도구와 전기기사 암기 노트

## 스피또 스코프

동행복권 공식 발행·지급 데이터를 하루 4회 확인하고, 상품·회차별로 다음 정보를 분리해 보여주는 정적 PWA입니다.

- 판매점 입고율과 등위별 미지급수량
- 발행구조 기준 세전·세후 기대값
- 1등만, 1~3등, 전체 등위 기대값
- 청구진행 프록시와 사용자 지정 미해결 매수 시나리오
- 손익분기 미해결 매수, 예산별 기대손익·한 번 이상 당첨 확률
- 역대 관측 최고값, 변경 로그, 홀수 1등 신호, 고액 지급 패턴
- 브라우저 알림, Atom 알림 피드, 설치형 PWA

**대시보드:**  
https://asanamaja.github.io/elec/output/speetto/

공식 `잔여수량`은 미판매 재고가 아니라 미지급 당첨권 수입니다. 앱의 청구진행 값은 실제 구매 가능 확률이 아닌 민감도 분석이며, 자세한 계산식과 전략 등급은 [`docs/SPEETTO_ANALYTICS.md`](docs/SPEETTO_ANALYTICS.md)를 참고하세요.

수동 갱신:

```bash
python3 scripts/speetto/update.py
python3 scripts/speetto/build_dashboard.py
python3 -m unittest discover -s scripts/speetto/tests -v
```

## 모바일에서 보기

**심벌·도면 사진 반영 (가볍게, 추천):**  
https://asanamaja.github.io/elec/output/symbols_view.html

**전체 175페이지 PDF 전사본:**  
https://asanamaja.github.io/elec/output/dandap_manual.html?v=20260629-render-audit

**학습 노트 (텍스트만, 사진 없음):**  
https://asanamaja.github.io/elec/private_study_notes.html

**Cursor 모바일 (에이전트):**
1. 폰에서 [cursor.com/agents](https://cursor.com/agents) 접속 (또는 홈 화면에 PWA 추가)
2. 같은 Cursor 계정으로 로그인
3. 저장소 `asanamaja/elec` 선택 후 작업

**폴더 연동 (Git 앱):**
- iOS: Working Copy 등으로 `https://github.com/asanamaja/elec.git` clone
- Android: MGit, Termux 등으로 동일 repo clone
- `git pull` 하면 PC·모바일·Cloud Agent 내용이 맞춰짐

## 파일

| 파일 | 설명 |
|------|------|
| `private_study_notes.md` | 마크다운 원본 |
| `private_study_notes.html` | 모바일·브라우저용 HTML |
| `output/dandap_replica.html` | PDF 원본 레이아웃 HTML 복제본 (A4 175p) |
| `scripts/pdf_to_html_replica.py` | PDF → HTML 변환 스크립트 |

## PDF 복제본 재생성

원본 PDF는 Git에 포함되지 않습니다. Google Drive 등에서 받은 뒤:

```bash
pip install -r scripts/requirements-replica.txt
# PDF를 assets/pdf/source.pdf 에 저장
python3 scripts/pdf_to_html_replica.py
```

출력: `output/dandap_replica.html` + `assets/images/crops/` (도표·일러스트 크롭)
