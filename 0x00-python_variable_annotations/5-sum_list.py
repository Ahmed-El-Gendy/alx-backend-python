#!/usr/bin/env python3
from typing import List
"""
Type-annotated function
"""


def sum_list(input_list: List[float]) -> float:
    """"List sum"""
    sum: float = 0.0
    for item in input_list:
        sum += item
    return sum
