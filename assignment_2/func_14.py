
sample_dict = [{'make':'Nokia', 'color':'Black'},
               {'make':'Mi Max', 'color':'Gold'},
               {'make':'Samsung', 'color':'Blue'}]
print("Original Dictionary:\n", sample_dict)
print("Sorted Dictionary:")
sample_dict.sort(key=lambda x:x['color'])
print(sample_dict)