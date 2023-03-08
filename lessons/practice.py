#user_name: str = input("What is your name? ")
#print("Hello, "+user_name+" good morning")


#def katelyn(age: int,name: str) -> str:
    #string: str = f"{name} is {age} years old."
    #return string

#rat = katelyn(20,"bryan")
#print(rat)



x: int = 1

def f(y: int) -> int:
    return x + y

print(f(x+1))
    
def only_evens(num_list: list[int]) -> list:
    """Returns a list of even numbers given a list of integers."""
    even = []
    for i in range(len(num_list)):
        if num_list[i] % 2 == 0:
            even.append(num_list[i])
    return even

def sub(list: list[int], start: int, end: int) -> list:
    sub = []
    for i in range(len(list)):
        if i >= end -1 or i < start -1:
            sub.append(list[i])
    return sub 

list: a_list
a_list = [10, 20, 30, 40]
sub(a_list, 1, 3)
print(sub)