sample_list = [(1,2), (3,4,5),(7,6,9), (5,5),(2,2),(6,5)]
print("Original list:", sample_list)
sample_list.sort(key=lambda x:x[-1])
print("Sorted list:",sample_list)