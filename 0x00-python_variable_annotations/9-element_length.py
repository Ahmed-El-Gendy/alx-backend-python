#!/usr/bin/env python3
"""
    Duck
"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Make list of Tuple"""
    return [(i, len(i)) for i in lst]
