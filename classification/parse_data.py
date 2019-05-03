import os
import csv
import requests
import random

remove = "https://img.cryptokitties.co/0x06012c8cf97bead5deae237070f9587f8e7a266d/"

directories = ["data/", "data/train/", "data/train/criminal/", "data/train/noncriminal", "data/validation/criminal", "data/validation//noncriminal"]
for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

with open('mturk-results-combined.csv', newline='') as f:
    rows = csv.reader(f, delimiter=',')
    next(rows)

    for row in rows:
        kitty_id = row[0][len(remove):len(row[0])]
        print(kitty_id)
        img = requests.get(row[0]).content
        path = "criminal/" if row[1] == "Yes" else "noncriminal/"
        base_path = "data/train/" if random.random() > .2 else "data/validation/"

        savePath = base_path + path + kitty_id
        with open(savePath, 'wb') as handler:
            handler.write(img)
