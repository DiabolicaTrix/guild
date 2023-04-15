import requests
import random

users_count = 100

types = ['male', 'female', 'pixel']
for i in range(0, users_count + 1):
    with open("../frontend/public/avatar" + str(i) + ".jpg", 'wb') as handle:

        url = "https://xsgames.co/randomusers/avatar.php?g=" + \
            random.choice(types)
        print("Downloading " + url)
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
