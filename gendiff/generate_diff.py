from gendiff.diff_log import get_diff
from gendiff.parser import parse_files
from gendiff.renderers.json import json_format
from gendiff.renderers.plain import format as plain
from gendiff.renderers.stylish import format as stylish

RENDERERS = {
    "stylish": stylish,
    "plain": plain,
    "json": json_format,
}


def generate_diff(file_1, file_2, style="stylish"):
    file_1, file_2 = parse_files(file_1, file_2)
    diff_log = get_diff(file_1, file_2)
    return RENDERERS[style](diff_log)
