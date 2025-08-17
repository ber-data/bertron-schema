"""Sample data, and functions that facilitate accessing that sample data."""

import json
from importlib import resources
from typing import Any

import yaml


def get_sample_data_text(file_path: str, encoding: str = "utf-8") -> str:
    """Get the text content of a sample data file.

    Args:
        file_path: The path to the sample data file, relative to the `sample_data/` directory.
        encoding: The text encoding to use when reading the file.

    Returns:
        The text content of the specified sample data file.

    References:
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files
    - https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file
    - https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable

    """
    # Define the path someone could use to `import` the Python package _containing_ the
    # `invalid/` and `valid/` directories (e.g. `import {something}`); which, currently,
    # happens to be the directory containing this `__init__.py` file.
    package_import_path = "sample_data"

    # Create a `Traversable` object that can be passed to the `resources.as_file()` function.
    traversable_resource_container = resources.files(package_import_path).joinpath(file_path)

    # Get a handle for the asset file (as a `Path` object).
    with resources.as_file(traversable_resource_container) as path:

        # Return the text content of the file.
        return path.read_text(encoding=encoding)


def get_sample_data(file_path: str, encoding: str = "utf-8") -> Any:  # noqa: ANN401
    """Get a Python value representing the content of a JSON/YAML-formatted sample data file.

    Args:
        file_path: The path to the sample data file, relative to the `sample_data/` directory.
        encoding: The text encoding to use when reading the file.

    Returns:
        The content of the specified sample data file, parsed into a Python value
        (in practice this is typically a dictionary or list).

    """
    # Determine which parsing function we will use, based upon the file's extension.
    if file_path.endswith((".yaml", ".yml")):
        parse = yaml.safe_load
    elif file_path.endswith(".json"):
        parse = json.loads
    else:
        # Raise an error indicating that we don't support files having that extension.
        # Note: The `!r` after the in-string variable below calls `repr()` on the value.
        #       Since the value is a string, the string will appear wrapped in quotes.
        msg = f"File extension suggest an unsupported file type: {file_path!r}"
        raise ValueError(msg)

    text = get_sample_data_text(file_path, encoding=encoding)
    return parse(text)
