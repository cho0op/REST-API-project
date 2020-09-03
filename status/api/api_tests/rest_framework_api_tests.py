import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/"


def do_call(method="get", _id=7):
    url = ENDPOINT + "?id=" + str(_id)
    print(url)
    r = requests.get(url)
    return r.json()


print(do_call())
