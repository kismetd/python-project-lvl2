_VAL_STATUS = {
    "unchanged": "  ",
    "old": "- ",
    "new": "+ ",
}

_CONVERSION = {
    "False": "false",
    "True": "true",
    "None": "null",
}


def stylish(log, indent="  "):
    diff = []
    for entry in log:
        prop = entry["property"]
        for key, val in entry["values"].items():
            status = _VAL_STATUS[key]
            if _CONVERSION.get(val):
                val = _CONVERSION[val]
            diff.append(f"{indent}{status}{prop}: {val}")
    return "\n".join(["{"] + diff + ["}"])
