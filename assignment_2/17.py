def multiply_list(items):
    product = 1
    for item in items:
        product *= item
    return product


print(multiply_list([1, 2, 3, 4]))
