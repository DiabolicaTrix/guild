from flask import Blueprint, request
from backend.database import connect
from backend.repositories.posts import get_user_posts
import backend.repositories.users as repo

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/<int:id>', methods=['GET'])
def get_user(id):
    return repo.get_user(id)


@users_blueprint.route('/', methods=['GET'])
def get_users():
    args = request.args

    if args['email']:
        user = repo.get_user_by_email(args['email'])
        if not user:
            return "User not found", 404
        return user

    return repo.get_users(id)


@users_blueprint.route('/<int:id>/picture', methods=['POST'])
def upload_user_picture(id):

    if 'file' not in request.files:
        return "No file part", 400

    return "OK I Guess", 201


@users_blueprint.route('/<int:id>/posts', methods=['GET'])
def get_posts(id):
    return repo.get_posts(id)


@users_blueprint.route('/<int:id>/projects', methods=['GET'])
def get_user_projects(id):
    return repo.get_user_projects(id)


@users_blueprint.route('/<int:id>/notifications', methods=['GET'])
def get_notifications(id):
    return repo.get_notifications(id)
