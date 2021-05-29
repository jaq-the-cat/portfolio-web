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
    if request.args.get('spa'):
        return jsonify({
            'title': 'About',
            'html': render_template('about.html', reviews=api.get_posts(), spa=True),
        })
    return render_template('about.html', **contact, reviews=api.get_posts(), spa=False, title='About')

@app.route('/reviews')
def reviews():
    if request.args.get('spa'):
        return jsonify({
            'title': 'Reviews',
            'html': render_template('reviews.html', reviews=api.get_posts(), spa=True),
        })
    return render_template('reviews.html', **contact, reviews=api.get_posts(), spa=False, title='Reviews')

@app.get('/projects')
def projects():
    if request.args.get('spa'):
        return jsonify({
            'title': 'Projects',
            'html': render_template('projects.html', projects=api.get_projects(), spa=True),
        })
    return render_template('projects.html', **contact, projects=api.get_projects(), spa=False, title='Projects')

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
