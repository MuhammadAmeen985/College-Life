# Python Practice Exercises

**Author:** Muhammad Ameen  
**Topic:** Functions, Mathematics, Type Hints, and Error Handling

## Beginner Level

### Exercise 1: Fahrenheit to Celsius
Write a function that converts a temperature from Fahrenheit to Celsius.

Formula: `C = (F - 32) × 5 / 9`

### Exercise 2: Celsius to Fahrenheit
Write a function that converts Celsius to Fahrenheit.

Formula: `F = (C × 9 / 5) + 32`

### Exercise 3: Celsius to Kelvin
Write a function that converts Celsius to Kelvin.

Formula: `K = C + 273.15`

### Exercise 4: Kelvin to Celsius
Write a function that converts Kelvin to Celsius.

Formula: `C = K - 273.15`

### Exercise 5: Safe Division
Write a function that divides two numbers. Raise a `ValueError` if the denominator is zero.

### Exercise 6: Square of a Number
Write a function that accepts a number and returns its square.

Example: `square(5)` → `25`

## Intermediate Level

### Exercise 7: Circle Area
Write a function that calculates the area of a circle using `math.pi`.

Formula: `A = πr²`

Raise a `ValueError` if the radius is negative.

### Exercise 8: Circle Circumference
Write a function that calculates the circumference of a circle.

Formula: `C = 2πr`

### Exercise 9: Rectangle Area
Write a function that calculates the area of a rectangle using its length and width.

Raise a `ValueError` if either dimension is negative.

### Exercise 10: Average of Three Numbers
Write a function that accepts three numbers and returns their average.

### Exercise 11: Power Calculator
Write a function that calculates a number raised to a specified power.

Example: `power(2, 3)` → `8`

### Exercise 12: Safe Square Root
Write a function that returns the square root of a number using `math.sqrt()`.

Raise a `ValueError` if the input is negative.

## Practical Engineering Level

### Exercise 13: RPM to Angular Velocity
Convert rotational speed from revolutions per minute (RPM) to radians per second.

Formula: `ω = RPM × 2π / 60`

### Exercise 14: Calculate Mechanical Power
Calculate rotational mechanical power from torque and angular velocity.

Formula: `P = T × ω`

Where:
- `P` = power in watts
- `T` = torque in newton-metres
- `ω` = angular velocity in radians per second

### Exercise 15: Pressure Conversion
Convert pressure from bar to pascals.

Formula: `Pressure (Pa) = Pressure (bar) × 100000`

### Exercise 16: Engineering Unit Converter
Create a function that converts a temperature between Celsius and Fahrenheit based on a user-selected conversion direction.

Accept `"C"` to convert Celsius to Fahrenheit and `"F"` to convert Fahrenheit to Celsius. Raise a `ValueError` for an unsupported direction.

## Practice Requirements

For each exercise:

1. Write a function with a meaningful name.
2. Add a docstring explaining what it does.
3. Use type hints where appropriate.
4. Handle invalid inputs when necessary.
5. Test at least three inputs, including an edge case.
6. Commit your solution to GitHub with a meaningful commit message.
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
