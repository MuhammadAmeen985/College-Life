import math
from typing import Union


def fahrenheit_to_celsius(temp_f: Union[int, float]) -> float:
    """Convert Fahrenheit to Celsius."""
    return (temp_f - 32) * 5 / 9


def celsius_to_fahrenheit(temp_c: Union[int, float]) -> float:
    """Convert Celsius to Fahrenheit."""
    return (temp_c * 9 / 5) + 32


def safe_divide(numerator: float, denominator: float) -> float:
    """Safely divide two numbers."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return numerator / denominator
