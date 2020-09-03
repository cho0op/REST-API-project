import json


def is_json(data):   # to check if it's json to prevent JSONDecodeError: Expecting value: line 1 column 1
    try:
        json_data = json.loads(data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid
