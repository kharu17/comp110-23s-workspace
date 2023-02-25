"""EX 03 - Gussing a secret word in one shot."""
__author__ = "730459195"

def contains_char(secret: str, guess: str) -> bool:
    """Checks if the inputted letter is one of the letters in the secret word."""
    assert len(guess) == 1
    index_guess = 0
    index_secret = 0
    while index_secret < len(secret):
        if(index_guess == len(guess)):
            index_guess = 0
            index_secret += 1
        if(index_secret < len(secret) and guess[index_guess] == secret[index_secret]):
            return True
        index_guess += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """ Returns a string which represents the guess and the status (white, yellow, green) of each letter."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    letter_idx: int = 0 
    boxes: str = ""

    while letter_idx < len(guess):
        if (guess[letter_idx] == secret[letter_idx]):
            boxes = boxes + GREEN_BOX
        else:
            index: int = 0
            if (contains_char(secret, guess[letter_idx])):
                boxes = boxes + YELLOW_BOX
            else:
                boxes = boxes + WHITE_BOX
        letter_idx = letter_idx + 1
    return boxes

def input_guess(num: int) -> str:
    """Asks for a valid input from the user based on the length of the secret word."""
    guess: str = str(input(f"Enter a {num} character word: "))
    while (len(guess) != num):
        guess = str(input(f"That wasn't {num} chars! Try again: "))
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret = "codes"
    turn = 1
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return
        turn += 1
    print("X/6 - Sorry, try again tomorrow!")
        
if __name__ == "__main__":
    main()