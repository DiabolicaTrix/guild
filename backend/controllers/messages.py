import jwt
import backend.repositories.messages as repo


def get_user_conversations(token):
    # Extract user id from token
    decoded = jwt.decode(token, options={"verify_signature": False})
    user_id = decoded['id']

    return repo.get_user_conversations(user_id)


def get_messages_with_user(token, receiver_id):
    # Extract user id from token
    decoded = jwt.decode(token, options={"verify_signature": False})
    user_id = decoded['id']

    return repo.get_messages_with_user(user_id, receiver_id)


def send_message_to_user(token, receiver_id, content):
    # Extract user id from token
    decoded = jwt.decode(token, options={"verify_signature": False})
    user_id = decoded['id']

    return repo.send_message_to_user(user_id, receiver_id, content)
