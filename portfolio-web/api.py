import os
from flask import Blueprint, jsonify
from github import Github
import firebase_admin
from firebase_admin import firestore
from google.cloud import firestore as gfs
from typing import List

_g = Github()
fb = firebase_admin.initialize_app()
fs: gfs.Client = firestore.client()

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.get('/projects')
def api_projects():
    user: str = str(os.getenv('GITHUB_USER'))
    repos = _g.get_user(user).get_repos()
    return jsonify(map(lambda repo: {
        'url': f'https://github.com/{repo.full_name}',
        'description': repo.description,
    }, repos))

@bp.get('/reviews')
def api_reviews():
    posts: List[gfs.DocumentSnapshot] = fs.collection('posts').get()
    return jsonify(list(
        map(lambda post: post.to_dict() | {'id': post.id},
        posts
    )))
