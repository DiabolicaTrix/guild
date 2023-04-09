import time
import os
import bcrypt
import jwt
from flask import Blueprint
from flask import request
from backend.database import connect

auth_blueprint = Blueprint('authentication', __name__)


@auth_blueprint.post('/login')
def login():
    body = request.json
    # Validate the email and password are not empty
    if not body or not body['email'] or not body['password']:
        return "Invalid request", 400

    conn = connect()
    cursor = conn.cursor(buffered=True)

    # TODO add email index to users table
    # TODO add email unique constraint to users table
    query = "SELECT id, name, email, picture, password FROM users WHERE email = %s"
    cursor.execute(query, [body['email']])

    # Check if the user exists
    if cursor.rowcount == 0:
        return "User not found", 404

    # Check if the password matches
    (id, name, email, picture, hashed_password) = cursor.fetchone()
    if not bcrypt.checkpw(body['password'].encode('utf-8'), hashed_password.encode('utf-8')):
        # Return 404 to avoid leaking information about the existence of the user
        return "User not found", 404

    # Generate a JWT token
    token = jwt.encode({
        'id': id,
        'name': name,
        'email': email,
        'picture': picture,
    }, os.getenv("JWT_PRIVATE_KEY"), algorithm='HS256')

    return {
        'token': token
    }, 200


@ auth_blueprint.post('/register')
def register():
    body = request.json
    # Validate the name, email and password are not empty
    if not body or not body['name'] or not body['email'] or not body['password']:
        return "Invalid request", 400

    # Validate the password and password confirmation match
    if body['password'] != body['password_confirmation']:
        return "Passwords don't match", 400

    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(
        body['password'].encode('utf-8'), bytes(salt))

    conn = connect()
    cursor = conn.cursor()

    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (body['name'],
                   body['email'], hashed_password))
    cursor.close()
    conn.commit()

    print(cursor.rowcount)
    if cursor.rowcount == 0:
        return "Error registering user", 500

    return "Registered", 201
