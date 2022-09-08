"""EX04 - list utility functions."""

__author__ = "730607227"

def all(inputList: list[int], checkNumber: int) -> bool:
    """check if all elements of a list are equal to the check number."""
    if len(inputList) == 0:
        return False
    i: int = 0
    while i < len(inputList):
        if checkNumber != inputList[i]:
            return False
        i += 1
    return True

def max(input: list[int]) -> int:
    """find the maximum value in a list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max: int = input[0]
    i: int = 0
    while i < len(input):
        if input[i] > max:
            max = input[i]
        i += 1
    return max

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """return true if lists are equal, false otherwise"""
    if len(list1) != len(list2):
        return False
    i: int = 0
    while i < len(list1):
        if list1[i] != list2[i]:
            return False
        i += 1
    return True