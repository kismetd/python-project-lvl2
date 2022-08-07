def generate_log(file_1, file_2):
    log = []

    for key, value in file_1.items():
        prop = {"property": key}
        if file_2.get(key):
            if value == file_2[key]:
                prop["values"] = {"unchanged": str(value)}
            else:
                prop["values"] = {"old": str(value), "new": str(file_2[key])}
        else:
            prop["values"] = {"old": str(value)}
        log.append(prop)

    for key, value in file_2.items():
        if not file_1.get(key):
            prop = {"property": key}
            prop["values"] = {"new": str(value)}
            log.append(prop)

    log.sort(key=lambda x: x["property"])
    return log
