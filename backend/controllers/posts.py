import jwt
from backend.exceptions.missingpermissions import MissingPermission
import backend.repositories.posts as repo
import backend.repositories.projects as project_repo


def create_post(token, project_id, content):
    decoded = jwt.decode(token, options={"verify_signature": False})
    user_id = decoded['id']
    if not project_repo.is_user_member(user_id, project_id):
        raise MissingPermission

    return repo.create_post(content, user_id, project_id)
