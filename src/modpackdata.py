from .jsonparser import parse

def get_modpack_data(name):
    modpacks_data = parse()
    # Filter the modpack data based on the provided name
    matching_modpacks = [modpack for modpack in modpacks_data if modpack['name'] == name]

    if matching_modpacks:
        # Return the first matching modpack (assuming unique names)
        return matching_modpacks[0]

    # Return None if no matching modpack was found
    return None