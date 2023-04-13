import backend.database as db


def get_role(id):
    query = 'SELECT id, project_id, user_id, name FROM projects_roles WHERE id = %s LIMIT 1'
    cursor = db.get(query, [id])

    if cursor.rowcount == 0:
        return None

    (id, project_id, user_id, name) = cursor.fetchone()

    result = {
        'id': id,
        'project_id': project_id,
        'user_id': user_id,
        'name': name,
    }

    return result
