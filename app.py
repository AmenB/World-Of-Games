import games.currency_roulette_game as currency_roulette_game
import games.guess_game as guess_game
import games.memory_game as memory_game
import mysql.connector
from mysql.connector import Error


def welcome():
    while True:
        username = input("Enter your Name\n")
        if len(username) >= 1 and username.isalpha():
            print(f"Hi {username} and welcome to the World of Games: The Epic Journey")
            return username
        else:
            print("Please enter a valid name\n")


def start_play(username):
    while True:
        game_number = input("""Please choose a game to play: 
1. Memory Game - a sequence of numbers will appear for 1 second and you have to
guess it back.
2. Guess Game - guess a number and see if you chose like the computer.
3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n""")
        if game_number.isdigit() and game_number in ['1', '2', '3']:
            break
        else:
            print("Please enter only one number from the list\n")

    while True:
        difficulty = input("Select a difficulty level between 1 and 5:\n")
        if difficulty.isdigit() and difficulty in ['1', '2', '3', '4', '5']:
            break
        else:
            print("Please enter only one number from the list\n")

    difficulty = int(difficulty)

    if game_number == '1':
        result = memory_game.play(difficulty)
    elif game_number == '2':
        result = guess_game.play(difficulty)
    elif game_number == '3':
        result = currency_roulette_game.play(difficulty)

    if result:
        insert_score(username, difficulty + 5)

    while input("Do you want to try again? Press 'y' to continue or 'n' to leave: ").lower() == "y":
        start_play(username)  # Pass username to maintain context
    else:
        exit()


import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error

def insert_score(name, score):
    db_config = {
        'host': '127.0.0.1',  # Use localhost or 127.0.0.1 for local access
        'user': 'root',
        'password': 'root',
        'database': 'db'
    }

    connection = None
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            cursor = connection.cursor()

            # Check if the record exists
            cursor.execute("SELECT Score FROM score WHERE Name = %s", (name,))
            result = cursor.fetchone()

            if result:
                # Record exists, update the existing score
                current_score = result[0]
                new_score = current_score + score
                sql_query = "UPDATE score SET Score = %s WHERE Name = %s"
                values = (new_score, name)
            else:
                # Record does not exist, insert a new record
                sql_query = "INSERT INTO score (Name, Score) VALUES (%s, %s)"
                values = (name, score)

            # Execute the query
            cursor.execute(sql_query, values)

            # Commit the transaction
            connection.commit()
            print(f"Updated MySQL {name} with score {score}")

    except Error as e:
        print(f"Error: {str(e)}")

    finally:
        # Close the cursor and connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

