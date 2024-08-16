#!/usr/bin/env python3
"""
    Duck
"""
from typing import Sequence, Optional, Any


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Make list of any"""
    if lst:
        return lst[0]
    else:
        return None
