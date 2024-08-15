#!/usr/bin/env python3
from typing import List, Union
"""
Type-annotated function
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return float(sum(mxd_lst))
