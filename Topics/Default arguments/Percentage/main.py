def get_percentage(number, round_digits=None):
    if round_digits is None:
        return "{0}%".format(str(round(number * 100)))
    else:
        return "{0}%".format(str(round(number * 100, round_digits)))