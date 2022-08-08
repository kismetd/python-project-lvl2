CONVERSION_TABLE = {
    "False": "false",
    "True": "true",
    "None": "null",
}


STATUS_TABLE = {
    "old": "- ",
    "new": "+ ",
    "removed": "- ",
    "added": "+ ",
    "unchanged": "  ",
    "nested": "  ",
}


def parse_val(val):
    val = str(val)
    if CONVERSION_TABLE.get(val):
        return CONVERSION_TABLE[val]
    return val
