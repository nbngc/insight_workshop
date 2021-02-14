sample_str = 'abc'
starts = lambda x,y: True if x.startswith(y) else False

print(starts(sample_str, 'b'))
print(starts(sample_str, 'a'))
print(starts('xyz', 'x'))
print(starts('klms', 'a'))