def is_inrange(num, min_limit, max_limit):
    if num in range(min_limit, max_limit):
        print(f"{num} is in range ({min_limit}, {max_limit})")
    else:
        print("The num is outside the given range")


is_inrange(5, 3, 7)
