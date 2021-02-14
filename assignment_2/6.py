def not_poor(input_string):
    str_not = input_string.find('not')
    str_poor = input_string.find('poor')

    if str_poor > str_not > 0 and str_poor > 0:
        input_string = input_string.replace(input_string[str_not:(str_poor + 4)], 'good')
        return input_string
    elif input_string.find('good'):
        input_string = input_string.replace('good', 'poor')
        return input_string
    else:
        return input_string


print(not_poor('The lyrics is not that poor!'))
print(not_poor('the lyrics is good'))