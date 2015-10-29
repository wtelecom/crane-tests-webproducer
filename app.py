import os
from flask import Flask
import redis

app = Flask(__name__)
r = redis.StrictRedis(host='db', port=6379, db=0)


@app.route("/set/<smthng>")
def produce(number):
    r.set('data', str(smthng))
    return {'data':str(smthng), 'action':'set'}


if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5001))
        app.run(host='0.0.0.0', port=port)
