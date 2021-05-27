import os
from flask import Blueprint, jsonify
from github import Github
import firebase_admin

_g = Github()

bp = Blueprint('api', __name__, url_prefix='/api')
firebase_admin.initialize_app()

@bp.route('/projects')
def api_projects():
    user: str = str(os.getenv('GITHUB_USER'))
    repos = _g.get_user(user).get_repos()
    return jsonify(map(lambda repo: {
        'url': f'https://github.com/{repo.full_name}',
        'description': repo.description,
    }, repos))

@bp.route('/reviews')
def api_reviews():
    user: str = str(os.getenv('GITHUB_USER'))
    repos = _g.get_user(user).get_repos()
    return jsonify(list(map(
        lambda repo: {
            'url': f'https://github.com/{repo.full_name}',
            'description': repo.description,
        }, repos
    )))
