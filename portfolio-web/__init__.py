import os

from dotenv import load_dotenv
from flask import Flask, render_template, redirect
from . import api

app = Flask(__name__)
load_dotenv('.env')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

contact = {"email": os.getenv('EMAIL'), "phone": os.getenv('PHONE')}

@app.get('/')
@app.get('/about')
def about():
    return render_template('about.html', **contact)

@app.route('/reviews')
def reviews():
    return render_template('reviews.html', **contact, reviews=api.get_posts())

@app.get('/projects')
def projects():
    return render_template('projects.html', **contact, projects=api.get_projects())

@app.post('/review')
def addreview():
    return redirect('/reviews')

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
