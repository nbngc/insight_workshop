def trimmed_string(input_string):
    # convert the string into list
    input_string_list = list(input_string)
    final_string = ""
    final_list = []

    if len(input_string) < 2:
        final_string = "Empty String"
        return final_string
    else:
        final_list = input_string_list[:2] + input_string_list[-2:]
        final_string = final_string.join(final_list)
        #         print(final_string)
        return final_string


print(trimmed_string('python'))
print(trimmed_string('py'))
print(trimmed_string('w'))