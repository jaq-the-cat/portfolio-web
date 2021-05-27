import os

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify

app = Flask(__name__)
load_dotenv('.env')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

@app.get('/')
@app.get('/about')
def about():
    return render_template('about.html', email=os.getenv('EMAIL'), phone=os.getenv('PHONE'))

@app.route('/reviews')
def reviews():
    return render_template('reviews.html')

@app.get('/projects')
def projects():
    return render_template('projects.html')

@app.post('/review')
def addreview():
    return jsonify(True)

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
