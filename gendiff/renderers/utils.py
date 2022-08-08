CONVERSION_TABLE = {
    "False": "false",
    "True": "true",
    "None": "null",
}


def parse_val(val):
    val = str(val)
    if CONVERSION_TABLE.get(val):
        return CONVERSION_TABLE[val]
    return val
