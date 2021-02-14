sample_list = [67,976,56,43,44.5,123.35,45,56,74.4, 'xyz', 'abc']
integer_lst = list(filter(lambda x: True if type(x) == int else False, sample_list))
print(integer_lst)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# print("\nEven numbers from the above list:")
# even_nums = list(filter(lambda x: x%2 == 0, nums))
# print(even_nums)
# print("\nOdd numbers from the above list:")
# odd_nums = list(filter(lambda x: x%2 != 0, nums))
# print(odd_nums)
