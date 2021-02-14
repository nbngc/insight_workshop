def del_key(d, key):
    print(d)
    if key in d:
        del d[key]
    return d


myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
key = 'a'
print(del_key(myDict, key))
