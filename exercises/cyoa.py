"""Choose your own adventure game."""
__author__ = "730459195"

from random import randint

points: int 
player: str
LUCK: str = "\U0001F4AA"
WIN: str = "\U0001F973"
LOSE: str = "\U0001F635"


def greet() -> None:
    """Prints a welcome message and asks user for their name."""
    global LUCK
    print(f"Welcome! The goal of this game is to get 20 points in the least number of tries. Each turn, guess a number and you will either earn or lose points. Good luck! {LUCK}")
    greeting: str = input("Before getting started, enter your name: ")
    global player
    player = greeting


def level() -> None:
    """Allows user to choose their desired level of the game."""
    global points
    mode: str = input("Would you like to play on hard? (This subtracts 10 points on the first turn, which makes getting to 20 points more difficult) Type yes if wanted: ")
    if mode == "yes":
        points -= 10
        print("You have chosen to play on hard mode, you will start with -10 points")
    else:
        print("You have chosen to play on normal mode")
   

def branch_2(choice: int, points: int) -> int:
    """Determines if player choice gives or takes points from the point total."""
    if choice == 1 or choice == 2 or choice == 3:
        choice_1: int = randint(1, 3)
        if choice == choice_1:
            print("You just earned 10 points! ")
            points += 10
            print(f"Now you have {points} points.")
        else:
            print("You just lost 2 points ")
            points -= 2
            print(f"Now you have {points} points.")
    else:
        print("Try choosing a number from 1, 2, or 3.")
    return points
        

def main() -> None:
    """Main function that allows user to play game."""
    global points
    global player
    points = 0
    greet()
    level()
    global WIN
    global LOSE
    finish: int = 4
    choice: int = 0
    i: int = 0
    while choice != finish and points < 20:
        choice = int(input(f"Alright {player} pick a number from 1, 2, and 3. If you want to exit the game, type 4. "))
        if choice != finish:
            points = branch_2(choice, points)
        i += 1
    if points >= 20:
        print(f"Goodbye, you earned {points} points in {i} tries! See you later! {WIN}")
    else:
        print(f"Goodbye, you stopped at {points} points. {LOSE} ")


if __name__ == "__main__":
    main()