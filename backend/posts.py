from flask import Blueprint, request
import jwt

from backend.database import connect
from backend.exceptions.missingpermissions import MissingPermission
import backend.repositories.posts as repo
import backend.controllers.posts as controller

posts_blueprint = Blueprint('posts', __name__)


@posts_blueprint.route('/', methods=['GET'])
def get_posts():
    posts = repo.get_posts()

    return posts


@posts_blueprint.route('/', methods=['POST'])
def create_post():
    body = request.json

    # Validate content and project_id
    if not body or not body['content'] or not body['project_id']:
        return "Invalid request", 400

    try:
        success = controller.create_post(
            request.environ['token'], body['project_id'], body['content'])

        if not success:
            return "Error creating post", 500
        return "Post created", 201

    except MissingPermission:
        return "Forbidden", 403
