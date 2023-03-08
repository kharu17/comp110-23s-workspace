"""EX 04 - Different functions utilizing lists."""
__author__ = "730459195"


def all(num_list: list[int], num: int) -> bool:
    """Checks if all numbers in a list are the same and returns result."""
    list_len: int = len(num_list)
    i: int = 0
    if list_len == 0:
        return False
    while i <= list_len - 1: 
        if num != num_list[i]:
            return False
        i += 1
    return True


def max(num_list: list[int]) -> int:
    """Returns the max value in a list."""
    list_len: int = len(num_list)

    if list_len == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    max_num: int = num_list[0]
    while i <= list_len - 1:
        current_num: int = num_list[i]
        if (current_num > max_num):
            max_num = current_num
        i += 1    
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Checks if two lists are the exact same and returns result."""
    if len(list1) != len(list2):
        return False
    list_len: int = len(list1)
    i: int = 0
    while i <= list_len - 1:
        if list1[i] != list2[i]:
            return False
        i += 1
    return True