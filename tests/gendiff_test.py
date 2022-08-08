from pathlib import Path

import pytest
from conftest import get_fixture_path
from gendiff.generate_diff import generate_diff


@pytest.mark.parametrize(
    "file_1, file_2, type, output, formatter",
    [
        ("file1.json", "file2.json", "flat", "flat-diff.txt", "stylish"),
        ("file1.yaml", "file2.yml", "flat", "flat-diff.txt", "stylish"),
    ],
)
def test_flat_files(file_1, file_2, type, output, formatter):
    file_1 = get_fixture_path(file_1, type)
    file_2 = get_fixture_path(file_2, type)
    diff_path = Path(get_fixture_path(output, formatter, True))
    with diff_path.open() as expected:
        expected = diff_path.read_text()
    assert generate_diff(file_1, file_2, formatter) == expected


@pytest.mark.parametrize(
    "file_1, file_2, type, output, formatter",
    [
        ("file1.json", "file2.json", "nested", "nested-diff.txt", "stylish"),
        ("file1.yaml", "file2.yaml", "nested", "nested-diff.txt", "stylish"),
        ("file1.json", "file2.json", "nested", "nested-diff.txt", "plain"),
    ],
)
def test_nested_files(file_1, file_2, type, output, formatter):
    file_1 = get_fixture_path(file_1, type)
    file_2 = get_fixture_path(file_2, type)
    diff_path = Path(get_fixture_path(output, formatter, True))
    with diff_path.open() as expected:
        expected = diff_path.read_text()
    assert generate_diff(file_1, file_2, formatter) == expected
