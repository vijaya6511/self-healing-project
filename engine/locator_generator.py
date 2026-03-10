def generate_locator(element):

    if element["id"]:
        return ("id", element["id"])

    if element["class"]:
        class_name = element["class"].split()[0]
        return ("css", f".{class_name}")

    if element["text"]:
        return ("xpath", f"//{element['tag']}[text()='{element['text']}']")

    return ("tag", element["tag"])