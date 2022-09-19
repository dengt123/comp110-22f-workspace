"""EX05 - list utility functions."""

__author__ = "730607227"


def only_evens(input_list: list[int]) -> list[int]:
    """Returning even elemnts from a list."""
    output: list[int] = []
    for i in input_list:
        if i % 2 == 0:
            output.append(i)
    return output


def concat(input_one: list[int], input_two: list[int]) -> list[int]:
    """Returning the second list after the first in one list."""
    output: list[int] = []
    for i in input_one:
        output.append(i)
    for j in input_two:
        output.append(j)
    return output


def sub(input_list: list[int], start: int, end: int) -> list[int]:
    """Creating a subset from the start to the end index."""
    output: list[int] = []
    if len(input_list) == 0 or start > len(input_list) or end <= 0:
        return output
    if start < 0:
        start = 0
    if end > len(input_list): 
        end = len(input_list)
    for i in range(start, end):
        output.append(input_list[i])
    return output
    
