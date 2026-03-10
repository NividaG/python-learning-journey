# utils.py

def apply_discount(price: float, discount_percent: float) -> float:
    return price - (price * discount_percent / 100)


def clean_text(text: str) -> str:
    return text.strip().lower()
