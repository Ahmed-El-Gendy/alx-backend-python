#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test the access_nested_map function
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: dict,
            path: Tuple,
            expected: Union[Dict, int],
            ) -> None:
        """
        Test that the function returns the expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
