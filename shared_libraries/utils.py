import json
import yaml
import os

SHARED_LIBRARIES_DIR = './shared_libraries'

with open("./shared_libraries/index.json", 'r') as f:
    INTENT_INDEX = json.load(f)

def read_yaml_file(file_name: str) -> dict:
    """
    Reads a YAML file and returns its content.

    Args:
        file_name (str): The name of the YAML file within shared_libraries.

    Returns:
        dict or list: The content of the YAML file.
        None: If the file does not exist or an error occurs.
    """
    full_path = os.path.join("./shared_libraries/workflows", file_name)
    try:
        with open(full_path, 'r') as f:
            data = yaml.safe_load(f)
        return data
    except yaml.YAMLError as e:
        print(f"Error decoding YAML from {full_path}: {e}")
        return None
    except Exception as e:
        print(f"An error occurred while reading {full_path}: {e}")
        return None
