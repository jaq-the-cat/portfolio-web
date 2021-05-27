import os

from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)
load_dotenv('.env')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.route('/about')
def about():
    return 'About'

@app.route('/')
@app.route('/reviews')
def reviews():
    return 'Reviews'

@app.route('/projects')
def projects():
    return 'Projects'

@app.route('/review', methods=('GET', 'POST'))
def addreview():
    return 'Add review'

from .api import bp as api
app.register_blueprint(api)

# DEBUG
@app.after_request
def after_request(r):
    if  os.getenv('FLASK_DEBUG'):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
    return r
