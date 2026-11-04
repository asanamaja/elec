#!/usr/bin/env python3
"""Build the installable static Speetto dashboard and alert feed."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "speetto"
OUTPUT_DIR = ROOT / "output" / "speetto"
TEMPLATE_PATH = Path(__file__).with_name("dashboard_template.html")


def read_jsonl(path: Path, limit: int | None = None) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows[-limit:] if limit else rows


def compact_history(snapshot: dict) -> dict:
    return {
        "observed_at": snapshot["observed_at"],
        "state_hash": snapshot["state_hash"],
        "rounds": [
            {
                "id": item["id"],
                "status": item["status"],
                "shipment_rate": item["shipment_rate"],
                "official_as_of": item["official_as_of"],
                "first_remaining": item["tiers"][0]["remaining"],
                "net_roi": item["metrics"]["proxy"]["blocks"]["all"]["net_roi"],
                "first_roi": item["metrics"]["proxy"]["blocks"]["first"]["net_roi"],
                "break_even_unresolved": item["metrics"]["break_even"]["all_prizes_max_unresolved"],
            }
            for item in snapshot.get("rounds", [])
        ],
    }


def build_feed(latest: dict) -> str:
    updated = latest["observed_at"]
    entries = []
    for index, alert in enumerate(latest.get("alerts", [])[:30]):
        alert_id = f"{latest['state_hash']}-{index}"
        entries.append(
            f"""
  <entry>
    <id>tag:asanamaja.github.io,2026:speetto:{escape(alert_id)}</id>
    <title>{escape(alert["title"])}</title>
    <updated>{escape(updated)}</updated>
    <link href="https://asanamaja.github.io/elec/output/speetto/"/>
    <summary>{escape((alert.get("round_id") or "") + " " + alert["message"])}</summary>
  </entry>"""
        )
    return f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <id>tag:asanamaja.github.io,2026:speetto</id>
  <title>스피또 스코프 변경 알림</title>
  <updated>{escape(updated)}</updated>
  <link href="https://asanamaja.github.io/elec/output/speetto/"/>
  <link rel="self" href="https://asanamaja.github.io/elec/output/speetto/alerts.xml"/>
  {''.join(entries)}
</feed>
"""


def main() -> None:
    latest_path = DATA_DIR / "latest.json"
    if not latest_path.exists():
        raise SystemExit("Run scripts/speetto/update.py before building the dashboard.")
    latest = json.loads(latest_path.read_text(encoding="utf-8"))
    history = [compact_history(item) for item in read_jsonl(DATA_DIR / "history.jsonl")]
    checks = read_jsonl(DATA_DIR / "checks.jsonl", limit=120)
    payload = {
        "latest": latest,
        "history": history,
        "checks": checks,
        "built_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
    }
    embedded = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    html = template.replace("__SPEETTO_DATA__", embedded).replace(
        "__BUILD_TIME__", payload["built_at"]
    )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "index.html").write_text(html, encoding="utf-8")
    (OUTPUT_DIR / "alerts.xml").write_text(build_feed(latest), encoding="utf-8")
    print(
        f"Built dashboard with {len(latest['rounds'])} rounds and "
        f"{len(history)} historical snapshots."
    )


if __name__ == "__main__":
    main()
