import os
from flask import Blueprint, jsonify
from github import Github

_g = Github(os.getenv('GITHUB_KEY'))

bp = Blueprint('api', __name__, url_prefix='/api')

def get_posts() -> list:
    return []

def get_projects() -> list[dict[str, str]]:
    user: str = str(os.getenv('GITHUB_USER'))
    repos = _g.get_user(user).get_repos()
    return list(map(lambda repo: {
        'name': repo.full_name,
        'description': repo.description,
    }, repos))

@bp.get('/projects')
def api_projects():
    return jsonify(get_projects())

@bp.get('/reviews')
def api_reviews():
    return jsonify(list(
        map(lambda post: post.to_dict() | {'id': post.id},
        get_posts()
    )))
