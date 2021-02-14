def enquiry(enquiry_list):
    if not enquiry_list:
        return "Empty list"
    else:
        return "Non empty list"


print(enquiry([]))
print(enquiry([1, 2, 3]))
