from flask import Blueprint
from backend.database import connect
from backend.repositories.posts import get_user_posts
import backend.repositories.users as repo

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/<int:id>', methods=['GET'])
def get_user(id):
    return repo.get_user(id)


@users_blueprint.route('/<int:id>/posts', methods=['GET'])
def get_posts(id):
    return repo.get_posts(id)


@users_blueprint.route('/<int:id>/projects', methods=['GET'])
def get_user_projects(id):
    return repo.get_user_projects(id)
