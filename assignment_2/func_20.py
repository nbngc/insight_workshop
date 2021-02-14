array_1 = [1,2,3,4,5,6,7,8,10]
array_2 = [2,4,1,8,9]

result = list(filter(lambda x: x in array_1, array_2))

print("Intersection of two arrays:", result)