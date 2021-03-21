# 4. Create a list. Append the names of your colleagues and friends to it. Has the id of the list changed? Sort the
# list. What is the first item on the list? What is the second item on the list?

names = []

print("List ID:", id(names))
names.append("ram")
names.append("hari")
names.append("shyam")
print("List ID:", id(names))
names.sort()
print("First:", names[0])
print("Second:", names[1])