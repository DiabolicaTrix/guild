import backend.database as db


def get_themes():
    query = 'SELECT id, name, color FROM themes'
    cursor = db.get(query)

    if cursor.rowcount == 0:
        return None

    results = []
    for (id, name, color) in cursor:
        results.append({
            'id': id,
            'name': name,
            'color': color,
        })

    return results
