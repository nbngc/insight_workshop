def count_letter_case(input_str):
    lower_cnt = 0
    upper_cnt = 0
    for ltr in input_str:
        if ltr.isspace():
            continue
        elif ltr.islower():
            lower_cnt += 1
        elif ltr.isupper():
            upper_cnt += 1
        else:
            raise ValueError("Unrecognized character in the string")
    return lower_cnt, upper_cnt


lower, upper = count_letter_case('The quick Brow Fox')
print("No. of Upper case characters:", upper)
print("No. of Lower case characters:", lower)
