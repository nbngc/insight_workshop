def sum_list(items):
    sum_items = 0
    for item in items:
        sum_items += item
    return sum_items


print(sum_list([1, 2, 3, -5]))
print(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
