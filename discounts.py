# discounts.py
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Tuple, List

@dataclass
class Discount:
    code: str
    type: str                 # "percent" or "amount"
    value: float
    min_purchase: float = 0.0
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    stackable: bool = False

def is_discount_valid(
    discount: Discount,
    cart_total: float,
    applied_codes: List[str],
    now: datetime,
) -> Tuple[bool, Optional[str]]:
    if cart_total < 0:
        return False, "invalid_cart_total"
    if discount.type not in {"percent", "amount"}:
        return False, "invalid_type"

    if discount.type == "percent":
        if discount.value < 0 or discount.value > 100:
            return False, "invalid_percent"
    else:  # amount
        if discount.value < 0:
            return False, "invalid_amount"
        if discount.value > cart_total:
            return False, "amount_exceeds_total"

    if cart_total < discount.min_purchase:
        return False, "below_min_purchase"

    if discount.start and now < discount.start:
        return False, "not_started"
    if discount.end and now > discount.end:
        return False, "expired"

    if not discount.stackable and applied_codes:
        return False, "not_stackable"

    return True, None
