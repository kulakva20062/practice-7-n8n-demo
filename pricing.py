"""Minimal price calculations for the n8n demo."""


def line_total(unit_cents: int, quantity: int) -> int:
    if quantity < 0:
        raise ValueError("quantity must be non-negative")
    return unit_cents * quantity


def subtotal(*amounts: int) -> int:
    return sum(amounts)


def format_cents(value: int) -> str:
    return f"{value / 100:.2f}"


def discount(value: int, percentage: int) -> int:
    return value * (100 - percentage) // 100


def savings(value: int, percentage: int) -> int:
    return value - discount(value, percentage)
