import pytest
from conftest import PARSERS, get_fixture_path
from gendiff.parser import parse_files


@pytest.mark.parametrize(
    "file_1, file_2, type_1, type_2",
    [
        ("file1.doc", "file2.json", "wrong", "flat"),
        ("file1.doc", "file1.txt", "wrong", "wrong"),
        ("file1.yml", "file1.txt", "flat", "wrong"),
        ("file1.yaml", "file1.doc", "nested", "wrong"),
    ],
)
def test_wrong_file_type(file_1, file_2, type_1, type_2):
    path_1 = get_fixture_path(file_1, type_1)
    path_2 = get_fixture_path(file_2, type_2)
    with pytest.raises(NotImplementedError):
        parse_files(path_1, path_2)


@pytest.mark.parametrize(
    "file_1, file_2, type_1, type_2",
    [
        ("file1.yaml", "file2.json", "flat", "flat"),
        ("file1.json", "file1.yaml", "flat", "nested"),
        ("file1.yaml", "file1.json", "nested", "nested"),
        ("file1.json", "file2.yml", "flat", "flat"),
    ],
)
def test_different_file_types(file_1, file_2, type_1, type_2):
    path_1 = get_fixture_path(file_1, type_1)
    path_2 = get_fixture_path(file_2, type_2)
    with pytest.raises(ValueError):
        parse_files(path_1, path_2)


@pytest.mark.parametrize(
    "file_1, file_2, data_type, parser",
    [
        ("file1.json", "file2.json", "flat", ".json"),
        ("file1.json", "file2.json", "nested", ".json"),
        ("file1.yml", "file1.yml", "flat", ".yml"),
        ("file1.yaml", "file2.yaml", "nested", ".yaml"),
    ],
)
def test_parse_files(file_1, file_2, data_type, parser):
    path_1 = get_fixture_path(file_1, data_type)
    path_2 = get_fixture_path(file_2, data_type)
    parser = PARSERS[parser]
    with open(path_1, "r") as f1, open(path_2, "r") as f2:
        expected = (parser(f1), parser(f2))
    actual = parse_files(path_1, path_2)
    assert actual == expected
