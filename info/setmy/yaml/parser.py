from info.setmy import yaml


def parse_yaml_file(file_name: str):
    with open(file_name, 'r') as yaml_file:
        return yaml.safe_load(yaml_file)
    return None
