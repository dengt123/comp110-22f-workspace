"""EX05 - Tests for the list utility functions."""

__author__ = "730607227"


from utils import only_evens, sub, concat


def test_only_evens_empty_list() -> None:
    """Testing if the empty list returns nothing."""
    assert only_evens([]) == []


def test_only_evens_normal_list() -> None:
    """Testing a list with evens and odds."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens_full_even() -> None:
    """Testing a list with only evens."""
    assert only_evens([2, 6, 10, 8]) == [2, 6, 10, 8]


def test_concat_first_list_empty() -> None:
    """Testing concatnate with an empty first list."""
    assert concat([], [1, 3, 5, 2, 8]) == [1, 3, 5, 2, 8]


def test_concat_two_lists() -> None:
    """Testing concatnate on two lists."""
    assert concat([1, 3, 2, 7], [5, 8, 2, 9]) == [1, 3, 2, 7, 5, 8, 2, 9]


def test_concat_two_more_lists() -> None:
    """Testing concatenate on more lists."""
    assert concat([1, 92, 35, 83, 728], [82, 18, 79, 298]) == [1, 92, 35, 83, 728, 82, 18, 79, 298]


def test_sub_negative_start() -> None:
    """Testing with a negative start index."""
    assert sub([1, 2, 3],-3, 2) == [1, 2]


def test_sub_example() -> None:
    """Testing the given example."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_long_case() -> None:
    """Testing a case with a long list."""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 8) == [4, 5, 6, 7, 8]
