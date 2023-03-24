"""Challenge Question 04"""
__author__ = "730459195"

def zip (list1: list[str] , list2: list[int]) -> dict[str, int]: 
    """Produces a dictionary where the first list is the keys and the second list is the corresponding values."""
    zip_list: dict[str, int] = {}
    if len(list1) != len(list2) or len(list1) == 0 or len(list2) == 0:
        return {}
    for i in range(len(list1)):
        zip_list[list1[i]] = list2[i]
    return zip_list

print(zip(["w","t","d"], [1, 2, 3]))