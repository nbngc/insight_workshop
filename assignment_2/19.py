def smallest_num(item_list):
    smallest = item_list[0]
    for item in item_list:
        if item < smallest:
            smallest = item
    return smallest


print(smallest_num([1, 5, 6, 2]))
