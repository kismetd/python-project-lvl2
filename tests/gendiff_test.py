from pathlib import Path

import pytest
from conftest import get_fixture_path
from gendiff.lib import generate_diff


@pytest.mark.parametrize(
    "file_1, file_2, type, output, formatter",
    [
        ("file1.json", "file2.json", "flat", "flat-diff.txt", "stylish"),
        ("file1.yaml", "file2.yaml", "flat", "flat-diff.txt", "stylish"),
        ("file1.yml", "file2.yml", "flat", "flat-diff.txt", "stylish"),
        ("file1.yml", "file2.yaml", "flat", "flat-diff.txt", "stylish"),
    ],
)
def test_flat_files_stylish(file_1, file_2, type, output, formatter):
    file_1 = get_fixture_path(file_1, type)
    file_2 = get_fixture_path(file_2, type)
    diff_path = Path(get_fixture_path(output, formatter, True))
    with diff_path.open() as expected:
        expected = diff_path.read_text()
    assert generate_diff(file_1, file_2, formatter) == expected
