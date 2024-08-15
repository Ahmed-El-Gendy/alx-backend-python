#!/usr/bin/env python3
from typing import Callable
"""
Type-annotated function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
