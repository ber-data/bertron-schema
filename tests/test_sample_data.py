"""Tests for sample data functions."""

import json

import pytest
import yaml

from sample_data import get_sample_data, get_sample_data_file_paths, get_sample_data_text


def test_get_sample_data_file_paths():
    """Test that get_sample_data_file_paths returns a list of file paths."""
    file_paths = get_sample_data_file_paths()
    
    # Should return a list
    assert isinstance(file_paths, list)
    
    # Should contain at least some files
    assert len(file_paths) > 0
    
    # All entries should be strings
    assert all(isinstance(path, str) for path in file_paths)
    
    # Should contain expected file extensions
    extensions = [path.split(".")[-1] for path in file_paths]
    assert any(ext in ["yaml", "yml", "json"] for ext in extensions)


def test_get_sample_data_text():
    """Test that get_sample_data_text can read sample files and returns strings."""
    file_paths = get_sample_data_file_paths()
    
    # Test with the first available file
    test_file = file_paths[0]
    text_content = get_sample_data_text(test_file)
    
    # Should return a string
    assert isinstance(text_content, str)
    
    # Should have some content
    assert len(text_content) > 0


def test_get_sample_data_text_with_encoding():
    """Test that get_sample_data_text respects the encoding parameter."""
    file_paths = get_sample_data_file_paths()
    test_file = file_paths[0]
    
    # Should work with explicit UTF-8 encoding
    text_content = get_sample_data_text(test_file, encoding="utf-8")
    assert isinstance(text_content, str)
    assert len(text_content) > 0


def test_get_sample_data_yaml():
    """Test that get_sample_data can parse YAML files correctly."""
    file_paths = get_sample_data_file_paths()
    
    # Find a YAML file to test
    yaml_files = [path for path in file_paths if path.endswith((".yaml", ".yml"))]
    assert len(yaml_files) > 0, "No YAML files found in sample data"
    
    test_file = yaml_files[0]
    data = get_sample_data(test_file)
    
    # Should parse into a Python object (typically dict or list)
    assert data is not None
    
    # Verify it's valid YAML by comparing with yaml.safe_load
    text_content = get_sample_data_text(test_file)
    expected_data = yaml.safe_load(text_content)
    assert data == expected_data


def test_get_sample_data_json():
    """Test that get_sample_data can parse JSON files correctly."""
    file_paths = get_sample_data_file_paths()
    
    # Find a JSON file to test
    json_files = [path for path in file_paths if path.endswith(".json")]
    
    if json_files:  # Only test if JSON files exist
        test_file = json_files[0]
        data = get_sample_data(test_file)
        
        # Should parse into a Python object
        assert data is not None
        
        # Verify it's valid JSON by comparing with json.loads
        text_content = get_sample_data_text(test_file)
        expected_data = json.loads(text_content)
        assert data == expected_data


def test_get_sample_data_unsupported_extension():
    """Test that get_sample_data raises ValueError for unsupported file types."""
    # Test with a fake file path with unsupported extension
    with pytest.raises(ValueError, match="File extension suggest an unsupported file type"):
        get_sample_data("fake_file.txt")


def test_get_sample_data_with_encoding():
    """Test that get_sample_data respects the encoding parameter."""
    file_paths = get_sample_data_file_paths()
    test_file = file_paths[0]
    
    # Should work with explicit UTF-8 encoding
    data = get_sample_data(test_file, encoding="utf-8")
    assert data is not None


def test_get_sample_data_specific_files():
    """Test that get_sample_data works with specific known files."""
    file_paths = get_sample_data_file_paths()
    
    # Should include both valid and invalid directories
    assert any("valid/" in path for path in file_paths)
    assert any("invalid/" in path for path in file_paths)
    
    # Test with a specific YAML file if it exists
    if "valid/Dataset-001.yaml" in file_paths:
        data = get_sample_data("valid/Dataset-001.yaml")
        assert isinstance(data, dict)
        assert "id" in data
    
    # Test with a JSON file if it exists  
    json_files = [path for path in file_paths if path.endswith(".json")]
    if json_files:
        data = get_sample_data(json_files[0])
        assert data is not None