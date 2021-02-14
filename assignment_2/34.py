def merge_dict(dict1, dict2):
    dict1.update(dict2)
    return dict1


dict1 = {1: 20, 2: 20}
dict2 = {3: 30, 4: 40}
print(merge_dict(dict1, dict2))
