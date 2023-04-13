import backend.database as db


def get_application(id):
    query = '''SELECT applications.user_id, role_id, motivation, users.name as user_name, users.picture as user_picture, projects.id as project_id, projects.name as project_name, pr.name as role_name
                FROM applications
                INNER JOIN users ON users.id = user_id
                INNER JOIN projects_roles pr ON pr.id = role_id 
                INNER JOIN projects ON projects.id = pr.project_id 
                WHERE applications.id = %s LIMIT 1'''
    cursor = db.get(query, [id])

    if cursor.rowcount == 0:
        return None

    (user_id, role_id, motivation, user_name, user_picture,
     project_id, project_name, role_name) = cursor.fetchone()

    return {
        'user': {
            'id': user_id,
            'name': user_name,
            'picture': user_picture
        },
        'project': {
            'id': project_id,
            'name': project_name
        },
        'role': {
            'id': role_id,
            'name': role_name
        },
        'motivation': motivation
    }


def send_application(user_id, role_id, motivation):
    query = '''INSERT INTO applications (user_id, role_id, motivation) VALUES (%s, %s, %s)'''
    cursor = db.post(query, [user_id, role_id, motivation])

    if cursor.rowcount == 0:
        return None

    return cursor.lastrowid
