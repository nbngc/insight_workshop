
is_num = lambda q: q.replace('.','',1).isdigit()  # replace decimal with space  for first occurance
print(is_num('26587'))
print(is_num('4.2365'))
print(is_num('4.2.365'))
print(is_num('-12547')) #negative num not passed till now
print(is_num('00'))
print(is_num('A001'))
print(is_num('001'))
print("\nchecking negative numbers:")
# if the string has - at the start check only the rest for is num else check the string
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('-16.4'))
print(is_num1('-24587.11'))
