#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum list"""
    return float(sum(mxd_lst))
