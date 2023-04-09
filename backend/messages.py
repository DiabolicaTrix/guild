from flask import Blueprint, request
import jwt
from backend.exceptions.insertexception import InsertException

from backend.exceptions.missingpermissions import MissingPermission
import backend.controllers.messages as controller

messages_blueprint = Blueprint('messages', __name__)


@messages_blueprint.route('/', methods=['GET'])
def get_conversations():
    conversations = controller.get_user_conversations(request.environ['token'])

    return conversations


@messages_blueprint.route('/<int:id>', methods=['GET'])
def get_messages_with_user(id):
    conversations = controller.get_messages_with_user(
        request.environ['token'], id)

    return conversations


@messages_blueprint.route('/<int:id>', methods=['POST'])
def send_message_to_user(id):
    body = request.json

    if not body['content']:
        return "Invalid request", 400

    try:
        message = controller.send_message_to_user(
            request.environ['token'], id, body['content'])

        return message, 201
    except InsertException:
        return "Error sending message", 500
