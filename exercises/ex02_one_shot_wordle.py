"""EX 02 - Gussing a secret word in one shot."""
___author__ = "730459195"

SECRET: str = "python"
guess: str = str(input("What is your 6-letter guess? "))
playing: bool = True
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
letter_idx: int = 0 
boxes: str = ""

while letter_idx < 6:
    if (guess[letter_idx] == SECRET[letter_idx]):
        boxes = boxes + GREEN_BOX
    else:
        if guess[letter_idx] in SECRET:
            boxes = boxes + YELLOW_BOX
        else:
            boxes = boxes + WHITE_BOX
    letter_idx = letter_idx + 1


while playing:
    if guess == SECRET:
        print(boxes)
        print("Woo! You got it!")
        playing = False
    else:
        if (len(guess) != 6):
            guess = str(input("That was not 6 letters! Try again: "))
        if (len(guess) == 6):
            print(boxes)
            print("Not quite. Play again soon!")
            playing = False 


       
    

