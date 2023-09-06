import os
import re
from collections import OrderedDict
from functools import reduce

from info.setmy.arguments.config import Config
from info.setmy.arguments.parser import parse_arguments
from info.setmy.environment.variables import get_environment_variables_list, get_environment_variable
from info.setmy.json.parser import parse_json_file
from info.setmy.string.operations import combined_list, combined_by_function_list, find_named_placeholders, \
    replace_named_placeholder
from info.setmy.yaml.parser import parse_yaml_file


class Application:
    application_file_prefix = "application"
    application_file_suffixes = ["json", "yml", "yaml"]  # In overloading order

    def __init__(self, argv: [str], argv_config: Config):
        self.argv = argv
        self.argv_config = argv_config
        self.arguments = parse_arguments(self.argv, self.argv_config)
        # get resource/config folders in order and loading (overload in case of existing file) by that
        # order: code, env, cli
        self.config_paths = list(
            OrderedDict.fromkeys(
                ["./test/resources", "./resources"] +
                get_environment_variables_list("SMI_CONFIG_PATHS") +
                self.get_cli_config_paths()
            )
        )
        # get profiles in order and overload by that order: (code, ) env, cli
        self.profiles_list = find_last_not_none_and_empty(
            get_environment_variables_list("SMI_PROFILES"),
            self.arguments.smi_profiles
        )
        self.default_application_files = combined_list(
            [Application.application_file_prefix],
            Application.application_file_suffixes,
            "."
        )
        application_profiles_file_prefixes = combined_list(
            [Application.application_file_prefix],
            self.profiles_list,
            "-"
        )
        application_profiles_files = combined_list(
            application_profiles_file_prefixes,
            Application.application_file_suffixes,
            "."
        )
        self.application_files = application_profiles_files + self.default_application_files
        self.applications_files_paths = list(
            map(
                lambda item: [item, self.parse_file_by_type(item)],
                combined_by_function_list(
                    self.config_paths,
                    self.application_files,
                    "/",
                    lambda file_path: os.path.isfile(file_path)
                )
            )
        )
        self.merged_config = reduce(
            lambda x, y: merge_dicts(x, y),
            list(
                map(
                    lambda sub_list: sub_list[1],
                    self.applications_files_paths
                )
            ),
            {}  # initial value
        )

    def get_cli_config_paths(self):
        if hasattr(self.arguments, "smi_config_paths") and self.arguments.smi_config_paths is not None:
            return self.arguments.smi_config_paths
        return []

    @staticmethod
    def parse_file_by_type(file_name: str):
        new_file_name = file_name.lower()
        if re.search(r'\.(yaml|yml)$', new_file_name):
            return parse_yaml_file(file_name, {'post_read_function': post_read_function})
        elif re.search(r'\.json$', new_file_name):
            return parse_json_file(file_name, {'post_read_function': post_read_function})
        else:
            return None


def post_read_function(text: str):
    placeholders = find_named_placeholders(text)
    placeholder_value_pairs = list(
        map(
            lambda place_holder: [place_holder, get_environment_variable(place_holder)],
            placeholders
        )
    )
    for placeholder_value_pair in placeholder_value_pairs:
        placeholder = placeholder_value_pair[0]
        value = placeholder_value_pair[1]
        if value is not None:
            text = replace_named_placeholder(text, placeholder, value)
    return text


def find_last_not_none_and_empty(*args):
    last_not_none = []
    for arg in args:
        if arg is not None and isinstance(arg, list) and arg:
            last_not_none = arg
    return last_not_none


def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries hierarchically.

    Args:
        dict1 (dict): First dictionary.
        dict2 (dict): Second dictionary.

    Returns:
        dict: Merged dictionary.
    """
    result = dict1.copy()
    for key, value in dict2.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = merge_dicts(result[key], value)
        else:
            result[key] = value
    return result
