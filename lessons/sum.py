""""Example function for unit tests using for...in range(...) loop"""

def sum(xs: list[float]) -> float:
    """returns sum of all elements in xs"""
    sum_total: float = 0.0
    idx: int = 0
    for idx in range(0, len(xs)):
        sum_total += xs[idx]
        idx += 1
    return sum_total