def parse_log(log):
    lines = []
    for prop, value in log.items():
        if value["status"] == "nested":
            value = "complex"
        lines.append(f"[Property: {prop}] = {value}")
    return "\n".join(lines)
