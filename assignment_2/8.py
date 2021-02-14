def remove_nth_char(input_str, n):
    if len(input_str) < 1:
        raise Exception("Sorry, empty string not allowed")
    if n > len(input_str):
        raise Exception("Character to be removed not within word range")
    else:
        upto_n = input_str[:n]
        after_n = input_str[n + 1:]

        return upto_n + after_n


print(remove_nth_char('python', 0))
print(remove_nth_char('python', 1))
print(remove_nth_char('python', 6))
# print(remove_nth_char('p', 4))
# print(remove_nth_char('', 0))