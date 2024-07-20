import random
import time
import os
import utils
import score

def generate_sequence(difficulty):
    random_list = []
    for i in range(difficulty):
        random_list.append(random.randint(1,101))
    print(random_list)
    time.sleep(0.7)
    utils.Screen_cleaner()
    return random_list

def get_list_from_user(difficulty):
    while True:
        user_input = input(f"Enter a list of the numbers separated by spaces: ")
        if user_input:
            user_list = user_input.split()
            user_list = [int(item) for item in user_list]
            return user_list
            break

def is_list_equal(random_list,user_random_list):
    if random_list == user_random_list:
        return True
    else:
        return False

def play(difficulty):
    random_list = generate_sequence(difficulty)
    user_random_list = get_list_from_user(difficulty)
    result = is_list_equal(random_list, user_random_list)
    if result is True:
        print("Your answer is correct")
        return True
    else:
        print("Your answer is wrong")
        return Fals
