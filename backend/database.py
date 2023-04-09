import mysql.connector


def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password='root',
        database='guild'
    )


def get(query, params=[]):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    cursor.execute(query, params)

    cursor.close()
    return cursor


def post(query, params=[]):
    conn = connect()
    cursor = conn.cursor(buffered=True)

    cursor.execute(query, params)

    cursor.close()
    conn.commit()
    return cursor
