import games.currency_roulette_game as currency_roulette_game
import games.guess_game as guess_game
import games.memory_game as memory_game
import score

def welcome():
    while True:
        username = input("Enter your Name\n")
        if len(username) >= 1 and username.isalpha():
            print (f"Hi {username} and welcome to the World of Games: The Epic Journey")
            break
        else:
            print("Please enter your real name\n")
def start_play():
    while True:
        game_number = input("""Please choose a game to play: 
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")
        if game_number.isdigit and (game_number == '1' or game_number == '2' or game_number == '3'):
            break
        else:
            print("Please enter only one number from the list\n")
    while True:
        difficulty = input("select a difficulty level between 1 and 5:\n")
        if difficulty.isdigit and (difficulty=='1' or difficulty=='2' or difficulty=='3' or difficulty=='4' or difficulty=='5'):
            break
        else:
            print("Please enter only one number from the list\n")
    if game_number == '1':
        result = memory_game.play(int(difficulty))
    elif game_number == '2':
        result = guess_game.play(int(difficulty))
    elif game_number == '3':
        result = currency_roulette_game.play(int(difficulty))
    if result == True:
        score.add_score(int(difficulty))
    while input("Do you want to try again? press 'y' to continue or 'n' to leave: ") == "y":
        start_play()
    else:
        exit()






