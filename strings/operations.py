import json


def trim_list(strings_list):
    fragments = [fragment.strip() for fragment in strings_list]
    return fragments


def to_boolean(text: str, default_value=False):
    if text is None:
        return default_value
    lower_text = text.lower()
    if lower_text == 'true' or lower_text == 'yes':
        return True
    elif lower_text == 'false' or lower_text == 'no':
        return False
    else:
        raise ValueError("Invalid boolean value")


def to_int(text: str, default_value=0):
    if text is None:
        return default_value
    try:
        return int(text)
    except (ValueError, TypeError):
        return None


def to_float(text: str, default_value=0.0):
    if text is None:
        return default_value
    try:
        return float(text)
    except (ValueError, TypeError):
        return default_value


def json_to_object(text: str, default_value={}):
    if text is None:
        return default_value
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None
