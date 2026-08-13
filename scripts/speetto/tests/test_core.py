#!/usr/bin/env python3
from __future__ import annotations

import sys
import unittest
from pathlib import Path


SPEETTO_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SPEETTO_DIR))

from core import calculate_round_metrics, net_prize, probability_at_least_one  # noqa: E402


def make_record(product: str, price: int, issued: int, shipment: float, tiers: list[tuple[int, int, int]]) -> dict:
    """Build rank tuples of (prize, initial, remaining)."""

    return {
        "id": f"{product}-test",
        "product": product,
        "product_name": product,
        "round": 1,
        "status": "판매중",
        "price": price,
        "issued": issued,
        "shipment_rate": shipment,
        "tiers": [
            {
                "rank": rank,
                "prize": prize,
                "initial": initial,
                "claimed": initial - remaining,
                "remaining": remaining,
            }
            for rank, (prize, initial, remaining) in enumerate(tiers, start=1)
        ],
    }


class TaxTests(unittest.TestCase):
    def test_small_prizes_are_tax_free(self) -> None:
        self.assertEqual(net_prize(2_000_000, 1_000), 2_000_000)

    def test_high_prize_progressive_tax(self) -> None:
        self.assertAlmostEqual(net_prize(200_000_000, 500), 156_000_110)
        self.assertAlmostEqual(net_prize(500_000_000, 1_000), 368_000_330)
        self.assertAlmostEqual(net_prize(1_000_000_000, 2_000), 703_000_660)


class ProbabilityTests(unittest.TestCase):
    def test_at_least_one(self) -> None:
        p = probability_at_least_one(1 / 5_000_000, 2)
        self.assertAlmostEqual(p, 1 - (1 - 1 / 5_000_000) ** 2)
        self.assertEqual(probability_at_least_one(0, 100), 0)


class MetricTests(unittest.TestCase):
    def test_speetto_2000_baseline(self) -> None:
        record = make_record(
            "SP2000",
            2_000,
            5_000_000,
            0,
            [
                (1_000_000_000, 1, 1),
                (100_000_000, 3, 3),
                (10_000_000, 25, 25),
                (20_000, 13_750, 13_750),
                (4_000, 350_000, 350_000),
                (2_000, 1_400_000, 1_400_000),
            ],
        )
        metrics = calculate_round_metrics(record)
        self.assertAlmostEqual(metrics["baseline"]["gross_roi"], 0.6025, places=5)
        self.assertAlmostEqual(metrics["baseline"]["net_roi"], 0.560701, places=5)
        self.assertTrue(metrics["pair_option"]["available"])

    def test_round_68_break_even_inventory(self) -> None:
        # Lower tiers are left at 10% of initial.  This reproduces the
        # sensitivity calculation discussed in the product methodology.
        record = make_record(
            "SP2000",
            2_000,
            40_000_000,
            100,
            [
                (1_000_000_000, 8, 3),
                (100_000_000, 24, 1),
                (10_000_000, 200, 20),
                (20_000, 110_000, 11_000),
                (4_000, 2_800_000, 280_000),
                (2_000, 11_200_000, 1_120_000),
            ],
        )
        metrics = calculate_round_metrics(record)
        expected = (
            3 * net_prize(1_000_000_000, 2_000)
            + net_prize(100_000_000, 2_000)
            + 20 * net_prize(10_000_000, 2_000)
            + 11_000 * 20_000
            + 280_000 * 4_000
            + 1_120_000 * 2_000
        ) / 2_000
        self.assertAlmostEqual(
            metrics["break_even"]["all_prizes_max_unresolved"],
            expected,
        )
        self.assertEqual(metrics["tiers"][0]["remaining"], 3)
        self.assertTrue(metrics["pair_option"]["odd_remaining_signal"])

    def test_first_zero_classification(self) -> None:
        record = make_record(
            "SP500",
            500,
            4_000_000,
            100,
            [
                (200_000_000, 1, 0),
                (1_000_000, 20, 1),
                (5_000, 60_000, 6_000),
                (500, 1_200_000, 120_000),
            ],
        )
        metrics = calculate_round_metrics(record)
        self.assertEqual(metrics["decision"]["code"], "first-zero")


if __name__ == "__main__":
    unittest.main()
