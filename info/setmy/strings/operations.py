import json
import re
from itertools import product

from info.setmy import yaml


def split_and_trim(text: str, split_text: str = ","):
    trimmed_list = trim_list(text.split(split_text))
    return trimmed_list


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


def yaml_to_object(text: str, default_value={}):
    if text is None:
        return default_value
    try:
        return yaml.safe_load(text)
    except (yaml.YAMLError):
        return None


# TODO : test it
def find_named_placeholders(text: str, to_clean: bool = True):
    pattern = r"\${(.*?)}"
    placeholders = re.findall(pattern, text)
    if to_clean is True:
        cleaned_placeholders = [placeholder.replace("${", "").replace("}", "") for placeholder in placeholders]
        return cleaned_placeholders
    return placeholders


# TODO : test it
def replace_named_placeholder(text: str, place_holder_name: str, replacement: str):
    if replacement is None:
        replacement_string = ""
    else:
        replacement_string = replacement
    placeholder = "${" + place_holder_name + "}"
    return text.replace(placeholder, replacement_string)


# TODO : test it
# list1 = ["A", "B", "C"]
# list2 = ["X", "Y"]
# result should be: ['AX', 'AY', 'BX', 'BY', 'CX', 'CY']
def combined_list(list1: [str], list2: [str], join_text: str = ''):
    """
    Creates a new list by multiplying elements from two input lists, and joining them with the specified join_text separator.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.
        join_text (str, optional): The separator used to join elements from the input lists. Defaults to an empty string.

    Returns:
        list: A new list where elements from the two input lists are multiplied and joined with the join_text separator.
    """
    return [join_text.join(items) for items in product(list1, list2)]
