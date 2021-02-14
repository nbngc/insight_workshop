def sum_items_dict(dict1):
    total = 0
    for key, value in dict1.items():
        total = total + value
    return total


d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print("Sum of values:", sum_items_dict(d))

# print(sum(d.values()))
