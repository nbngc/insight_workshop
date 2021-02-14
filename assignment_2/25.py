def check_dict_empty_in_list(my_list):
    for d in my_list:
        if not d:
            return True
        else:
            return False


print(check_dict_empty_in_list([{}, {}, {}]))
print(check_dict_empty_in_list([{1, 2}, {}, {}]))
print(check_dict_empty_in_list([{1, 2}, {2, 5}]))
