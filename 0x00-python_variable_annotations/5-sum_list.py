#!/usr/bin/env python3
from typing import List, Dict
"""
Type-annotated function
"""


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for item in input_list:
        sum += item
    return sum
