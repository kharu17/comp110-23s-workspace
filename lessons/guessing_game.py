"""Ask user for number, give hints about number if wrong"""

SECRET: int = 10  #all caps means constant value 
guess: int = int(input("Guess a number! "))
playing: bool = True 

while playing: 
    if guess == SECRET:
        print("Correct!")
        playing = False 
    else:
        if guess % 2 == 1:
            print("Your guess is odd. The answer is even. ")
        if guess < SECRET:
            print("Too low")
        else: #guess > SECRET
            print("Too high")
        guess = int(input("Wrong guess, try again. "))



    