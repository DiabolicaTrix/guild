from flask import Blueprint, request
import backend.repositories.applications as repo

applications_blueprint = Blueprint('applications', __name__)


@applications_blueprint.route('/<int:id>', methods=['GET'])
def get_application(id):
    result = repo.get_application(id)

    if result is None:
        return "Application not found", 404

    return result
