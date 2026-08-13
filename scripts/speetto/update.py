#!/usr/bin/env python3
"""Fetch official Speetto data, calculate metrics, and append history logs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from core import SPECS, enrich_round


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "speetto"
LATEST_PATH = DATA_DIR / "latest.json"
HISTORY_PATH = DATA_DIR / "history.jsonl"
CHECKS_PATH = DATA_DIR / "checks.jsonl"

BASE_URL = "https://www.dhlottery.co.kr"
PUBLICATION_URL = f"{BASE_URL}/st/selectPblcnDsctn.do"
DETAIL_URL = f"{BASE_URL}/st/selectPblcnDsctnDtl.do"
WINNER_URL = f"{BASE_URL}/st/selectWnDsctn.do"
REFERER = f"{BASE_URL}/st/pblcnDsctn"
USER_AGENT = "SpeettoScope/1.0 (+https://asanamaja.github.io/elec/output/speetto/)"


def _request_json(url: str, params: list[tuple[str, Any]] | dict[str, Any], retries: int = 3) -> dict[str, Any]:
    query = urlencode(params, doseq=True)
    request = Request(
        f"{url}?{query}",
        headers={
            "Accept": "application/json",
            "Referer": REFERER,
            "User-Agent": USER_AGENT,
            "X-Requested-With": "XMLHttpRequest",
        },
    )
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            with urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            if payload.get("resultCode") not in (None, "success"):
                raise RuntimeError(payload.get("resultMessage") or payload["resultCode"])
            if payload.get("data") is None:
                raise RuntimeError("Official endpoint returned no data")
            return payload
        except (HTTPError, URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(2**attempt)
    raise RuntimeError(f"Failed to fetch {url}: {last_error}")


def parse_korean_money(value: str | None, fallback: int) -> int:
    if not value:
        return fallback
    compact = value.replace(",", "").replace(" ", "")
    direct = re.search(r"(\d+)원", compact)
    if direct and not any(unit in compact for unit in ("억", "천만", "백만", "만", "천")):
        return int(direct.group(1))
    unit_patterns = (
        ("억원", 100_000_000),
        ("천만원", 10_000_000),
        ("백만원", 1_000_000),
        ("만원", 10_000),
        ("천원", 1_000),
    )
    for unit, multiplier in unit_patterns:
        match = re.search(rf"(\d+){unit}", compact)
        if match:
            return int(match.group(1)) * multiplier
    return fallback


def parse_probability_percent(value: Any) -> float:
    if value in (None, ""):
        return 0.0
    text = str(value).strip().replace("%", "")
    if "/" in text:
        numerator, denominator = text.split("/", 1)
        try:
            return 100.0 * float(numerator) / float(denominator)
        except (ValueError, ZeroDivisionError):
            return 0.0
    try:
        return float(text)
    except ValueError:
        return 0.0


def fetch_publications() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    params = [
        ("gdsType", ""),
        ("gdsPrice", ""),
        ("gdsStatus", ""),
        ("pageNum", 1),
        ("recordCountPerPage", 100),
    ]
    data = _request_json(PUBLICATION_URL, params)["data"]
    return data["list"], data.get("stRnkDate", [])


def normalize_round(summary: dict[str, Any], detail: dict[str, Any]) -> dict[str, Any]:
    product = summary["stGmTypeCd"]
    spec = SPECS[product]
    tiers: list[dict[str, int]] = []
    for rank, fallback_prize in enumerate(spec["prizes"], start=1):
        initial = int(detail.get(f"stRnk{rank}WnQty") or 0)
        if initial <= 0:
            continue
        claimed = int(detail.get(f"stRnk{rank}WnCmptnQty") or 0)
        remaining = int(detail.get(f"stIvtRnk{rank}Qty") or max(0, initial - claimed))
        tiers.append(
            {
                "rank": rank,
                "prize": parse_korean_money(detail.get(f"stRnk{rank}GdsLstcCharCn"), fallback_prize),
                "initial": initial,
                "claimed": claimed,
                "remaining": remaining,
            }
        )
    return {
        "id": f"{product}-{int(detail['stEpsd'])}",
        "product": product,
        "product_name": detail["stGmTypeNm"],
        "round": int(detail["stEpsd"]),
        "status": detail["ntslStatus"],
        "price": int(detail["stNtslAmt"]),
        "issued": int(detail["pblcnQty"]),
        "shipment_rate": float(detail["stSpmtRt"]),
        "overall_win_probability_percent": parse_probability_percent(detail.get("stSumWnPbltNm")),
        "official_payout_rate_percent": float(detail.get("stSumWnGiveRt") or 0),
        "sales_start": detail.get("stNtslBgngDt"),
        "sales_end": detail.get("stNtslEndDt"),
        "claim_end": detail.get("stGiveEndDt"),
        "official_as_of": detail.get("dataChgDt") or summary.get("dataChgDt"),
        "source_serial": int(summary["ntslWnSn"]),
        "tiers": tiers,
    }


def fetch_rounds() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    summaries, rank_dates = fetch_publications()
    rounds: list[dict[str, Any]] = []
    for summary in summaries:
        payload = _request_json(DETAIL_URL, {"ntslWnSn": summary["ntslWnSn"]})
        rounds.append(normalize_round(summary, payload["data"]["result"]))
        time.sleep(0.04)
    rounds.sort(key=lambda item: (item["status"] != "판매중", -item["price"], -item["round"]))
    return rounds, rank_dates


def _product_code(name: str) -> str | None:
    return {
        "스피또500": "SP500",
        "스피또1000": "SP1000",
        "스피또2000": "SP2000",
    }.get(name)


def fetch_winners() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for product_name in ("스피또500", "스피또1000", "스피또2000"):
        payload = _request_json(
            WINNER_URL,
            {
                "stGmTypeNm": product_name,
                "pageNum": 1,
                "recordCountPerPage": 2500,
            },
        )
        for item in payload["data"]["list"]:
            product = _product_code(item.get("ltGdsNm", ""))
            if not product:
                continue
            records.append({
                "row_id": item.get("rowId"),
                "product": product,
                "product_name": item["ltGdsNm"],
                "round": int(item["ltEpsd"]),
                "rank": int(item["wnSqNo"]),
                "prize": int(str(item["ltWnAmtCn"]).replace(",", "")),
                "paid_at": item["giveDt"],
                "store_id": item.get("ltShpId"),
                "store_name": item.get("ltShpNm") or "미확인",
            })
    return sorted(records, key=lambda item: item["paid_at"], reverse=True)


def calculate_winner_stats(winners: list[dict[str, Any]], current_rounds: list[dict[str, Any]]) -> dict[str, Any]:
    firsts = [record for record in winners if record["rank"] == 1]
    first_counts = Counter(record["product"] for record in firsts)

    # Distinct product/round/rank/store records avoid counting a SP2000 pair as
    # two independent "lucky store" events.
    store_events: dict[tuple[Any, ...], dict[str, Any]] = {}
    for record in winners:
        key = (record["product"], record["round"], record["rank"], record["store_id"], record["store_name"])
        store_events[key] = record
    repeat_counter = Counter(
        (record["store_id"] or record["store_name"], record["store_name"])
        for record in store_events.values()
    )
    repeat_stores = [
        {"store_key": key, "store_name": name, "events": count}
        for (key, name), count in repeat_counter.most_common(20)
    ]

    pair_groups: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
    for record in firsts:
        if record["product"] == "SP2000" and record["round"] >= 16:
            key = (record["round"], record["store_id"] or f"name:{record['store_name']}")
            pair_groups[key].append(record)
    completed_pairs = [records for records in pair_groups.values() if len(records) == 2]
    same_day_pairs = sum(
        1 for records in completed_pairs if len({record["paid_at"] for record in records}) == 1
    )
    split_gaps = []
    for records in completed_pairs:
        dates = sorted(datetime.strptime(record["paid_at"], "%Y%m%d").date() for record in records)
        gap = (dates[-1] - dates[0]).days
        if gap:
            split_gaps.append(gap)

    odd_signals: list[dict[str, Any]] = []
    current_ids = {
        (round_record["product"], round_record["round"]): round_record
        for round_record in current_rounds
        if round_record["status"] == "판매중"
    }
    for (product, round_number), round_record in current_ids.items():
        first_remaining = round_record["tiers"][0]["remaining"]
        if product != "SP2000" or first_remaining % 2 == 0:
            continue
        by_store: dict[tuple[Any, ...], list[dict[str, Any]]] = defaultdict(list)
        for record in firsts:
            if record["product"] == product and record["round"] == round_number:
                by_store[(record["store_id"], record["store_name"])].append(record)
        singleton_stores = [
            {
                "store_id": store_id,
                "store_name": store_name,
                "paid_at": max(record["paid_at"] for record in records),
                "paid_tickets": len(records),
            }
            for (store_id, store_name), records in by_store.items()
            if len(records) % 2 == 1
        ]
        odd_signals.append(
            {
                "product": product,
                "round": round_number,
                "first_remaining": first_remaining,
                "singleton_paid_stores": singleton_stores,
                "warning": "홀수는 미지급 상태 신호일 뿐 짝장이 판매점 재고에 있다는 뜻이 아님",
            }
        )

    return {
        "official_rows": len(winners),
        "first_rows_by_product": dict(first_counts),
        "repeat_stores": repeat_stores,
        "pair_claims": {
            "completed_pair_groups": len(completed_pairs),
            "same_day_groups": same_day_pairs,
            "split_day_groups": len(completed_pairs) - same_day_pairs,
            "unmatched_groups": sum(1 for records in pair_groups.values() if len(records) % 2 == 1),
            "split_gap_days_median": sorted(split_gaps)[len(split_gaps) // 2] if split_gaps else 0,
            "split_gap_days_max": max(split_gaps, default=0),
        },
        "odd_signals": odd_signals,
        "latest_high_prize_payments": winners[:40],
    }


def _round_state(round_record: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": round_record["id"],
        "status": round_record["status"],
        "shipment_rate": round_record["shipment_rate"],
        "official_as_of": round_record["official_as_of"],
        "remaining": [tier["remaining"] for tier in round_record["tiers"]],
        "claimed": [tier["claimed"] for tier in round_record["tiers"]],
    }


def state_hash(rounds: list[dict[str, Any]], winner_stats: dict[str, Any]) -> str:
    state = {
        "rounds": [_round_state(round_record) for round_record in rounds],
        "winner_rows": winner_stats["official_rows"],
        "odd_signals": winner_stats["odd_signals"],
    }
    encoded = json.dumps(state, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()[:20]


def load_latest() -> dict[str, Any] | None:
    if not LATEST_PATH.exists():
        return None
    return json.loads(LATEST_PATH.read_text(encoding="utf-8"))


def detect_changes(previous: dict[str, Any] | None, rounds: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not previous:
        return [{"type": "initial", "message": "첫 공식 데이터 스냅숏을 저장했습니다."}]
    old_by_id = {item["id"]: item for item in previous.get("rounds", [])}
    changes: list[dict[str, Any]] = []
    for current in rounds:
        old = old_by_id.get(current["id"])
        if not old:
            changes.append(
                {"type": "new-round", "round_id": current["id"], "message": f"{current['id']} 신규 회차"}
            )
            continue
        if old["shipment_rate"] != current["shipment_rate"]:
            changes.append(
                {
                    "type": "shipment",
                    "round_id": current["id"],
                    "from": old["shipment_rate"],
                    "to": current["shipment_rate"],
                    "message": f"입고율 {old['shipment_rate']}% → {current['shipment_rate']}%",
                }
            )
        old_tiers = {tier["rank"]: tier for tier in old["tiers"]}
        for tier in current["tiers"]:
            old_tier = old_tiers.get(tier["rank"])
            if old_tier and old_tier["remaining"] != tier["remaining"]:
                changes.append(
                    {
                        "type": "remaining",
                        "round_id": current["id"],
                        "rank": tier["rank"],
                        "from": old_tier["remaining"],
                        "to": tier["remaining"],
                        "message": (
                            f"{tier['rank']}등 미지급 {old_tier['remaining']} → {tier['remaining']}매"
                        ),
                    }
                )
    return changes


def build_alerts(rounds: list[dict[str, Any]], changes: list[dict[str, Any]]) -> list[dict[str, Any]]:
    alerts: list[dict[str, Any]] = []
    for round_record in rounds:
        if round_record["status"] != "판매중":
            continue
        first_remaining = round_record["tiers"][0]["remaining"]
        metrics = round_record["metrics"]
        if first_remaining == 0:
            alerts.append(
                {
                    "level": "danger",
                    "code": "first-zero",
                    "round_id": round_record["id"],
                    "title": "1등 제외 회차",
                    "message": "공식 미지급 1등이 0매입니다.",
                }
            )
        if round_record["product"] == "SP2000" and first_remaining % 2 == 1:
            alerts.append(
                {
                    "level": "watch",
                    "code": "odd-first",
                    "round_id": round_record["id"],
                    "title": "홀수 잔여 감지",
                    "message": "짝 중 한 장만 지급된 상태일 수 있습니다. 판매·재고 신호는 아닙니다.",
                }
            )
        proxy_roi = metrics["proxy"]["blocks"]["all"]["net_roi"]
        if proxy_roi >= 1.0:
            alerts.append(
                {
                    "level": "model",
                    "code": "proxy-positive",
                    "round_id": round_record["id"],
                    "title": "청구진행 모형상 양수",
                    "message": f"세후 추정 ROI {proxy_roi * 100:.1f}%. 미판매 기대값으로 해석 금지.",
                }
            )
        if metrics["break_even"]["shipment_necessary_condition_met"]:
            alerts.append(
                {
                    "level": "info",
                    "code": "shipment-necessary-met",
                    "round_id": round_record["id"],
                    "title": "입고 필요조건 통과",
                    "message": "손익분기 미해결 매수에 대한 입고율 필요조건만 충족했습니다.",
                }
            )
    for change in changes:
        if change["type"] not in {"initial"}:
            alerts.append(
                {
                    "level": "change",
                    "code": f"change-{change['type']}",
                    "round_id": change.get("round_id"),
                    "title": "공식 수치 변경",
                    "message": change["message"],
                }
            )
    return alerts


def load_history() -> list[dict[str, Any]]:
    if not HISTORY_PATH.exists():
        return []
    snapshots = []
    for line in HISTORY_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            try:
                snapshots.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return snapshots


def historical_summary(history: list[dict[str, Any]], rounds: list[dict[str, Any]]) -> dict[str, Any]:
    observations: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for snapshot in history:
        for item in snapshot.get("rounds", []):
            proxy = item.get("metrics", {}).get("proxy", {}).get("blocks", {})
            if proxy:
                observations[item["id"]].append(
                    {
                        "observed_at": snapshot["observed_at"],
                        "net_roi": proxy["all"]["net_roi"],
                        "first_roi": proxy["first"]["net_roi"],
                        "shipment_rate": item["shipment_rate"],
                        "first_remaining": item["tiers"][0]["remaining"],
                    }
                )
    comparison: dict[str, Any] = {}
    all_points = [point for points in observations.values() for point in points]
    for current in rounds:
        roi = current["metrics"]["proxy"]["blocks"]["all"]["net_roi"]
        points = observations.get(current["id"], [])
        values = [point["net_roi"] for point in points]
        percentile = (
            100.0 * sum(value <= roi for value in values) / len(values)
            if values
            else 100.0
        )
        comparison[current["id"]] = {
            "observations": len(points) + 1,
            "current_percentile": percentile,
            "best_net_roi": max([roi, *values]),
        }
    candidates = [
        {
            "round_id": round_id,
            **point,
        }
        for round_id, points in observations.items()
        for point in points
    ]
    candidates.extend(
        {
            "round_id": current["id"],
            "observed_at": current.get("official_as_of"),
            "net_roi": current["metrics"]["proxy"]["blocks"]["all"]["net_roi"],
            "first_roi": current["metrics"]["proxy"]["blocks"]["first"]["net_roi"],
            "shipment_rate": current["shipment_rate"],
            "first_remaining": current["tiers"][0]["remaining"],
        }
        for current in rounds
    )
    return {
        "snapshots": len(history),
        "points": len(all_points),
        "comparison": comparison,
        "best_all_roi": max(candidates, key=lambda item: item["net_roi"], default=None),
        "best_first_roi": max(candidates, key=lambda item: item["first_roi"], default=None),
    }


def append_jsonl(path: Path, payload: dict[str, Any], max_lines: int | None = None) -> None:
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    lines.append(json.dumps(payload, ensure_ascii=False, separators=(",", ":")))
    if max_lines and len(lines) > max_lines:
        lines = lines[-max_lines:]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def send_webhook(alerts: list[dict[str, Any]], observed_at: str) -> None:
    webhook = os.environ.get("SPEETTO_ALERT_WEBHOOK_URL")
    actionable = [alert for alert in alerts if alert["code"] in {"odd-first", "proxy-positive"}]
    if not webhook or not actionable:
        return
    content = "\n".join(
        f"• {alert.get('round_id', '')} {alert['title']}: {alert['message']}"
        for alert in actionable[:10]
    )
    body = json.dumps(
        {"content": f"스피또 스코프 알림 ({observed_at})\n{content}"},
        ensure_ascii=False,
    ).encode("utf-8")
    request = Request(webhook, data=body, method="POST", headers={"Content-Type": "application/json"})
    try:
        with urlopen(request, timeout=15):
            pass
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"Webhook warning: {exc}", file=sys.stderr)


def update() -> dict[str, Any]:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    observed_at = datetime.now(UTC).replace(microsecond=0).isoformat()
    previous = load_latest()
    rounds, rank_dates = fetch_rounds()
    enriched = [enrich_round(round_record) for round_record in rounds]
    winners = fetch_winners()
    winner_stats = calculate_winner_stats(winners, enriched)
    changes = detect_changes(previous, enriched)
    alerts = build_alerts(enriched, changes)
    digest = state_hash(enriched, winner_stats)
    old_history = load_history()
    summary = historical_summary(old_history, enriched)

    snapshot = {
        "schema_version": 1,
        "observed_at": observed_at,
        "state_hash": digest,
        "source": {
            "name": "동행복권",
            "publication_url": f"{BASE_URL}/st/pblcnDsctn",
            "winner_url": f"{BASE_URL}/st/wnrStry?stGmTypeCd=all",
            "definitions": {
                "shipment_rate": "발행량 중 판매점에 누적 입고된 비율",
                "remaining": "당첨수량-지급수량. 미판매 당첨권이 아님",
                "proxy": "저액권 지급 진행률로 만든 미해결 모집단 추정치. 판매량이 아님",
            },
        },
        "rounds": enriched,
        "winner_stats": winner_stats,
        "rank_update_dates": rank_dates,
        "changes": changes,
        "alerts": alerts,
        "history_summary": summary,
    }

    LATEST_PATH.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not previous or previous.get("state_hash") != digest:
        append_jsonl(HISTORY_PATH, snapshot)
    append_jsonl(
        CHECKS_PATH,
        {
            "checked_at": observed_at,
            "ok": True,
            "state_hash": digest,
            "changed": not previous or previous.get("state_hash") != digest,
            "rounds": len(enriched),
            "official_rows": winner_stats["official_rows"],
        },
        max_lines=2_000,
    )
    send_webhook(alerts, observed_at)
    return snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    try:
        snapshot = update()
    except Exception as exc:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        append_jsonl(
            CHECKS_PATH,
            {
                "checked_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
                "ok": False,
                "error": str(exc),
            },
            max_lines=2_000,
        )
        raise
    print(
        f"Updated {len(snapshot['rounds'])} rounds, "
        f"{snapshot['winner_stats']['official_rows']} winner rows, "
        f"{len(snapshot['alerts'])} alerts."
    )


if __name__ == "__main__":
    main()
