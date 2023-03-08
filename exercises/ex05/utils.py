"""Functions utilizing lists."""
__author__ = "730459195"

def only_evens(num_list: list[int]) -> list:
    """Returns a list of even numbers given a list of integers."""
    even = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
    return even

def concat(list1, list2):
    big = []
    for i in range(len(list1)):
        big.append(list1[i])
    for i in range(len(list2)):
        big.append(list2[i])
    return big

def sub(list, start, end):
    sub = []
    for i in range(len(list)):
        if i >= end -1 or i < start -1:
            sub.append(list[i])
    return sub 
