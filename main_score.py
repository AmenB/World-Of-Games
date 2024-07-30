from flask import Flask

app = Flask(__name__)

try:
    with open("scores.txt", 'r') as file:
        score = file.read()
except Exception:
    score = "Error: 404"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)