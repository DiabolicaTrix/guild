import jwt
from backend.exceptions.missingpermissions import MissingPermission
import backend.repositories.applications as repo


def send_application(token, project_id, motivation):
    decoded = jwt.decode(token, options={"verify_signature": False})
    user_id = decoded['id']

    id = repo.send_application(user_id, project_id, motivation)

    return id
