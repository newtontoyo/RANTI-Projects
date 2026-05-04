from flask import Flask, request
import redis
import time

app = Flask(__name__)

def get_redis():
    while True:
        try:
            r = redis.Redis(
                host='redis',
                port=6379,
                decode_responses=True,
                socket_connect_timeout=2
            )
            r.ping()
            print("Connected to Redis")
            return r
        except Exception as e:
            print("Waiting for Redis...", e)
            time.sleep(2)

# Initialize Redis connection
r = get_redis()

@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.get_json()
        choice = data.get("vote")

        if not choice:
            return "Invalid vote", 400

        print(f"Incoming vote: {choice}")

        r.rpush("votes", choice)

        # Debug: confirm write
        current = r.lrange("votes", 0, -1)
        print(f"Redis contents now: {current}")

        return "OK"
    except Exception as e:
        print("ERROR writing to Redis:", e)
        return "Error", 500


# 🔥 CRITICAL ENTRYPOINT (FIXED)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
