#user_name: str = input("What is your name? ")
#print("Hello, "+user_name+" good morning")


#def katelyn(age: int,name: str) -> str:
    #string: str = f"{name} is {age} years old."
    #return string

#rat = katelyn(20,"bryan")
#print(rat)


#s: dict[int, int] = {}

#i: int = 1
#while i < 5:
    #s[1 ** 2] = i
    #i += 1

#print(s)

def shrink(xs: dict[str, int]) -> list[int]:
    new_list: list[int] = []
    for x in xs:
        if xs[x] % 2 == 0 and xs[x] < 18:
            new_list.append(xs[x])
    return new_list

y = shrink({"h": 4, "b": 20})
print(y)