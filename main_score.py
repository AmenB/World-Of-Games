from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    try:
        with open("scores.txt", 'r') as file:
            score = file.read()
    except Exception:
        score = "Error: 404"
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
