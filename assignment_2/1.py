# 1. Write a Python program to count the number of characters (character frequency) in a string.
#     Sample String : google.com'
#     Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

stringA = 'google.com'
print("Given String:", stringA)

count_dict = {i: stringA.count(i) for i in list(stringA)}
print("Frequency of each character :\n ", count_dict)
