def largest_num(item_list):
    largest = item_list[0]
    for item in item_list:
        if item > largest:
            largest = item
    return largest


print(largest_num([1, 5, 6, 2]))
