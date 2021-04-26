def sum(*item)
    if not item:
        return items
    output = type(items[0])()
    for item in items:
        output += item
    return output