#!/usr/bin/env python3
from typing import Tuple, Union
"""
Type-annotated function
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, float(v**2))
