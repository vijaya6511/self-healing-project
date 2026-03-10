def get_selector(by, value):
    if by == "id":
        return f"#{value}"
    elif by == "class":
        return f".{value}"
    elif by == "name":
        return f"[name='{value}']"
    elif by == "css":
        return value
    elif by == "xpath":
        return f"xpath={value}"
    else:
        raise Exception(f"Unsupported locator type: {by}")