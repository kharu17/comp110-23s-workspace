"""Functions utilizing lists."""
__author__ = "730459195"


def only_evens(num_list: list[int]) -> list:
    """Returns a list of even numbers given a list of integers."""
    even = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
    return even


def concat(list1: list[int], list2: list[int]) -> list:
    """Returns all elements of the first list, followed by all elements of the second list."""
    big = []
    for i in range(len(list1)):
        big.append(list1[i])
    for i in range(len(list2)):
        big.append(list2[i])
    return big


def sub(list: list[int], start: int, end: int) -> list:
    """Returns a list defined by a given start and end index (non-inclusive)."""
    sub = []
    if len(list) == 0 or start >= len(list) or end <= 0:
        return []
    for i in range(len(list)):
        if i >= start and i < end:
            sub.append(list[i])
    return sub 
