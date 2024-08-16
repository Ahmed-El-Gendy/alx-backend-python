#!/usr/bin/env python3
"""
Type-annotated function
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """To tuple"""
    return (k, float(v**2))
