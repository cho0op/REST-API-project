import json

import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/"


def do_call(method="get", _id=15):
    url = ENDPOINT
    headers = {'Content-Type': "application/json"}
    # headers to prevent some "detail": "Unsupported media type \"text/plain;charset=UTF-8\" in request."
    data = {"id": _id, "content": "hhhhhhuuuuu", 'user': 1}
    json_data = json.dumps(data)
    r = requests.delete(url, data=json_data, headers=headers)
    return r.json()


print(do_call())
