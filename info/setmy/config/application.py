from info.setmy.arguments.config import Config
from info.setmy.arguments.parser import parse_arguments
from info.setmy.environment.variables import get_environment_variables_list
from info.setmy.strings.operations import combined_list


class Application:
    application_file_prefix = "application"
    application_file_suffixes = ["json", "yml", "yaml"]

    def __init__(self, argv: [str], argv_config: Config):
        self.argv = argv
        self.argv_config = argv_config
        self.arguments = parse_arguments(self.argv, self.argv_config)
        # get profiles in order and overload by that order: code, env, cli
        self.profiles_list = find_last_not_none(
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


def find_last_not_none(*args):
    last_not_none = []
    for arg in args:
        if arg is not None and isinstance(arg, list) and arg:
            last_not_none = arg
    return last_not_none
