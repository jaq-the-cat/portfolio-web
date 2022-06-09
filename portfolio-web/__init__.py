import os

from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request
from . import api

app = Flask(__name__)
load_dotenv('.env')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

contact = {"email": os.getenv('EMAIL'), "phone": os.getenv('PHONE')}

@app.route('/')
@app.route('/about')
def about():
    return render_template('about.html', **contact, reviews=api.get_posts(), title='About')

@app.route('/reviews')
def reviews():
    return render_template('reviews.html', **contact, reviews=api.get_posts(), title='Reviews')

@app.get('/projects')
def projects():
    return render_template('projects.html', **contact, projects=api.get_projects(), title='Projects')

app.register_blueprint(api.bp)

# DEBUG
@app.after_request
def after_request(r):
    if  os.getenv('FLASK_DEBUG'):
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
    return r
