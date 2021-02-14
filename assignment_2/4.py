# string_1 = input("Enter first string:")
# string_2 = input("Enter second string:")

string_1 = 'abc'
string_2 = 'xyz'

combined = string_2[:2] + string_1[2:] + " " + string_1[:2] + string_2[2:]
print(combined)
