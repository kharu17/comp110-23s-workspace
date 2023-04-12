"""EX 08 - Functions related to wrangling data."""
__author__ = "730459195"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        #save every value under key "header"
        result.append(row[header])
    return result


def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dictionary with column header."""
    result: dict[str, list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
        #for each key, make a dictionary entry with all column values
        result[key] = column_values(table, key)
    return result


def head(table: dict[str,list[str]], rows: int) -> dict[str,list[str]]:
    """Produce a column-based table with only a certain number of rows of data for each column."""
    result: dict[str, list[str]] = {}
    for col in table:
        my_list: list[str] = []
        i: int = 0
        if len(table[col]) < rows:
            rows = len(table[col])
        while i < rows:
            my_list.append(table[col][i])
            i += 1
        result[col] = my_list
    return result


def select(table: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for val in table:
        if val in names:
            result[val] = table[val]
    return result


def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for col in table_1:
        result[col] = table_1[col]
    for col in table_2:
        if col in result:
            result[col] += table_2[col]
        else:
            result[col] = table_2[col]
    return result


def count(freq: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value in the given list and each value associated is the number of times it appeared in the input list."""
    result: dict[str, int] = {}
    for i in range(len(freq)):
        if freq[i] in result:
            result[freq[i]] += 1
        else:
            result[freq[i]] = 1
    return result


