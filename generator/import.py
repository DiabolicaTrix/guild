import csv
import datetime
import random
import lorem
import mysql.connector
import time


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='root',
    database='guild'
)


# Projects
project_status = ['DONE', 'IN_PROGRESS', 'STARTING']
projects_count = 106
with open("projects.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        status = random.choice(project_status)
        query = '''INSERT INTO projects (name, theme, description, status, progress) VALUES (%s, %s, %s, %s, %s)'''
        cursor = conn.cursor(buffered=True)
        cursor.execute(query, [row[0], row[1], row[2], status,
                       100 if status == 'DONE' else random.randint(0, 100)])
        cursor.close()
        conn.commit()

# Users

# 123 password hashed
password = "$2b$12$pgfA4t4v8Lk7Ok9UvAlVCuhz2M1oDabz9ImA6sVlhGarpzQZxDC9a"
users_count = 100
with open("users.csv", "r") as f:
    reader = csv.reader(f)
    index = 0
    for row in reader:
        query = '''INSERT INTO users (name, email, role, password, picture) VALUES (%s, %s, %s, %s, %s)'''
        cursor = conn.cursor(buffered=True)
        cursor.execute(query, [row[0], row[1], row[2],
                       password, '/avatar' + str(index) + '.jpg'])
        cursor.close()
        conn.commit()
        index += 1


# Projects Roles
# It is possible for a user to have multiple roles in a project
roles = ['Team Lead', 'Developper', 'Quality Assurance', 'Designer', 'Product Owner',
         'Scrum Master', '3D Artist', '2D Artist', 'Sound Designer', 'Animator']

# Keeps mapping between user_id and project_ids to create posts later
user_projects = {}

for i in range(1, projects_count + 1):
    # 1 to 5 roles per project
    users = []
    for j in range(0, random.randint(1, 5)):
        query = '''INSERT INTO projects_roles (project_id, user_id, name) VALUES (%s, %s, %s)'''
        cursor = conn.cursor(buffered=True)

        user_id = random.randint(1, users_count)
        cursor.execute(query, [i, user_id, random.choice(roles)])
        cursor.close()
        conn.commit()

        users.append(user_id)
    user_projects[i] = users

    # Add some empty roles
    for j in range(0, random.randint(0, 2)):
        query = '''INSERT INTO projects_roles (project_id, user_id, name) VALUES (%s, %s, %s)'''
        cursor = conn.cursor(buffered=True)

        cursor.execute(query, [i, None, random.choice(roles)])
        cursor.close()
        conn.commit()

# Posts
posts_count = 100
time.strftime('%Y-%m-%d %H:%M:%S')
for i in range(1, projects_count + 1):
    # 0 to 30 posts per project
    for j in range(0, random.randint(0, 30)):
        query = '''INSERT INTO posts (author_id, project_id, content, created_at) VALUES (%s, %s, %s, %s)'''
        cursor = conn.cursor(buffered=True)

        created_at = datetime.datetime(random.randint(2020, 2022), random.randint(1, 12), random.randint(
            1, 28), random.randint(0, 23), random.randint(0, 59), random.randint(0, 59))

        content = lorem.paragraph()
        cursor.execute(query, [random.choice(
            user_projects[i]), i, content, created_at.strftime('%Y-%m-%d %H:%M:%S')])
        cursor.close()
        conn.commit()
