"""Data test."""

import glob
import os

from linkml_runtime.loaders import yaml_loader

from schema.datamodel.bertron_schema_pydantic import Entity

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "sample_data")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, "*.yaml"))


def test_data() -> None:
    """Data test."""
    for path in EXAMPLE_FILES:
        obj = yaml_loader.load(path, target_class=Entity)
        assert obj
