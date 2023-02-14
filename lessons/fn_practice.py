"""Example functions to learn definition and calling syntax"""

def my_max(number1: int, number2: int) -> int:
    """Returns max value out of 2 numbers"""
    if number1 >= number2:
        return number1
    else:
        return number2

max_number: int = my_max(1,10)
print(max_number)