import json
import requests


BASE_URL = "http://127.0.0.1:8000/"
END_POINT = "api/updates/"


def get_update_list():
    r = requests.get(BASE_URL + END_POINT)
    data = r.json()
    for dict in data:
        print(dict.get("id"))
    return data


def get_update(update_id):
    r = requests.get(BASE_URL + END_POINT + str(update_id))
    data = r.json()
    return data


def create_update():
    data = {
        "user": 1,
        "content": "New update"
    }
    r = requests.post(BASE_URL + END_POINT, data=data)
    print(r.status_code)
    print(r.headers)
    print(r.json())
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


print(create_update())
