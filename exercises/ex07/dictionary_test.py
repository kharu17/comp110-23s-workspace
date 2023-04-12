"""Unit tests for functions utilizing dictionaries."""
__author__ = "730459195"
from dictionary import invert, favorite_color, count


def test_invert_edge() -> None:
    """Tests if invert function returns an empty dictionary given an empty dictionary."""
    assert invert({}) == {}


def test_invert_use() -> None:
    """Tests if invert function returns inverted dictionary given a dictionary with two keys."""
    assert invert({"12": "1", "31": "13"}) == {"1": "12", "13": "31"}


def test_invert_use1() -> None:
    """Tests if invert function returns inverted dictionary given a dictionary with three keys."""
    assert invert({"1": "2", "3": "4", "5": "6"}) == {"2": "1", "4": "3", "6": "5"}


def test_favcol_edge() -> None:
    """Tests if function returns empty string given an empty dictionary."""
    assert favorite_color({}) == ""


def test_favcol_use() -> None:
    """Tests if function returns color that appears first in given dictionary."""
    assert favorite_color({"joe": "blue"}) == "blue"


def test_favcol_use1() -> None:
    """Tests if function returns color that appears most frequently in given dictionary."""
    assert favorite_color({"joe": "blue", "bob": "blue", "amy": "red"}) == "blue"


def test_count_edge() -> None:
    """Tests if function returns empty dictionary given empty list."""
    assert count([]) == {}


def test_count_use() -> None:
    """Tests if function returns dictionary with counts of each number from given list."""
    assert count(["1", "1", "2", "5", "1"]) == {"1": "3", "2": "1", "5": "1"}


def test_count_use1() -> None:
    """Tests if function returns dictionary with counts of each number from given list."""
    assert count(["5", "5", "5", "5", "5", "5", "5", "1", "2", "3"]) == {"5": "7", "1": "1", "2": "1", "3": "1"}