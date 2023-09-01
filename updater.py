import json

import httpx
import csv
import os

DATA_URL = 'https://davidmegginson.github.io/ourairports-data/airports.csv'


def _update_json() -> None:
    data_request = httpx.get(DATA_URL)

    if data_request.status_code == 200:
        reader = csv.DictReader(data_request.text.splitlines())
        if not os.path.exists('./dist'):
            os.mkdir('./dist')
        with open('dist/airports.json', 'w+') as jf:
            json.dump(list(reader), jf, indent=4)


if __name__ == '__main__':
    _update_json()
