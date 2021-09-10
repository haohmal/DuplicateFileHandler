orig_list = ['a', 'b', 'c']
result = blackbox(orig_list)
if id(result) == id(orig_list):
    print("modifies")
else:
    print("new")
