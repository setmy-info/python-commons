import json


def parse_json_file(file_name: str):
    with open(file_name, "r") as json_file:
        return json.load(json_file)
    return None
