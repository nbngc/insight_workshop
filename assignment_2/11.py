sample_str = "Peter Piper picked a peck of pickled peppers A peck of pickled peppers Peter Piper picked If Peter " \
             "Piper picked a peck of pickled peppers Where’s the peck of pickled peppers Peter Piper picked "
counts = {}
word_list = sample_str.split()
for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
