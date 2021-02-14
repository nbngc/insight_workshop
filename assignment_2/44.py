def slice_tuple(tup, start=0, end = -1):
    _slice = tup[start:end]
    return _slice


tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
print(slice_tuple(tuplex, start=2, end=6))
print(slice_tuple(tuplex, start=2))
print(slice_tuple(tuplex, end=6))
print(slice_tuple(tuplex, start=-8, end=-4))
