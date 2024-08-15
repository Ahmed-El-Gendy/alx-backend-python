from typing import List, Tuple, Iterable, Sequence
"""
    Duck
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
