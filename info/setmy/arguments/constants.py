from info.setmy.arguments.argument import Argument
from info.setmy.string.operations import split_and_trim

SMI_PROFILES_ARGUMENT = Argument('smi-profiles', 'p', split_and_trim,
                                 'Comma separated profiles string.', False)
SMI_CONFIG_PATHS_ARGUMENT = Argument('smi-config-paths', 'c', split_and_trim,
                                     'Comma separated config paths.', False)
SMI_OPTIONAL_CONFIG_FILE_PATH_ARGUMENT = Argument('smi-optional-config-file', 'o', split_and_trim,
                                                  'Optional config file paths.', False)
