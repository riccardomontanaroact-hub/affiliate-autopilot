"""Offline illustrative computer energy cost estimator for VORLI.

Average watts must be measured at the wall. Activity and standby hours are
disjoint and refer to the same days of use. No network or payment features.
"""
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def _value(value, name):
    if isinstance(value, bool):
        raise ValueError(f"{name}: boolean not allowed")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError(f"{name}: invalid number") from None
    if not result.is_finite() or result < 0:
        raise ValueError(f"{name}: must be finite and nonnegative")
    return result


def estimate_pc_cost(*, active_watts, standby_watts, active_hours_per_day,
                     standby_hours_per_day, days_per_year,
                     electricity_eur_per_kwh, purchase_eur=0,
                     maintenance_3y_eur=0):
    """Return Decimal kWh/year, annual energy EUR, and three-year total EUR.

    Assumes the same use and electricity price for all three years.
    Consumption on uncounted days is excluded; include peripherals in watts.
    """
    raw = locals()
    v = {key: _value(value, key) for key, value in raw.items()}
    if v['active_hours_per_day'] + v['standby_hours_per_day'] > 24:
        raise ValueError('Activity plus standby exceeds 24 hours per day')
    if v['days_per_year'] != v['days_per_year'].to_integral_value():
        raise ValueError('Days of use must be a whole number')
    if v['days_per_year'] > 366:
        raise ValueError('Days of use exceeds 366 per year')
    active = v['active_watts'] * v['active_hours_per_day'] * v['days_per_year'] / 1000
    standby = v['standby_watts'] * v['standby_hours_per_day'] * v['days_per_year'] / 1000
    total = active + standby
    annual_exact = total * v['electricity_eur_per_kwh']
    three_year_exact = v['purchase_eur'] + 3 * annual_exact + v['maintenance_3y_eur']
    money = lambda amount: amount.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return {'active_kwh_per_year': active, 'standby_kwh_per_year': standby,
            'total_kwh_per_year': total, 'energy_eur_per_year': money(annual_exact),
            'total_eur_3_years': money(three_year_exact)}
