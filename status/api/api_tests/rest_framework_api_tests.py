import json
import os
import requests

ENDPOINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "bot-chto-takoe.jpg")


def detail_api_call(_id):
    r = requests.delete(ENDPOINT + str(_id) + "/")
    if r.status_code == requests.codes.ok:
        return r.json()
    return r.text


print(detail_api_call(27))

# def do_call(_id=13):
#     url = ENDPOINT
#     headers = {'Content-Type': "application/json"}
#     # headers to prevent some "detail": "Unsupported media type \"text/plain;charset=UTF-8\" in request."
#     data = {"id": _id, "content": "kek", "user": 1}
#     json_data = json.dumps(data)
#     r = requests.put(url, data=json_data, headers=headers)
#     return r.text
#
#
# def do_call_with_image(image_path=None):
#     headers = {'Content-Type': "application/json"}
#     if image_path is not None:
#         with open(image_path, 'rb') as image:  # rb: reads as bytes
#             data = {"id": 22, "user": 1, "content": "new content for imaged object"}
#             files_data = {"image": image}
#             r = requests.put(ENDPOINT, data=data, files=files_data, headers=headers)
#             print(r.text)
#             return r
#
#
# print(do_call_with_image(_id=29))
