def change_str(input_str):
    new_str = input_str[-1]+ input_str[1:-1] + input_str[0]
    return new_str


print(change_str('python'))
print(change_str('1python2'))