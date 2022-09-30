__author__ = "730607227"

from random import randint

points: int = 0
player: str
CLAPPING_HANDS: str = "\U0001F44F"

def main() -> None:
    global points
    game_active = True
    greet()
    while game_active == True:
        print(f"You have {points} points.")
        choice: str = input(f"What would you like to do, {player}? \n A) Streak Mode \n B) Free Play \n C) Exit \n")
        if choice == "A":
            points = start_streak(points)
        elif choice == "B":
            start_game()
        elif choice == "C":
            print(f"Goodbye! You have scored {points} points. Please come back again!")
            game_active = False
        else:
            print("Invalid input! Try again!")
    

def greet() -> None:
    global player
    print("Welcome to this coinflip simulator. Your points will be based on the number of coinflips you can accurately predict.")
    player = input("What is your name? ")


def start_streak(points: int) -> int:
    streak: int = 0
    streak_alive = True
    while streak_alive:
        coinflip = randint(1,2)
        guess = int(input(f"{player}, would you like to guess 1) Heads or 2) Tails? "))
        if guess == coinflip:
            streak += 1
            print(f"Your guess was correct! {CLAPPING_HANDS} Your streak has been extended to {streak}.")
        else:
            streak_alive = False
            print(f"Your guess was incorrect. Your final streak was {streak}.")
    return points + streak


def start_game() -> None:
    global points
    coinflip = randint(1,2)
    guess = int(input(f"{player}, would you like to guess 1) Heads or 2) Tails? "))
    if guess == coinflip:
        print(f"Your guess was correct! {CLAPPING_HANDS}")
        points += 1
    else:
        print("Your guess was incorrect.")

if __name__ == "__main__":
    main()