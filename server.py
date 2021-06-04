from flask import Flask, jsonify, after_this_request
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

# we don't want to hog up the SQL connection pool
# so we should connect to the DB before every request
# and close the db connection after every request

@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client
                      # (in our case this will be some JSON)

@app.route('/')
def index():
    return "app.send_static_file('index.html')"

if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()

if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)