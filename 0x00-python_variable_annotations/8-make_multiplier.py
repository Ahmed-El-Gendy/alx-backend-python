#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make mul function"""
    def multiplier_function(value: float) -> float:
        """Mul function"""
        return value * multiplier
    return multiplier_function
