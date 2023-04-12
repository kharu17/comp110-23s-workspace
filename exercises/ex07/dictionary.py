"""Functions utilizing dictionaries."""
__author__ = "730459195"


def invert(xs: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    invert: dict[str, str] = {}
    for x in xs:
        if (xs[x] in invert):
            raise KeyError
        invert[xs[x]] = x
    return invert


def favorite_color(cols: dict[str, str]) -> str:
    """Finds the most frequently favorited color."""
    freq: dict[str, int] = {}
    for name in cols:
        if cols[name] in freq:
            freq[cols[name]] += 1
        else:
            freq[cols[name]] = 1
    nam: str = ""
    freqen: int = 0
    for name in freq:
        if freq[name] > freqen:
            freqen = freq[name]
            nam = name
    return nam


def count(items: list[str]) -> dict[str, int]:
    """Returns a dictionary with all the unique items in a list and their frequency."""
    count: dict[str, int] = {}
    for item in items:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    return count