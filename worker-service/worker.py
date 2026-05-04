import redis
import psycopg2
import time

# --- Redis connection ---
def get_redis():
    while True:
        try:
            r = redis.Redis(host='redis', port=6379)
            r.ping()
            print("Connected to Redis")
            return r
        except Exception as e:
            print("Waiting for Redis...", e)
            time.sleep(2)

# --- Postgres connection ---
def get_db():
    while True:
        try:
            conn = psycopg2.connect(
                host="postgres",
                database="votes",
                user="postgres",
                password="postgres"
            )
            print("Connected to PostgreSQL")
            return conn
        except Exception as e:
            print("Waiting for PostgreSQL...", e)
            time.sleep(2)

r = get_redis()
conn = get_db()
cur = conn.cursor()

print("Worker started...")

# --- MAIN LOOP ---
while True:
    try:
        vote = r.lpop("votes")

        if vote:
            vote = vote.decode()
            print(f"Processing vote: {vote}")

            cur.execute(
                "INSERT INTO votes (choice) VALUES (%s)",
                (vote,)
            )
            conn.commit()

    except Exception as e:
        print("Worker error:", e)

    time.sleep(1)
