"""Data test."""

import glob
import os
import sys
from pathlib import Path

from linkml_runtime.loaders import yaml_loader

# Add src to path so we can import schema
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from schema.datamodel.bertron_schema_pydantic import Entity

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA_DIR = os.path.join(ROOT, "src", "sample_data")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, "*.yaml"))


def test_data() -> None:
    """Data test."""
    for path in EXAMPLE_FILES:
        obj = yaml_loader.load(path, target_class=Entity)
        assert obj
