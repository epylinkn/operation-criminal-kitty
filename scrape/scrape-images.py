import sys
import json
import time
import random
from urllib import request

def load_database(filename):
    print(filename)

    with open(f'databases/{filename}') as infile:
         return json.load(infile)

if __name__ == '__main__':
    database = load_database(sys.argv[1])
    progress = 0
    total = len(database)

    for key, kitty in database.items():
        progress = progress + 1
        print(f'{key}; Downloading {progress}/{total} kittens')

        f = open(f'images/{key}.png', 'wb')
        url = kitty["image_url_png"]
        f.write(request.urlopen(url).read())
        f.close()

        time.sleep(random.random() / 2)
