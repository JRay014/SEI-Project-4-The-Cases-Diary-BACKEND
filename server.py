from flask import Flask, jsonify
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True
PORT = 8000

app = Flask(__name__, static_folder='../build', static_url_path='/')

CORS(app)

@app.route('/')
def index():
    return "app.send_static_file('index.html')"

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)