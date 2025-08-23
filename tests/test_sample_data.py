"""Tests targeting functions that expose sample data."""

import json

import pytest
import yaml

from sample_data import get_sample_data, get_sample_data_file_paths, get_sample_data_text


def test_get_sample_data_file_paths_returns_a_list_of_file_paths() -> None:
    """Test that get_sample_data_file_paths returns a list of file paths."""
    paths = get_sample_data_file_paths()

    # Assert that the returned value is a non-empty list, and that each item in the list
    # is a string that ends with one of the supported filename extensions.
    assert isinstance(paths, list)
    assert len(paths) > 0
    assert all(isinstance(path, str) for path in paths)
    assert all(path.endswith((".yaml", ".yml", ".json")) for path in paths)


def test_get_sample_data_file_paths_return_value_includes_known_paths() -> None:
    """Test that get_sample_data_file_paths returns paths to sample data files that we know exist.

    Note: This test may become stale over time, as the `sample_data/` directory evolves.
    """
    paths = get_sample_data_file_paths()
    assert "invalid/Dataset-001.yaml" in paths
    assert "valid/Dataset-001.yaml" in paths
    assert "valid/emsl-example.json" in paths


def test_get_sample_data_text_returns_sample_data_as_a_string() -> None:
    """Test that get_sample_data_text returns sample data as a string."""
    paths = get_sample_data_file_paths()
    assert len(paths) > 0, "No sample data files were found"

    # Get the text content of the first sample data file, and assert that it is
    # a string consisting of something other than whitespace.
    text = get_sample_data_text(paths[0])
    assert isinstance(text, str)
    assert len(text.strip()) > 0


def test_get_sample_data_text_return_value_includes_known_text() -> None:
    """Test that get_sample_data_text returns text content from a known sample data file.

    Note: This test may become stale over time, as the names and content of
          the files in the `sample_data/` directory evolve.
    """
    text = get_sample_data_text("valid/Dataset-001.yaml")
    assert "id" in text

    text = get_sample_data_text("valid/emsl-example.json")
    assert "id" in text


def test_get_sample_data_returns_yaml_sample_data_as_python_object() -> None:
    """Test that get_sample_data returns YAML-formatted sample data as a Python object."""
    # Identify a YAML file we can use for testing.
    paths = get_sample_data_file_paths()
    yaml_file_paths = [path for path in paths if path.endswith((".yaml", ".yml"))]
    assert len(yaml_file_paths) > 0, "No YAML files were found among the sample data"

    # Get the sample data from the first identified YAML-formatted sample data file,
    # and assert that it has been parsed into the same Python object that we get
    # when we read the file's text content and parse it with `yaml.safe_load`.
    yaml_file_path = yaml_file_paths[0]
    data = get_sample_data(yaml_file_path)
    text = get_sample_data_text(yaml_file_path)
    assert data == yaml.safe_load(text)


def test_get_sample_data_returns_json_sample_data_as_python_object() -> None:
    """Test that get_sample_data returns JSON-formatted sample data as a Python object."""
    # Identify a JSON file we can use for testing.
    paths = get_sample_data_file_paths()
    json_file_paths = [path for path in paths if path.endswith(".json")]
    assert len(json_file_paths) > 0, "No JSON files were found among the sample data"

    # Get the sample data from the first identified JSON-formatted sample data file,
    # and assert that it has been parsed into the same Python object that we get
    # when we read the file's text content and parse it with `json.loads`.
    json_file_path = json_file_paths[0]
    data = get_sample_data(json_file_path)
    text = get_sample_data_text(json_file_path)
    assert data == json.loads(text)


def test_get_sample_data_rejects_unsupported_filename_extensions() -> None:
    """Test that get_sample_data raises an exception for an unsupported filename extension."""
    with pytest.raises(ValueError, match=r"^Filename extension"):
        get_sample_data("my_file.txt")


def test_get_sample_data_return_value_is_object_having_known_attributes() -> None:
    """Test that get_sample_data returns an object having attributes that are among those we expect.

    Note: This test may become stale over time, as the names and content of
          the files in the `sample_data/` directory evolve.
    """
    # Get the sample data from a known YAML file, and assert that it matches
    # the expected Python object.
    data = get_sample_data("valid/Dataset-001.yaml")
    assert isinstance(data, dict)
    assert all(key in data for key in ["id", "name"])

    # Get the sample data from a known JSON file, and assert that it matches
    # the expected Python object.
    data = get_sample_data("valid/emsl-example.json")
    assert isinstance(data, dict)
    assert all(key in data for key in ["id", "name"])
