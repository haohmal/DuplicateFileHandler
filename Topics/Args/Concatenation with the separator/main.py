def concat(*strings, sep=" "):
    result = ""
    for string in strings:
        if len(result) > 0:
            result += sep
        result += string
    return result