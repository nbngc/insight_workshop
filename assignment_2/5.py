string_1 = 'abc'
string_2 = 'string'
string_3 = 'to'


def add_ing(input_string):
    if len(input_string) < 3:
        return input_string
    elif input_string[-3:] == 'ing':
        return input_string + 'ly'
    else:
        return input_string[-3:] + 'ing'


print(add_ing(string_1))
print(add_ing(string_2))
print(add_ing(string_3))
