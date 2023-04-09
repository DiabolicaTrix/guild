import backend.database as db


def get_projects():
    query = 'SELECT id, name, description, status, created_at FROM projects'
    cursor = db.get(query)

    results = []
    for (id, name, description, status, created_at) in cursor:
        results.append({
            'id': id,
            'name': name,
            'description': description,
            'status': status,
            'created_at': created_at
        })

    return results


def get_project(id):
    query = 'SELECT id, name, description, status, created_at FROM projects WHERE id = %s'
    cursor = db.get(query, [id])

    (id, name, description, status, created_at) = cursor.fetchone()

    result = {
        'id': id,
        'name': name,
        'description': description,
        'status': status,
        'created_at': created_at
    }

    query = '''SELECT path FROM projects_pictures WHERE project_id = %s'''
    cursor = db.get(query, [id])

    if cursor.rowcount == 0:
        return result

    pictures = []
    for (path) in cursor:
        pictures.append(path)

    result['pictures'] = pictures

    return result


def is_user_member(user_id, project_id):
    query = 'SELECT * FROM projects_roles WHERE user_id = %s AND project_id = %s'
    cursor = db.get(query, [user_id, project_id])

    return cursor.rowcount > 0
