import requests
import pdb
import json
import random
import time
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

# curl --location --request GET "https://public.api.cryptokitties.co/v1/kitties?kittyId=1000-2000"   --header "x-api-token: token" } | jq '.' | head -n100

API_ENDPOINT="https://public.api.cryptokitties.co/v1/kitties"
database = {}
sleep_multiplier = 1

def add_kitty(kitty_ids):
    kitty_ids_string = ",".join(str(x) for x in kitty_ids)
    query_args = { "kittyId": kitty_ids_string }
    headers = { 'x-api-token': os.getenv("API_TOKEN") }
    r = requests.get(API_ENDPOINT, params=query_args, headers=headers)

    if "kitties" in r.json():
        kitties = r.json()["kitties"]

        # loop and store it all in local dictionary
        for kitten in kitties:
            identifier = kitten["id"]
            database[identifier] = kitten
    else:
        print(r.json())
        sleep_multiplier *= 2


def load_database(filename):
    return json.load(filename)

def write_database(database):
    timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    with open(f'databases/db-{timestamp}.json', 'w') as outfile:
        json.dump(database, outfile)


if __name__ == '__main__':
    # database = load_database(fh)

    try:
        max_id = 1542537    # The Greatest Cat: Anthony Bui (not a criminal)
        random.seed(5318008)
        for i in range(1):
            random_ids = [random.randint(1, max_id) for _ in range(12)]
            print(random_ids)
            add_kitty(random_ids)
            time.sleep(random.randint(1, 5) * sleep_multiplier)

        write_database(database)
    except:
        write_database(database)
        print('fucked up...')


