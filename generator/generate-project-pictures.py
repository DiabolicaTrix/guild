import csv
import os
import time
from dotenv import load_dotenv
import requests
import random
import mysql.connector
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='root',
    database='guild'
)

# Projects
projects_count = 106
with open("projects.csv", "r") as f:
    reader = csv.reader(f)
    index = 1
    for row in reader:
        response = openai.Image.create(
            prompt="A picture of a game called " + row[0],
            n=1,
            size="512x512"
        )
        print("Downloading image for " + row[0])
        with open("../frontend/public/project" + str(index) + ".png", 'wb') as handle:
            picture = requests.get(response.data[0].url, stream=True)

            if not picture:
                print(response)

            for block in picture.iter_content(1024):
                if not block:
                    break

                handle.write(block)

        query = '''INSERT INTO projects_pictures (project_id, path) VALUES (%s, %s)'''
        cursor = conn.cursor(buffered=True)
        cursor.execute(query, [index, '/project' + str(index) + '.png'])
        cursor.close()
        conn.commit()
        print("Inserted into DB")

        index = index + 1
        print("Sleeping for 12 seconds...")
        time.sleep(12)
