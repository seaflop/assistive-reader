import os

vowels = "aeiou"

def ensure_type(variable, variable_type: type):
    if (not isinstance(variable, variable_type)):
        raise TypeError(f"{variable=} must be a {variable_type}")

def ensure_file_extension(file_name: str, extension: str):
    if (not file_name.endswith(extension)):
        raise OSError(f"{file_name=} must be {extension} format")

def ensure_file_exists(file_name: str):
    if (not os.path.isfile(file_name)):
        raise OSError(f"{file_name=} not found")