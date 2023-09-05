import argparse

from info.setmy.arguments.config import Config


def parse_arguments(argv, config: Config):
    """
    Parses command-line arguments based on the provided configuration.

    Args:
        argv (list): List of command-line arguments.
        config (Config): Configuration object containing argument definitions.

    Returns:
        argparse.Namespace: Parsed command-line arguments as a namespace object.
    """
    parser = argparse.ArgumentParser(description=config.name)
    for argument in config.arguments:
        parser.add_argument(
            ('-' + argument.short_flag),
            ('--' + argument.name),
            type=argument.argument_type,
            help=argument.argument_help,
            required=argument.required
        )
    args = parser.parse_args(argv[1:])
    return args
