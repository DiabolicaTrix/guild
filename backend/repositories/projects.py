import backend.database as db


def get_projects():
    query = 'SELECT id, name, description, status, progress, created_at FROM projects'
    cursor = db.get(query)

    results = []
    for (id, name, description, status, progress, created_at) in cursor:
        result = {
            'id': id,
            'name': name,
            'description': description,
            'status': status,
            'progress': progress,
            'created_at': created_at
        }

        query = '''SELECT path FROM projects_pictures WHERE project_id = %s'''
        cursor = db.get(query, [id])

        pictures = []
        for (path) in cursor:
            pictures.append(path)

        print(pictures)

        if len(pictures) > 0:
            result['pictures'] = pictures

        results.append(result)

    return results


def search_projects(search, themes, filters):
    query = 'SELECT id, name, description, status, progress, created_at FROM projects WHERE name LIKE %s'
    params = ['%' + search + '%']

    if themes is not None and len(themes) > 0:
        placeholders = ', '.join(['%s'] * len(themes))
        query = query + ' AND theme_id IN (%s)' % placeholders
        params.extend(themes)

    cursor = db.get(query, params)

    results = []
    for (id, name, description, status, progress, created_at) in cursor:
        result = {
            'id': id,
            'name': name,
            'description': description,
            'status': status,
            'progress': progress,
            'created_at': created_at
        }

        query = '''SELECT path FROM projects_pictures WHERE project_id = %s'''
        cursor = db.get(query, [id])

        pictures = []
        for (path) in cursor:
            pictures.append(path)

        print(pictures)

        if len(pictures) > 0:
            result['pictures'] = pictures

        results.append(result)

    return results


def get_project(id):
    query = 'SELECT id, name, description, status, progress, created_at FROM projects WHERE id = %s'
    cursor = db.get(query, [id])

    (id, name, description, status, progress, created_at) = cursor.fetchone()

    result = {
        'id': id,
        'name': name,
        'description': description,
        'status': status,
        'progress': progress,
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


def create_project(name, description):
    query = '''INSERT INTO projects (name, description) VALUES (%s, %s)'''
    cursor = db.post(query, [name, description])

    if cursor.rowcount == 0:
        return None

    return cursor.lastrowid


def assign_members_to_projects(project_id, members):
    for member in members:
        query = '''INSERT INTO projects_roles (project_id, user_id, name) VALUES (%s, %s, %s)'''
        cursor = db.post(query, [project_id, member['id'], member['role']])

        if cursor.rowcount == 0:
            return False

    return True


def is_user_member(user_id, project_id):
    query = 'SELECT * FROM projects_roles WHERE user_id = %s AND project_id = %s'
    cursor = db.get(query, [user_id, project_id])

    return cursor.rowcount > 0
