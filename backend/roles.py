from flask import Blueprint, request
import backend.repositories.roles as repo
import backend.controllers.applications as applications_controller

roles_blueprint = Blueprint('roles', __name__)


@roles_blueprint.route('/<int:id>', methods=['GET'])
def get_role(id):
    return repo.get_role(id)


@roles_blueprint.route('/<int:id>/apply', methods=['POST'])
def send_application(id):
    # Validate motivation
    if not request.json or not request.json['motivation']:
        return "Invalid request", 400

    id = applications_controller.send_application(
        request.environ['token'], id, request.json['motivation'])

    if id is None:
        return "Error sending application", 500

    return {'id': id}, 201
