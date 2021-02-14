def replace_last_elem_list(lst1, lst2):
    return lst1[:-1] + lst2


#     lst1[-1:] = lst2
#     return lst1

print(replace_last_elem_list([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))