def evaluate_game(user_choice, computers_choice):
    if user_choice == computers_choice:
        return None
    elif user_choice == 'Rock' and computers_choice == 'Scissor':
        return True
    elif user_choice == 'Scissor' and computers_choice == 'Paper':
        return True
    elif user_choice == 'Paper' and computers_choice == 'Rock':
        return True
    elif user_choice == 'Paper' and computers_choice == 'Scissor':
        return False
    elif user_choice == 'Scissor' and computers_choice == 'Rock':
        return False
    elif user_choice == 'Rock' and computers_choice == 'Paper':
        return False
