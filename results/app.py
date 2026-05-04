from flask import Flask, jsonify
import psycopg2
import time

app = Flask(__name__)

def get_conn():
    while True:
        try:
            conn = psycopg2.connect(
                host="postgres",
                database="votes",
                user="postgres",
                password="postgres"
            )
            return conn
        except Exception as e:
            print("Waiting for PostgreSQL...", e)
            time.sleep(5)

@app.route('/results')
def results():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT choice, COUNT(*) FROM votes GROUP BY choice;")
    rows = cur.fetchall()

    result = {row[0]: row[1] for row in rows}

    return jsonify(result)

@app.route('/')
def home():
    return "Results service is running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
