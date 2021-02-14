def count_first_and_last_same(str_list):
    count = 0
    for item in str_list:
        if len(item) >= 2 and item[0] == item[-1]:
            count += 1
    return count


print(count_first_and_last_same(['abc', 'xyz', 'aba', '1221']))
