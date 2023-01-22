"""Checks light, if green, says go """

light: str = input("What color is the light? ").lower()

if (light == "green"):
    print("Go!")
    print("Drive safe!")
else:
    if(light != "red"):
        print("Go report this")
    else:
        print("Stop!")
print("Don't look at your phone!")