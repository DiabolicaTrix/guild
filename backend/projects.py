from flask import Blueprint, request
from backend.database import connect
from backend.exceptions.missingpermissions import MissingPermission
from backend.repositories.posts import get_project_posts
import backend.repositories.projects as repo
import backend.controllers.projects as controller

projects_blueprint = Blueprint('projects', __name__)


@projects_blueprint.route('/', methods=['GET'])
def get_projects():
    return repo.get_projects()


@projects_blueprint.route('/<int:id>', methods=['GET'])
def get_project(id):
    return repo.get_project(id)


@projects_blueprint.route('/', methods=['POST'])
def create_project():
    body = request.json

    # Validate name, description and members
    if not body or not body['name'] or not body['description'] or not body['members']:
        return "Invalid request", 400

    # Validate members is an array and contains at least one member
    if not isinstance(body['members'], list) or len(body['members']) == 0:
        return "Invalid request", 400

    try:
        id = controller.create_project(
            request.environ['token'], body['name'], body['description'], body['members'])

        if not id:
            return "Error creating post", 500
        return {'id': id}, 201

    except MissingPermission:
        return "Forbidden", 403


@projects_blueprint.route('/<int:id>/posts', methods=['GET'])
def get_posts(id):
    posts = get_project_posts(id)

    if len(posts) == 0:
        return "No posts found for project", 404

    return posts


@projects_blueprint.route('/<int:id>/roles', methods=['GET'])
def get_roles(id):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    query = '''SELECT PR.name, users.name as user_name, picture as user_picture, users.id as user_id FROM projects_roles as PR LEFT JOIN users ON users.id = PR.user_id WHERE project_id = %s'''
    cursor.execute(query, [id])
    cursor.close()

    if cursor.rowcount == 0:
        return "Not found", 404

    results = []
    for (name, user_name, user_picture, user_id) in cursor:
        result = {
            'name': name,
        }

        if user_name is not None:
            result['user'] = {
                'id': user_id,
                'name': user_name,
                'picture': user_picture
            }

        results.append(result)

    return results
