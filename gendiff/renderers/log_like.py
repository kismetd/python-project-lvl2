def parse_log(log):
    lines = []
    for prop in sorted(log):
        value = log[prop]
        if value["status"] == "nested":
            value = "complex"
        lines.append(f"[Property: {prop}] = {value}")
    return "\n".join(lines)
