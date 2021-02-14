def add_item_tuple(tup, idx, value):
    tup_list = list(tup)
    tup_list[idx] = value
    return tuple(tup_list)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
print(add_item_tuple(fruits, 2, 'papaya'))