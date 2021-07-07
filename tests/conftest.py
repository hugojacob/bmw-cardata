"""
conftest.py
"""
import pathlib

import pytest


@pytest.fixture
def test_data() -> dict:
    data_dir = pathlib.Path(__file__).parent.resolve() / "data"

    return {data_file.name: data_file for data_file in data_dir.glob("*")}
