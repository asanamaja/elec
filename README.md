# elec — 전기기사 암기 노트

## 모바일에서 보기

**심벌·도면 사진 반영 (가볍게, 추천):**  
https://asanamaja.github.io/elec/output/symbols_view.html

**전체 175페이지 PDF 전사본:**  
https://asanamaja.github.io/elec/output/dandap_manual.html?v=20260629-fidelity

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
