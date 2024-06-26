from flask import Flask

app = Flask(__name__)

try:
    with open("scores.txt", 'r') as file:
        score = file.read()
except Exception:
    score = "Error"
@app.route("/")
def hello_world():
    return (f"""
    <html>
        <head>
            <title>Score Game</title>
        </head>
        <body>
            <h1>The score is:</h1>
            <div id="score"> {score} </div>
        </body>
    </html>


    """)

@app.errorhandler(Exception)
def handle_exception(e):
    return (f"""
    <html>
        <head>
            <title>Score Game - Error</title>
        </head>
        <body>
            <h1>Error</h1>
            <div id="score"> Error </div>
        </body>
    </html>
    """),


if __name__ == '__main__':
    app.run(port=5000)