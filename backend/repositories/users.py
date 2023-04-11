import backend.database as db
from backend.repositories.posts import get_user_posts


def get_user(id):
    query = 'SELECT id, name, email, role, picture, created_at FROM users WHERE id = %s LIMIT 1'
    cursor = db.get(query, [id])

    (id, name, email, role, picture, created_at) = cursor.fetchone()

    return {
        'id': id,
        'name': name,
        'email': email,
        'role': role,
        'picture': picture,
        'created_at': created_at
    }


def get_user_by_email(email):
    query = 'SELECT id, name, email, role, picture, created_at FROM users WHERE email = %s LIMIT 1'
    cursor = db.get(query, [email])

    if cursor.rowcount == 0:
        return None

    (id, name, email, role, picture, created_at) = cursor.fetchone()

    return {
        'id': id,
        'name': name,
        'email': email,
        'role': role,
        'picture': picture,
        'created_at': created_at
    }


def get_posts(id):
    results = get_user_posts(id)

    if len(results) == 0:
        return "No posts found for user", 404

    return results


def get_user_projects(id):
    query = '''SELECT id, projects.name, description, status, created_at
                FROM projects
                INNER JOIN projects_roles PR ON PR.project_id = id 
                WHERE user_id = %s'''
    cursor = db.get(query, [id])

    results = []
    for (id, name, description, status, created_at) in cursor:
        result = {
            'id': id,
            'name': name,
            'description': description,
            'status': status,
            'created_at': created_at,
        }
        query = '''SELECT path FROM projects_pictures WHERE project_id = %s'''
        cursor = db.get(query, [id])

        pictures = []
        for (path) in cursor:
            pictures.append(path)

        result['pictures'] = pictures
        results.append(result)

    cursor.close()

    return results
