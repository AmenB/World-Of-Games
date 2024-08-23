from flask import Flask
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'mysql-container',  # Use the name of the MySQL container
    'user': 'root',  # MySQL username
    'password': 'root',  # MySQL password
    'database': 'db'  # Database name (ensure this is correct)
}

@app.route("/")
def hello_world():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute a query to get the score
        cursor.execute("SELECT Name, Score FROM score LIMIT 1;")
        result = cursor.fetchone()

        if result:
            name, score = result
            score_display = f"{name}: {score}"
        else:
            score_display = "No score found."

        # Close the cursor and connection
        cursor.close()
        connection.close()
    except Error as e:
        score_display = f"Error: {str(e)}"

    return (f"""
    <html>
        <head>
            <title>Score Game</title>
        </head>
        <body>
            <h1>The score is:</h1>
            <div id="score"> {score_display} </div>
        </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
