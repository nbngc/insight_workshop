a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# print(list(set(a)))


def remove_duplicate(duplicates):
    final_list = []
    for num in duplicates:
        if num not in final_list:
            final_list.append(num)
    return final_list


print(remove_duplicate(a))
