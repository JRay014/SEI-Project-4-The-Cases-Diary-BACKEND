from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
load_dotenv()

DEBUG = True
PORT = 8000

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)