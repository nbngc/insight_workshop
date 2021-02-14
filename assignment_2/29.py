def concat_dict(*args):
    dict_final = {}
    for arg in args:
        dict_final.update(arg)
    print(dict_final)


dict1 = {1: 20, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
concat_dict(dict1, dict2, dict3)
