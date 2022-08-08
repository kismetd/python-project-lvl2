def to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    return f"{value}"


def make_line(state, path, old=None, new=None, value=None):
    path = ".".join(path)
    if state == "removed":
        line = f"Property '{path}' was removed"
    elif state == "changed":
        line = f"Property '{path}' was updated. From {old} to {new}"
    elif state == "added":
        line = f"Property '{path}' was added with value: {value}"
    else:
        line = ""
    return line


def format(diff, path=None):
    if path is None:
        path = []
    result = []
    for key in sorted(diff):
        path.append(key)
        data = diff[key]
        stat = data["status"]

        if stat == "nested":
            result.append(format(data["value"], path))

        if stat == "changed":
            old_value = to_str(data["old"])
            new_value = to_str(data["new"])
            line = make_line(stat, path, old_value, new_value)
        else:
            value = to_str(data["value"])
            line = make_line(stat, path, value=value)

        path.pop()
        result.append(line)
    return "\n".join(line for line in result if line)
