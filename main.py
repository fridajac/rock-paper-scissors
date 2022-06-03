import time

from evaluate_game import evaluate_game
from get_computers_choice import get_computers_choice



def check_score(user_score, computer_score):
    if user_score == 3:
        print("YOU WON THIS ROUND, with a score of", {user_score}, ":", {computer_score})
        return True
    if computer_score == 3:
        print("Sorry, the computer won this round with a score of", {user_score}, ":", {computer_score})
        return True
    return False


def play_game():
    user_score = 0
    computer_score = 0
    while True:
        while True:
            user_choice = input('Do you want to pick Rock, Paper or Scissor?')
            if user_choice == 'Scissor' or user_score == 'Rock' or user_score == 'Paper':
                break
            print("Bad input. Try again")
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
            user_score += 1
            print("YES, you won! Current score ", {user_score}, ":", {computer_score})
        else:
            computer_score += 1
            print("Sorry, you lost! Current score ", {user_score}, ":", {computer_score})
        if check_score(user_score, computer_score):
            break


def start_new_game():
    name = input('Enter your name: ')
    print(f'Okay ', name, f', here we go! Game is starting')
    play_game()


def main():
    print(f'Welcome to Rock, Paper and Scissors! Best of luck!')
    time.sleep(1)
    start_new_game()


main()
