from flask import Blueprint, request
import backend.repositories.themes as repo

themes_blueprint = Blueprint('themes', __name__)


@themes_blueprint.route('/', methods=['GET'])
def get_themes():
    return repo.get_themes()
