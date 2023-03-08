"""Unit tests for functions utilizing lists."""
__author__ = "730459195"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import concat

def test_empty() -> None:
    """Tests list that is returned if given list is empty."""
    assert only_evens([]) == []

def test_all_evens() -> None:
    """Tests list that is returned if elements of given list are all even."""
    test_list: list[int] = [2, 4, 6]
    assert only_evens(test_list) == [2, 4, 6]

def test_all_odds() -> None:
    """Tests list that is returned if one of the elements of given list is even."""
    test_list: list[int] = [1, 3, 6]
    assert only_evens(test_list) == [6]

def test_empty() -> None:
    """Tests list that is returned if given lists are empty."""
    assert concat([]) == []

def test_many_with_one() -> None:
    """Tests list that is returned if first given list has many elements and second list only has one."""
    test_list



