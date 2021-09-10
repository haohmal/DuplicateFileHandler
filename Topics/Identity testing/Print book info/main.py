def print_book_info(title, author=None, year=None):
    result = '"{}"'.format(title)
    if author is not None or year is not None:
        result += " was written"
    if author is not None:
        result += " by {}".format(author)
    if year is not None:
        result += " in {}".format(year)
    print(result)