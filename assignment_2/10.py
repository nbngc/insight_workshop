def del_odd_index(input_str):
    new_word = [ch for idx, ch in enumerate(input_str) if idx % 2 == 0]
    return "".join(new_word)


print(del_odd_index('python'))