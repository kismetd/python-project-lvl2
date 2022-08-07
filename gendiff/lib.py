from gendiff.diff_log import generate_log
from gendiff.parser import parse_files
from gendiff.renderers.log_like import parse_log
from gendiff.renderers.stylish import stylish

RENDERERS = {
    "stylish": stylish,
    "log-like": parse_log,
}


def generate_diff(file_1, file_2, style="stylish"):
    file_1, file_2 = parse_files(file_1, file_2)
    diff_log = generate_log(file_1, file_2)
    return RENDERERS[style](diff_log)
