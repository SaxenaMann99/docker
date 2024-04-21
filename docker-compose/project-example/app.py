import time
import logging
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# Configure logging
logging.basicConfig(filename='/app/logs/python.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                logging.error("Redis connection error: %s", exc)
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    logging.info("Visited %s times", count)
    return 'Hello idiot! I have been seen {} times.\n'.format(count)


# This is a simple Flask web application that counts how many times the '/' route has been accessed and stores this count in a Redis database.
# It uses Redis, an in-memory data structure store, for caching.
