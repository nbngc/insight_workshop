tup = tuple("Hello world")
print(tup)
# get index of the first item whose value is passed as parameter
index = tup.index('o')
print(index)
# define the index from which you want to search
index = tup.index('o', 5)
print(index)
# define the segment of the tuple to be searched
index = tup.index('r', 5, 9)
print(index)
# if item not exists in the tuple return ValueError Exception
index = tup.index('y')
