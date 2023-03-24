"""Unit tests for functions utilizing lists."""
__author__ = "730459195"

from exercises.ex05.utils import only_evens, sub, concat


def test_empty_list() -> None:
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
    assert concat([], []) == []


def test_many_with_one() -> None:
    """Tests list that is returned if first given list has multiple elements and second list only has one."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [4]
    assert concat(test_list1, test_list2) == [1, 2, 3, 4]


def test_many_with_many() -> None:
    """Tests list that is returned if first given list and second given list have multiple elements."""
    test_list1: list[int] = [1, 2, 3]
    test_list2: list[int] = [8, 9, 10]
    assert concat(test_list1, test_list2) == [1, 2, 3, 8, 9, 10]


def test_start_large() -> None:
    """Tests list that is returned if start index is larger than length of given list."""
    test_list: list[int] = [1, 2, 3]
    start: int = 5
    end: int = 1
    assert sub(test_list, start, end) == []


def test_start_one() -> None:
    """Tests list that is returned if start index is one."""
    test_list: list[int] = [1, 3, 5, 7]
    start: int = 1
    end: int = 3
    assert sub(test_list, start, end) == [3, 5]


def test_end_four() -> None:
    """Tests list that is returned if end index is four."""
    test_list: list[int] = [1, 3, 5, 7]
    start: int = 1
    end: int = 4
    assert sub(test_list, start, end) == [3, 5, 7]