def sq_sum(*numbers):
    result = 0
    for num in numbers:
        result += num ** 2
    return result