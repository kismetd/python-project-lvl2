def _parse_property(prop, vals, stat):
    val_stat = stat
    if stat == "removed":
        val_stat = "old"
    elif val_stat == "added":
        val_stat = "new"
    t = "flat"
    val = "complex" if isinstance(vals[val_stat], dict) else vals[val_stat]
    if val == "complex":
        t = "nested"
    return f"Property: [{prop}]. Type: [{t}]. Status: [{stat}]. Value: [{val}]"


def _parse_changed_property(prop, vals):
    t = "flat"
    val_1 = "complex" if isinstance(vals["old"], dict) else vals["old"]
    val_2 = "complex" if isinstance(vals["new"], dict) else vals["new"]
    if val_1 == "complex" or val_2 == "complex":
        t = "nested"
    return (
        f"Property: [{prop}]. Type: [{t}]."
        f" Status: [changed]. Value: was=[{val_1}], now=[{val_2}]"
    )


def parse_log(log):
    outp = []
    for entry in log:
        prop = entry["property"]
        vals = entry["values"]
        if vals.get("old") and vals.get("new"):
            outp.append(_parse_changed_property(prop, vals))
        elif vals.get("old") and not vals.get("new"):
            outp.append(_parse_property(prop, vals, "removed"))
        elif vals.get("new") and not vals.get("old"):
            outp.append(_parse_property(prop, vals, "added"))
        elif vals.get("unchanged"):
            outp.append(_parse_property(prop, vals, "unchanged"))
    return "\n".join(outp)
