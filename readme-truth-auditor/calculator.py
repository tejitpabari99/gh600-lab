def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def percentage(value: float, total: float) -> float:
    return divide(value, total) * 100