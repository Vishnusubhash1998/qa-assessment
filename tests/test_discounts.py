import pytest
from datetime import datetime, timedelta
from discounts import Discount, is_discount_valid

NOW = datetime(2025, 1, 1, 12, 0, 0)

@pytest.mark.parametrize(
    "discount,cart_total,applied_codes,now",
    [
        (Discount("NEW10","percent",10, start=NOW-timedelta(days=1), end=NOW+timedelta(days=1)), 100.0, [], NOW),
        (Discount("SAVE5","amount",5, min_purchase=20, start=NOW-timedelta(days=7), end=NOW+timedelta(days=7), stackable=True), 25.0, ["WELCOME"], NOW),
        (Discount("FREEME","percent",100), 30.0, [], NOW),
        (Discount("ZERO","percent",0, stackable=True), 40.0, [], NOW),
    ],
    ids=["pct-10-ok", "amount-5-ok-stackable", "pct-100-free", "pct-0-trivial"]
)
def test_is_discount_valid_true(discount, cart_total, applied_codes, now):
    ok, err = is_discount_valid(discount, cart_total, applied_codes, now)
    assert ok is True
    assert err is None

@pytest.mark.parametrize(
    "discount,cart_total,applied_codes,now,expected_error",
    [
        (Discount("BADPCT","percent",150), 100.0, [], NOW, "invalid_percent"),
        (Discount("NEGPCT","percent",-1), 100.0, [], NOW, "invalid_percent"),
        (Discount("NEGAMT","amount",-5), 50.0, [], NOW, "invalid_amount"),
        (Discount("TOOBIG","amount",60), 50.0, [], NOW, "amount_exceeds_total"),
        (Discount("MIN50","amount",5, min_purchase=50), 49.99, [], NOW, "below_min_purchase"),
        (Discount("LATER","percent",10, start=NOW+timedelta(days=1)), 100.0, [], NOW, "not_started"),
        (Discount("OLD","percent",10, end=NOW-timedelta(seconds=1)), 100.0, [], NOW, "expired"),
        (Discount("EXCL","percent",10, stackable=False), 100.0, ["OTHER"], NOW, "not_stackable"),
        (Discount("WEIRD","bogo",1), 100.0, [], NOW, "invalid_type"),
        (Discount("ANY","amount",1), -5.0, [], NOW, "invalid_cart_total"),
    ],
    ids=[
        "pct>100","pct<0","amt<0","amt>cart",
        "below-min","not-started","expired",
        "not-stackable","bad-type","bad-cart"
    ]
)
def test_is_discount_valid_false(discount, cart_total, applied_codes, now, expected_error):
    ok, err = is_discount_valid(discount, cart_total, applied_codes, now)
    assert ok is False
    assert err == expected_error
