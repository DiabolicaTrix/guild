import jwt
from backend.exceptions.missingpermissions import MissingPermission
import backend.repositories.projects as repo


def create_project(token, name, description, members):
    decoded = jwt.decode(token, options={"verify_signature": False})
    user_id = decoded['id']

    # Validate the the user creating the project is in the members list id
    if not any(member['id'] == user_id for member in members):
        raise MissingPermission

    id = repo.create_project(name, description)

    if not id:
        return None

    if not repo.assign_members_to_projects(id, members):
        return None

    return id
