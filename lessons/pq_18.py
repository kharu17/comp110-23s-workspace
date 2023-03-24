def value_exists(xs: dict[str, int], x: int) -> bool:
    for num in xs:
        if x == xs[num]:
            return True
    return False