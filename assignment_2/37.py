def product_dict(items):
    result = 1
    for key in items:
        result *= items[key]
    return result


d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Product of values:", product_dict(d))
