from flask import Flask, jsonify
from flask_cors import CORS
from flask_login import LoginManager
import os
from dotenv import load_dotenv
from resources.entries import entries
from resources.users import users
import models

load_dotenv()

DEBUG = True
PORT = 8000

app = Flask(__name__, static_folder='../build', static_url_path='/')

CORS(app)
CORS(entries, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(entries, url_prefix='/api/entries')
app.register_blueprint(users, url_prefix='/api/users')

@app.route('/')
def index():
    return "app.send_static_file('index.html')"

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)