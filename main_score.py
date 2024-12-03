from flask import Flask
from prometheus_client import start_http_server, Summary, generate_latest, CONTENT_TYPE_LATEST
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Start Prometheus metrics server on a separate port (e.g., 5001)
start_http_server(5001)

# Database connection configuration
db_config = {
    'host': 'mysql-container',
    'user': 'root',
    'password': 'root',
    'database': 'db'
}

@app.route("/")
def hello_world():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Execute a query to get all users and their scores
        cursor.execute("SELECT Name, Score FROM score;")
        results = cursor.fetchall()

        if results:
            # Prepare the display of all users and scores
            score_display = "<ul>"
            for name, score in results:
                score_display += f"<li>{name}: {score}</li>"
            score_display += "</ul>"
        else:
            score_display = "No scores found."

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
            <h1>All Scores:</h1>
            <div id="score"> {score_display} </div>
        </body>
    </html>
    """)

@app.route("/metrics")
def metrics():
    # Generate and return the latest metrics for Prometheus
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
