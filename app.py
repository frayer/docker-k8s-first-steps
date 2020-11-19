from arguments import args
from flask import Flask, Response, json
import logging
import os

app = Flask(__name__)

LISTEN_HOST = args.host
LISTEN_PORT = args.port

@app.route('/')
def root():
    data = json.dumps({
        "appName": "python-flask-demo",
        "version": "1.0.0",
        "env": {
            "host": os.getenv('HOSTNAME'),
            "user_defined_1": os.getenv('USER_DEFINED_1'),
            "user_defined_2": os.getenv('USER_DEFINED_2'),
            "user_defined_3": os.getenv('USER_DEFINED_3')
        }
    })
    return Response(data, mimetype="application/json")

if __name__ == '__main__':
    app.run(host=LISTEN_HOST, port=LISTEN_PORT)
