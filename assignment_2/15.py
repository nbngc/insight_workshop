def insert_string_middle(brackets, word):
    return brackets[:2] + word + brackets[-2:]


print(insert_string_middle('{{}}', 'python'))
print(insert_string_middle('<<>>', 'PHP'))
print(insert_string_middle('{{}}', 'rubyonrails'))