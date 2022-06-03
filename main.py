import time

from get_computers_choice import get_computers_choice


def play_game():
    choice = input('Do you want to pick Rock, Paper or Scissors?')
    computers_choice = get_computers_choice()
    print("Okay, got it! Wait for it...")
    time.sleep(3)
    print("Your choice was:", choice)
    print("Computers choice was:", computers_choice)


def start_new_game():
    name = input('Enter your name: ')
    print(f'Okay ',name, f', here we go!')
    play_game()


def main():
    print(f'Welcome to Rock, Paper and Scissors! Best of luck!')
    time.sleep(1)
    start_new_game()


main()
