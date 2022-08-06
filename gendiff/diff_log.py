def generate_log(file_1, file_2):
    log = []
    for key, value in file_1.items():
        if file_2.get(key):
            if value == file_2[key]:
                log.append({"property": key, "unchanged": str(value)})
            else:
                log.append(
                    {
                        "property": key,
                        "old": str(value),
                        "new": str(file_2[key]),
                    }
                )
        else:
            log.append({"property": key, "old": str(value)})
    # check file_2 for values that were not present in file_1
    for key, value in file_2.items():
        if not file_1.get(key):
            log.append({"property": key, "new": str(value)})
    # sort in alphanumeric order by property name
    log.sort(key=lambda x: x["property"])
    return log


def _parse_property(entry, stat):
    val_stat = stat
    if stat == "removed":
        val_stat = "old"
    elif val_stat == "added":
        val_stat = "new"
    prpt = entry["property"]
    t = "flat"
    val = (
        "complex" if isinstance(entry[val_stat], dict) else entry[val_stat]
    )  # noqa E501
    if val == "complex":
        t = "nested"
    return f"Property: [{prpt}]. Type: [{t}]. Status: [{stat}]. Value: [{val}]"


def _parse_changed_property(entry):
    prpt = entry["property"]
    t = "flat"
    val_1 = "complex" if isinstance(entry["old"], dict) else entry["old"]
    val_2 = "complex" if isinstance(entry["new"], dict) else entry["new"]
    if val_1 == "complex" or val_2 == "complex":
        t = "nested"
    return (
        f"Property: [{prpt}]. Type: [{t}]."
        f" Status: [changed]. Value: was=[{val_1}], now=[{val_2}]"
    )


def parse_log(log):
    outp = []
    for entry in log:
        if entry.get("old") and entry.get("new"):
            outp.append(_parse_changed_property(entry))
        elif entry.get("old") and not entry.get("new"):
            outp.append(_parse_property(entry, "removed"))
        elif entry.get("new") and not entry.get("old"):
            outp.append(_parse_property(entry, "added"))
        elif entry.get("unchanged"):
            outp.append(_parse_property(entry, "unchanged"))
    return "\n".join(outp)
