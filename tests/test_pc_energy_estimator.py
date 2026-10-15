"""Regression tests for the VORLI offline energy estimator."""
import sys
from pathlib import Path
import unittest
from decimal import Decimal

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from pc_energy_estimator import estimate_pc_cost

BASE = dict(active_watts=120, standby_watts=0, active_hours_per_day=4,
            standby_hours_per_day=0, days_per_year=220, electricity_eur_per_kwh="0.30")

class EnergyTests(unittest.TestCase):
    def test_desktop(self):
        self.assertEqual(estimate_pc_cost(**BASE)["energy_eur_per_year"], Decimal("31.68"))

    def test_laptop(self):
        self.assertEqual(estimate_pc_cost(**{**BASE, "active_watts":45})["energy_eur_per_year"], Decimal("11.88"))

    def test_standby(self):
        value=estimate_pc_cost(**{**BASE, "standby_watts":2, "standby_hours_per_day":8,
                                  "purchase_eur":500, "maintenance_3y_eur":40})
        self.assertEqual(value["total_eur_3_years"], Decimal("638.21"))

    def test_zero(self):
        self.assertEqual(estimate_pc_cost(**{**BASE, "days_per_year":0})["total_kwh_per_year"], 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            estimate_pc_cost(**{**BASE, "active_watts":-1})

    def test_nan(self):
        with self.assertRaises(ValueError):
            estimate_pc_cost(**{**BASE, "electricity_eur_per_kwh":"NaN"})

    def test_boolean(self):
        with self.assertRaises(ValueError):
            estimate_pc_cost(**{**BASE, "days_per_year":True})

    def test_overlapping_hours(self):
        with self.assertRaises(ValueError):
            estimate_pc_cost(**{**BASE, "active_hours_per_day":17, "standby_hours_per_day":8})

    def test_fractional_days(self):
        with self.assertRaises(ValueError):
            estimate_pc_cost(**{**BASE, "days_per_year":20.5})

    def test_days_over_year(self):
        with self.assertRaises(ValueError):
            estimate_pc_cost(**{**BASE, "days_per_year":367})
