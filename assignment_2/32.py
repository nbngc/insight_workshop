def generate_dict(n):
    sq_dict = {}
    for i in range(1, n + 1):
        sq_dict[i] = i * i
    print(sq_dict)


n = int(input("Enter a number:"))
generate_dict(n)
