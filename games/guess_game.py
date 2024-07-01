import random
import utils
import score

def generate_number():
    return random.randint(0, 5)


def get_guess_from_user(difficulty):
    print(f"your difficulty level is {difficulty}")
    while True:
        user_input = input(f"Enter your guess from 0 to {difficulty} please: ")
        if user_input.isdigit() and int(user_input) >= 0 and int(user_input) <= difficulty:
            return int(user_input)
            break


def compare_results(user_input, secret_number):
    return True if user_input == secret_number else False


def play(difficulty):
    secret_number = generate_number()
    user_input = get_guess_from_user(difficulty)
    result = compare_results(user_input, secret_number)
    if result is True:
        print("Your answer is correct")
        return True
    else:
        print("Your answer is wrong")
        return False


