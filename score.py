import os

# Points_Of_Winning = (Difficulty x 3) + 5

def add_score(Difficulty):
    if not os.path.exists('scores.txt'):
        with open('scores.txt', 'w') as file:
            file.write('0')

    with open("scores.txt", 'r') as file:
        content = file.read().strip()

    with open('scores.txt', 'w') as file:
        score = (Difficulty * 3) + 5 + int(content)
        file.write(str(score))


