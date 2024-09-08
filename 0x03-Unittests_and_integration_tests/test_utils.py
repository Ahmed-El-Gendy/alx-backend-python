#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock
import requests


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

    @parameterized.expand([
        ({}, ('a',), KeyError),
        ({'a': 1}, ('a', 'b'), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: dict,
            path: Tuple,
            expected: Exception,
            ) -> None:
        """
        Test that the function raises the expected exception
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test the get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: dict,
            ) -> None:
        """
        Test that the function returns the expected value
        """
        with patch("requests.get") as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            assert get_json(test_url) == test_payload
            mock_get.assert_called_once_with(test_url)
