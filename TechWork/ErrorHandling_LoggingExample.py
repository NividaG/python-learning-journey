import logging

logging.basicConfig(level=logging.INFO)

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

try:
    result = divide(10, 0)
    print(result)
except ValueError as e:
    logging.error("Calculation failed: %s", e)