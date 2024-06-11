import random

import freecurrencyapi
import requests


def get_money_interval(difficulty):
    print(f"your difficulty level is {difficulty}")
    client = freecurrencyapi.Client('v1/latest?apikey=fca_live_UpnzHxsb9EE7AeaQJkBR6osSRzDK1OAfw5Ynd6Es')
    resp = requests.get("https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_UpnzHxsb9EE7AeaQJkBR6osSRzDK1OAfw5Ynd6Es")
    data = resp.json()
    random_number = random.randint(1, 100)
    sum = int(data["data"]["ILS"] * random_number)
    if difficulty == 5:
        difficulty = 1
    elif difficulty==4:
        difficulty=2
    elif difficulty==2:
        difficulty=4
    elif difficulty==1:
        difficulty=5
    minimum = sum - difficulty
    maximum = sum + difficulty
    return (random_number,minimum, maximum)


def get_guess_from_user(dollar):
    while True:
        user_input = input(f"How much the value for {dollar}$ in ILS ")
        if user_input.isdigit():
            return int(user_input)
            break

def compare_results(user_input,minimum,maximum):
    if user_input <= maximum and user_input >= minimum:
        return True
    else:
        return False

def play (difficulty):
    dollar, minimum, maximum = get_money_interval(difficulty)
    user_input = get_guess_from_user(dollar)
    result = compare_results(user_input,minimum,maximum)
    print(result)


