import json
from pathlib import Path

import yaml

PARSERS = {
    ".json": json.load,
    ".yaml": yaml.safe_load,
    ".yml": yaml.safe_load,
}


def _check_file_type_support(type_1, type_2):
    for s in (type_1, type_2):
        if not PARSERS.get(s):
            raise NotImplementedError(
                f"Invalid filetype. No support for {s} files.",
            )


def _check_same_file_type(type_1, type_2):
    if not PARSERS[type_1] == PARSERS[type_2]:
        raise ValueError("Can't compare different filetypes.")


def parse_files(file1, file2):
    path1, path2 = Path(file1).resolve(), Path(file2).resolve()
    sffx_1, sffx_2 = path1.suffix, path2.suffix
    _check_file_type_support(sffx_1, sffx_2)
    _check_same_file_type(sffx_1, sffx_2)
    with open(path1, "r") as f1, open(path2, "r") as f2:
        file1 = PARSERS[sffx_1](f1)
        file2 = PARSERS[sffx_2](f2)
    return file1, file2
