"""Price discount used by the skill-test bug path."""


def discount_price(price: int, percent: int) -> int:
    """Return price after a percent discount. percent is 0-100."""
    return price - (price * percent // 100)
