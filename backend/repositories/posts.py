import backend.database as db

# Get posts for project


def get_project_posts(id):
    query = '''SELECT posts.id, content, posts.created_at, name as author_name, picture as author_picture, users.id as author_id
               FROM posts
               INNER JOIN users ON posts.author_id = users.id
               WHERE project_id = %s
               ORDER BY posts.created_at DESC'''
    cursor = db.get(query, [id])

    results = []
    for (id, content, created_at, author_name, author_picture, author_id) in cursor:
        results.append({
            'id': id,
            'content': content,
            'created_at': created_at,
            'author': {
                'id': author_id,
                'name': author_name,
                'picture': author_picture
            }
        })
    return results


def get_user_posts(id):
    query = '''SELECT posts.id, content, posts.created_at, name as author_name, picture as author_picture, users.id as author_id
               FROM posts
               INNER JOIN users ON posts.author_id = users.id
               WHERE author_id = %s
               ORDER BY posts.created_at DESC'''
    cursor = db.get(query, [id])

    results = []
    for (id, content, created_at, author_name, author_picture, author_id) in cursor:
        results.append({
            'id': id,
            'content': content,
            'created_at': created_at,
            'author': {
                'id': author_id,
                'name': author_name,
                'picture': author_picture
            }
        })
    return results


def get_posts():
    query = '''SELECT posts.id, content, posts.created_at, name as author_name, picture as author_picture, users.id as author_id
               FROM posts
               INNER JOIN users ON posts.author_id = users.id
               ORDER BY posts.created_at DESC
               LIMIT 25'''
    cursor = db.get(query)

    results = []
    for (id, content, created_at, author_name, author_picture, author_id) in cursor:
        results.append({
            'id': id,
            'content': content,
            'created_at': created_at,
            'author': {
                'id': author_id,
                'name': author_name,
                'picture': author_picture
            }
        })
    return results


def create_post(content, author_id, project_id):
    query = '''INSERT INTO posts (content, author_id, project_id) VALUES (%s, %s, %s)'''
    cursor = db.post(query, [content, author_id, project_id])

    return cursor.rowcount != 0
