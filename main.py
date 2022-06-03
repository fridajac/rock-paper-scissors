import time

from evaluate_game import evaluate_game
from get_computers_choice import get_computers_choice


def play_game():
    user_choice = input('Do you want to pick Rock, Paper or Scissors?')
    print("Okay, you are playing with", user_choice, ". Wait for it...")
    print()
    computers_choice = get_computers_choice()
    time.sleep(3)
    print("You played with:", user_choice)
    print("The computer played with:", computers_choice)
    result = evaluate_game(user_choice, computers_choice)
    if result is None:
        print("It was a draw, go again!")
    elif result is True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost!")


def start_new_game():
    name = input('Enter your name: ')
    print(f'Okay ',name, f', here we go!')
    play_game()


def main():
    print(f'Welcome to Rock, Paper and Scissors! Best of luck!')
    time.sleep(1)
    start_new_game()


main()
