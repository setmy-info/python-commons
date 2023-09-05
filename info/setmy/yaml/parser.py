import yaml


def parse_yaml_file(file_name: str):
    with open(file_name, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
        return yaml_data
    return None
