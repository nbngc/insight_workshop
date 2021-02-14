def longest_word(input_list):
    len_list = [len(word) for word in input_list]
    return max(len_list)

sample_list = ['long', 'longer', 'longest']
l = longest_word(sample_list)

print("length of longest word in the list:", l)