from pathlib import Path

import pytest
from conftest import PARSERS, get_fixture_path
from gendiff import diff_log


@pytest.mark.parametrize(
    "file_1, file_2, type, output",
    [
        ("file1.json", "file2.json", "flat", "flat-diff.txt"),
        ("file1.yml", "file2.yaml", "flat", "flat-diff.txt"),
    ],
)
def test_parser_on_flat(file_1, file_2, type, output):
    path_1 = get_fixture_path(file_1, type)
    path_2 = get_fixture_path(file_2, type)
    suffix = "." + file_1.split(".")[1]
    parser = PARSERS[suffix]
    with open(path_1, "r") as f1, open(path_2, "r") as f2:
        file_1, file_2 = (parser(f1), parser(f2))
    log = diff_log.generate_log(file_1, file_2)
    actual = diff_log.parse_log(log)
    diff_path = Path(get_fixture_path(output, "diff-log", True))
    with diff_path.open() as expected:
        expected = diff_path.read_text()
    assert actual == expected
