import os, json



def is_json_file(filename):
        return filename.endswith('.json')

def read_json_file(filepath):
    with open(filepath, 'r') as json_file:
        data = json.load(json_file)
        data['filepath'] = os.path.relpath(os.path.dirname(filepath), 'modpacks')  # Get the relative path
        return data
    

def parse(directory='./modpacks'):
    """
    Retrieve JSON data from all .json files in subfolders of the specified directory.

    Args:
        directory (str): The directory to start searching for .json files (default is './modpacks').

    Returns:
        list: A list of JSON data dictionaries from all found .json files.
    """
    json_data = []

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if is_json_file(filename):
                json_path = os.path.join(dirpath, filename)
                data = read_json_file(json_path)
                json_data.append(data)
    return json_data