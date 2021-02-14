def insert_word_into_list_items(lst, word):
    return ['{}{}'.format(word, i) for i in lst]


print(insert_word_into_list_items([1, 2, 3, 4], 'emp'))
