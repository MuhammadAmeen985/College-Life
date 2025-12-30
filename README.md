# College-Life
daily exercise 
Author Muhammad Ameen
# Learning Plan & How to Use this Repository

Welcome! This repository will hold exercises, notes, and small projects as you learn to code.

Getting started:
1. Choose your primary track: Python (recommended for beginners) or JavaScript (for web).
2. Install required tools:
   - VS Code: https://code.visualstudio.com/
   - Git: https://git-scm.com/
   - Python: https://python.org/ (if learning Python)
   - Node.js: https://nodejs.org/ (if learning JavaScript)
3. Create a folder for exercises: `exercises/`
4. Commit your practice files often and write short commit messages.

Suggested structure:
- README.md (project description)
- LEARNING-PLAN.md (this file)
- exercises/
  - python/
  - javascript/
  - projects/

Use this repo to store code, notes, and small projects. If you want, I can help create branches, add exercises, or set up GitHub Pages for your portfolio.
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
