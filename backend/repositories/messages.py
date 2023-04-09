import backend.database as db
from backend.exceptions.insertexception import InsertException


def get_user_conversations(id):
    # Query to return user ids of users the user has a conversation with (at least 1 message)
    query = '''SELECT DISTINCT receiver_id , name, picture
                    FROM messages
                    INNER JOIN users ON users.id = messages.receiver_id
                    WHERE sender_id = %s
                UNION 
                SELECT DISTINCT sender_id, name, picture
                                FROM messages
                                INNER JOIN users ON users.id = messages.sender_id
                                WHERE receiver_id = %s
            '''
    cursor = db.get(query, [id, id])

    results = []
    for (receiver_id, name, picture) in cursor:
        results.append({
            'id': receiver_id,
            'name': name,
            'picture': picture,
        })
    return results


def get_messages_with_user(user_id, receiver_id):
    # Query to return all messages between user and receiver
    query = '''SELECT *
                FROM messages
                WHERE (sender_id = %s AND receiver_id = %s) OR (sender_id = %s AND receiver_id = %s)
                ORDER BY sent_at
            '''
    cursor = db.get(query, [user_id, receiver_id, receiver_id, user_id])

    results = []
    for (id, sender_id, receiver_id, content, sent_at) in cursor:
        results.append({
            'id': id,
            'sender_id': sender_id,
            'receiver_id': receiver_id,
            'content': content,
            'sent_at': sent_at,
        })
    return results


def send_message_to_user(user_id, receiver_id, content):
    query = '''INSERT INTO messages (sender_id, receiver_id, content) VALUES (%s, %s, %s)'''
    cursor = db.post(query, [user_id, receiver_id, content])

    if cursor.rowcount == 0:
        raise InsertException

    return {
        'id': cursor.lastrowid,
        'sender_id': user_id,
        'receiver_id': receiver_id,
        'content': content,
    }
