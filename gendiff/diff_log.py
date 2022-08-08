def get_diff(old, new):
    log = {}
    removed = old.keys() - new.keys()
    added = new.keys() - old.keys()
    kept = old.keys() & new.keys()

    for key in kept:
        old_val = old[key]
        new_val = new[key]
        if isinstance(old_val, dict) and isinstance(new_val, dict):
            log[key] = {
                "status": "nested",
                "value": get_diff(old_val, new_val),
            }
        elif old_val == new_val:
            log[key] = {"status": "unchanged", "value": old_val}
        else:
            log[key] = {"status": "changed", "old": old_val, "new": new_val}

    for key in added:
        log[key] = {"status": "added", "value": new[key]}

    for key in removed:
        log[key] = {"status": "removed", "value": old[key]}

    return log
