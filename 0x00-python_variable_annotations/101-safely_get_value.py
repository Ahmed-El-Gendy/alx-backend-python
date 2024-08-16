#!/usr/bin/env python3
"""
    Type var
"""
from typing import TypeVar, Mapping, Union, Any
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Type var"""
    if key in dct:
        return dct[key]
    else:
        return default
