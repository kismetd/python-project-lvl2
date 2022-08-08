from itertools import chain

from .utils import STATUS_TABLE, parse_val

SPACE = " "


def format_value(tree, spaces=2):
    step = 4

    def _walk(node, depth):
        if not isinstance(node, dict):
            return parse_val(node)

        line = []

        for key, value in node.items():
            indent = SPACE * (depth + step)
            val = _walk(value, depth + step)
            line.append(f"{indent}{key}: {val}")
        result = chain("{", line, [depth * SPACE + "}"])
        return "\n".join(result)

    return _walk(tree, spaces)


def form_line(key, value, stat, indent):
    sign = STATUS_TABLE[stat]
    return f"{indent * SPACE}{sign}{key}: {value}"


def format(tree, spaces=2):
    step = 4
    inner_step = step // 2

    def _walk(node, depth):
        lines = []

        for key in sorted(node):
            prop = node[key]
            stat = prop["status"]
            value = prop.get("value")

            if stat == "nested":
                value = format(value, depth + step)

            if stat == "changed":
                old_value = format_value(prop["old"], depth + inner_step)
                lines.append(form_line(key, old_value, "removed", depth))
                new_value = format_value(prop["new"], depth + inner_step)
                lines.append(form_line(key, new_value, "added", depth))
                continue

            value = format_value(value, depth + inner_step)
            lines.append(form_line(key, value, stat, depth))

        result = chain("{", lines, [(depth - inner_step) * SPACE + "}"])
        return "\n".join(result)

    return _walk(tree, spaces)
