#!/usr/bin/env python3
"""Speetto probability, tax, expectation, and alert calculations.

The official publication data reports shipped-to-retailer percentages and
unpaid winning tickets.  It does *not* report consumer sales or the number of
winning tickets in purchasable inventory.  Every metric derived from a
remaining-pool denominator is therefore explicitly named ``proxy``.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, log
from statistics import median
from typing import Any, Iterable


SPECS: dict[str, dict[str, Any]] = {
    "SP500": {
        "name": "스피또500",
        "price": 500,
        "prizes": [200_000_000, 1_000_000, 5_000, 500],
        "first_base_odds": 4_000_000,
        "color": "#4f8a68",
    },
    "SP1000": {
        "name": "스피또1000",
        "price": 1_000,
        "prizes": [500_000_000, 20_000_000, 10_000, 5_000, 1_000],
        "first_base_odds": 5_000_000,
        "color": "#386fa4",
    },
    "SP2000": {
        "name": "스피또2000",
        "price": 2_000,
        "prizes": [1_000_000_000, 100_000_000, 10_000_000, 20_000, 4_000, 2_000],
        "first_base_odds": 5_000_000,
        "color": "#a85d3f",
    },
}


BUDGET_SCALES = (10_000, 50_000, 100_000, 500_000, 1_000_000)


@dataclass(frozen=True)
class Tier:
    rank: int
    prize: int
    initial: int
    claimed: int
    remaining: int


def net_prize(prize: int, ticket_price: int) -> float:
    """Return estimated Korean lottery payout after withholding tax.

    Prizes up to KRW 2,000,000 are tax exempt.  For larger prizes, the ticket
    price is treated as acquisition cost, 22% applies through KRW 300,000,000,
    and 33% applies above that threshold.  Actual payment administration is
    authoritative; this function is an analytical estimate.
    """

    if prize <= 2_000_000:
        return float(prize)
    taxable = max(0, prize - ticket_price)
    lower = min(taxable, 300_000_000)
    upper = max(0, taxable - 300_000_000)
    return float(prize) - lower * 0.22 - upper * 0.33


def probability_at_least_one(probability: float, trials: int) -> float:
    probability = max(0.0, min(1.0, probability))
    if trials <= 0 or probability <= 0:
        return 0.0
    if probability >= 1:
        return 1.0
    return 1.0 - exp(trials * log(1.0 - probability))


def _weighted_claim_progress(tiers: Iterable[Tier]) -> float:
    """Robust proxy for the share of the print run already processed.

    Frequent prizes of KRW 50,000 or less are used because their claim counts
    are much less sparse than jackpots.  The median limits the influence of an
    individual tier's reporting delay.  It remains a *claim* proxy, not sales.
    """

    frequent = [
        tier.claimed / tier.initial
        for tier in tiers
        if tier.initial > 0 and tier.prize <= 50_000
    ]
    return max(0.0, min(1.0, median(frequent))) if frequent else 0.0


def _tier_expected_value(tiers: Iterable[Tier], denominator: float, net: bool, price: int) -> float:
    if denominator <= 0:
        return 0.0
    return sum(
        tier.remaining * (net_prize(tier.prize, price) if net else tier.prize)
        for tier in tiers
    ) / denominator


def _baseline_expected_value(tiers: Iterable[Tier], issued: int, net: bool, price: int) -> float:
    if issued <= 0:
        return 0.0
    return sum(
        tier.initial * (net_prize(tier.prize, price) if net else tier.prize)
        for tier in tiers
    ) / issued


def _metric_block(tiers: list[Tier], denominator: float, price: int) -> dict[str, Any]:
    first = tiers[:1]
    high = tiers[: min(3, len(tiers))]
    blocks = {
        "first": first,
        "high": high,
        "all": tiers,
    }
    output: dict[str, Any] = {}
    for key, selected in blocks.items():
        gross = _tier_expected_value(selected, denominator, False, price)
        net = _tier_expected_value(selected, denominator, True, price)
        output[key] = {
            "gross_ev": gross,
            "net_ev": net,
            "gross_roi": gross / price if price else 0.0,
            "net_roi": net / price if price else 0.0,
        }
    return output


def _scale_metrics(
    tiers: list[Tier],
    denominator: float,
    price: int,
    net_ev: float,
) -> list[dict[str, Any]]:
    probabilities = [
        min(1.0, tier.remaining / denominator) if denominator > 0 else 0.0
        for tier in tiers
    ]
    rows: list[dict[str, Any]] = []
    budgets = sorted({price, *BUDGET_SCALES})
    for budget in budgets:
        trials = max(1, budget // price)
        actual_budget = trials * price
        first_p = probability_at_least_one(probabilities[0], trials)
        high_p = probability_at_least_one(sum(probabilities[:3]), trials)
        any_p = probability_at_least_one(sum(probabilities), trials)
        cover_single_p = sum(
            probability
            for tier, probability in zip(tiers, probabilities)
            if net_prize(tier.prize, price) >= actual_budget
        )
        cover_probability = probability_at_least_one(cover_single_p, trials)
        expected_payout = trials * net_ev
        rows.append(
            {
                "budget": actual_budget,
                "tickets": trials,
                "expected_payout": expected_payout,
                "expected_profit": expected_payout - actual_budget,
                "first_probability": first_p,
                "high_probability": high_p,
                "any_probability": any_p,
                "single_prize_cover_probability": cover_probability,
            }
        )
    return rows


def _decision_band(net_roi: float, first_remaining: int, scale_rows: list[dict[str, Any]]) -> dict[str, str]:
    """Classify a proxy metric without turning it into a purchase instruction."""

    cover_at_100k = next(
        (row["single_prize_cover_probability"] for row in scale_rows if row["budget"] == 100_000),
        0.0,
    )
    if first_remaining == 0:
        return {"code": "first-zero", "label": "1등 제외", "tone": "danger"}
    if net_roi >= 1.5 and cover_at_100k >= 0.2:
        return {"code": "rare-strong", "label": "강한 관찰 신호", "tone": "strong"}
    if net_roi >= 1.25:
        return {"code": "buffered", "label": "완충 기대값", "tone": "positive"}
    if net_roi >= 1.0:
        return {"code": "model-positive", "label": "모형상 양수", "tone": "positive"}
    if net_roi >= 0.8:
        return {"code": "near", "label": "손익분기 근접", "tone": "watch"}
    return {"code": "negative", "label": "기대손실", "tone": "muted"}


def calculate_round_metrics(record: dict[str, Any]) -> dict[str, Any]:
    """Calculate all dashboard metrics for one normalized publication round."""

    product = record["product"]
    spec = SPECS[product]
    price = int(record.get("price") or spec["price"])
    issued = int(record["issued"])
    shipment_rate = float(record["shipment_rate"])
    tiers = [
        Tier(
            rank=int(item["rank"]),
            prize=int(item["prize"]),
            initial=int(item["initial"]),
            claimed=int(item["claimed"]),
            remaining=int(item["remaining"]),
        )
        for item in record["tiers"]
    ]

    baseline_gross = _baseline_expected_value(tiers, issued, False, price)
    baseline_net = _baseline_expected_value(tiers, issued, True, price)
    progress_proxy = _weighted_claim_progress(tiers)
    unresolved_proxy = max(1.0, issued * (1.0 - progress_proxy))
    unshipped_floor = max(0.0, issued * (1.0 - shipment_rate / 100.0))
    metrics = _metric_block(tiers, unresolved_proxy, price)

    all_remaining_net = sum(tier.remaining * net_prize(tier.prize, price) for tier in tiers)
    first_remaining_net = tiers[0].remaining * net_prize(tiers[0].prize, price)
    break_even_all = all_remaining_net / price if price else 0.0
    break_even_first = first_remaining_net / price if price else 0.0
    required_processed = max(0.0, min(1.0, 1.0 - break_even_all / issued)) if issued else 1.0

    tier_rows = []
    for tier in tiers:
        baseline_probability = tier.initial / issued if issued else 0.0
        proxy_probability = tier.remaining / unresolved_proxy if unresolved_proxy else 0.0
        tier_rows.append(
            {
                "rank": tier.rank,
                "prize": tier.prize,
                "net_prize": net_prize(tier.prize, price),
                "initial": tier.initial,
                "claimed": tier.claimed,
                "remaining": tier.remaining,
                "baseline_probability": baseline_probability,
                "proxy_probability": proxy_probability,
                "density_multiple": proxy_probability / baseline_probability if baseline_probability else 0.0,
                "baseline_gross_ev": baseline_probability * tier.prize,
                "baseline_net_ev": baseline_probability * net_prize(tier.prize, price),
                "proxy_gross_ev": proxy_probability * tier.prize,
                "proxy_net_ev": proxy_probability * net_prize(tier.prize, price),
            }
        )

    scale_rows = _scale_metrics(tiers, unresolved_proxy, price, metrics["all"]["net_ev"])
    decision = _decision_band(metrics["all"]["net_roi"], tiers[0].remaining, scale_rows)

    pair_option: dict[str, Any] | None = None
    if product == "SP2000":
        first_probability = tiers[0].remaining / unresolved_proxy if unresolved_proxy else 0.0
        extra_net = first_probability * (net_prize(tiers[0].prize, price) - price)
        pair_option = {
            "available": True,
            "odd_remaining_signal": tiers[0].remaining % 2 == 1,
            "first_remaining": tiers[0].remaining,
            "perfect_hold_extra_net_ev": extra_net,
            "perfect_hold_net_ev": metrics["all"]["net_ev"] + extra_net,
            "perfect_hold_net_roi": (metrics["all"]["net_ev"] + extra_net) / price,
            "caveat": "정확한 짝장이 미판매 상태이고 판매점이 즉시 보관해 주는 경우만 해당",
        }

    return {
        "baseline": {
            "gross_ev": baseline_gross,
            "net_ev": baseline_net,
            "gross_roi": baseline_gross / price,
            "net_roi": baseline_net / price,
            "expected_loss": price - baseline_net,
        },
        "proxy": {
            "claim_progress": progress_proxy,
            "unresolved_tickets": unresolved_proxy,
            "unshipped_floor": unshipped_floor,
            "blocks": metrics,
            "warning": "미지급 진행률로 만든 모형값이며 실제 미판매 재고 기대값이 아님",
        },
        "break_even": {
            "all_prizes_max_unresolved": break_even_all,
            "first_only_max_unresolved": break_even_first,
            "required_processed_fraction": required_processed,
            "minimum_shipment_rate": required_processed * 100.0,
            "shipment_necessary_condition_met": shipment_rate / 100.0 >= required_processed,
        },
        "tiers": tier_rows,
        "scales": scale_rows,
        "decision": decision,
        "pair_option": pair_option,
    }


def enrich_round(record: dict[str, Any]) -> dict[str, Any]:
    enriched = dict(record)
    enriched["metrics"] = calculate_round_metrics(record)
    return enriched

