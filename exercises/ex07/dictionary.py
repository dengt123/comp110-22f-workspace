"""EX07 - Dictionary Functions."""
__author__ = "730607227"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Invert dictionary keys and values."""
    output_dict: dict[str, str] = {}
    for i in input_dict:
        if input_dict[i] in output_dict:
            raise KeyError("Key Error.")
        else:
            output_dict[input_dict[i]] = i
    return output_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Find the most popular favorite color."""
    color_popularity: dict[str, int] = {}
    most_popular: list[str,int] = ["", 0]
    for i in input_dict:
        if input_dict[i] in color_popularity:
            color_popularity[input_dict[i]] += 1
        else:
            color_popularity[input_dict[i]] = 1
    for i in color_popularity:
        if color_popularity[i] > most_popular[1]:
            most_popular[0], most_popular[1] = i, color_popularity[i]
    return most_popular[0]
    

def count(input_list: list[str]) -> dict[str: int]:
    """Count the appearances by an element in a list."""
    output_dict: dict[str, int] = {}
    for i in input_list:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict