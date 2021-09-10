# put your python code here
def multiply(*kargs):
    result = 1
    for num in kargs:
        result *= num
    return result
