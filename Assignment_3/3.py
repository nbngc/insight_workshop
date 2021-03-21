# Write code that will print out the anagrams (words that use the same
# letters) from a paragraph of text.

from collections import Counter
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts)
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts))
print("\nAnagrams of 'abcd' in the above string: ")
print(result)



# string = ["tod", "salt", "dot", "last", "mood", "doom"]
# for i in string:
#     for j in string:
#         if len(i) == len(j) and i != j:
#             for item in range(len(i)):
#                 for items in range(len(j)):
#                     if i[item] == j[items]:
#                         result = j
#     print("The anagram of {} is:".format(i), result)