# Remove a certain element from a tuple
tup = (5, 6, 7,7, 2, 4, 6, 6, 6, 7,6, 10, 8)
N=6
rem = tuple(ele for ele in tup if ele!=N)
print(rem)

# Remove using index
tup1 = ('a','p','p','l','e')
idx = 2
tup1 = tup1[:2] + tup1[3:]
print(tup1)