def check_key(dict_1, key):
    if key in dict_1:  # if key in dict.keys()
        print("Present,", end=" ")
        print("Value = ", dict_1[key])
    else:
        print("Not Present")


dict_1 = {'a': 100, 'b': 200, 'c': 300}
key = 'b'
check_key(dict_1, key)
key = 'w'
check_key(dict_1, key)