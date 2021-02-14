import copy


def shallow_copy_list(li):
    li_copy = list(li)
    return li_copy


li1 = [4, 8, 2, 10, 18]
li2 = shallow_copy_list(li1)
print("Original list:", li1)
print("After Cloning:", li2)


def deep_copy_list(li):
    #     li_copy = copy.copy(li) #Shallow copy
    li_copy = copy.deepcopy(li)
    return li_copy


li1 = [4, 8, 2, 10, 18]
li2 = deep_copy_list(li1)
print("Original list:", li1)
print("After Cloning:", li2)
