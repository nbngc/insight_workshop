def filter_even_num(lst):
    evn = [item for item in lst if item % 2 == 0]
    return evn


sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(filter_even_num(sample_list))
