from pathlib import Path


def get_fixture_path(file_name, type, is_output=False):
    fixt_dir = str(Path.cwd() / "tests" / "fixtures")
    if is_output:
        fixt_dir = fixt_dir + "/output"
        p = Path(fixt_dir) / type / file_name
    else:
        fixt_dir = fixt_dir + "/files"
        p = Path(fixt_dir) / type / file_name
    return str(Path(p))
