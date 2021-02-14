def sort_last_elem(tup):
    tup.sort(key=lambda x: x[-1])
    return tup


tup = [(1, 3), (3, 2), (2, 1)]
print(sort_last_elem(tup))
