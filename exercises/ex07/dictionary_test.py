"""Dictionary Functions Tests."""
__author__ = "730607227"

import pytest
from dictionary import invert, favorite_color, count


def test_invert_one_element() -> None:
    """Testing invert on one element."""
    assert invert({"1": "3"}) == {"3": "1"}


def test_invert_duplicate_values() -> None:
    """Testing the Key Error on invert."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_multiple_elements() -> None:
    """Testing invert with multiple elements."""
    assert invert({"1": "3", "3": "2", "5": "5", "8": "4"}) == {"3": "1", "2": "3", "5": "5", "4": "8"}


def test_favorite_color_default() -> None:
    """Using the example case on favorite color."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_tie() -> None:
    """Testing faavorite color on a tie."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Jordan": "yellow"}) == "yellow"


def test_favorite_color_four_colors() -> None:
    """Testing favorite color with 4 colors."""
    assert favorite_color({"Marc": "yellow", "Alex": "blue", "Jordan": "green", "Kevin": "red", "Josh": "blue", "David": "blue", "Renee": "red"}) == "blue"


def test_count_all_same_element() -> None:
    """Testing count with one unique element."""
    assert count(["1", "1", "1", "1", "1", "1", "1"]) == {"1": 7}


def test_count_different_elements() -> None:
    """Testing normal case for count."""
    assert count(["1", "2", "3", "4", "1", "2", "2", "1", "3", "1"]) == {"1": 4, "2": 3, "3": 2, "4": 1}


def test_count_same_count() -> None:
    """Testing when all strings appear the same amount."""
    assert count(["a", "b", "c", "c", "b", "a"]) == {"a": 2, "b": 2, "c": 2}