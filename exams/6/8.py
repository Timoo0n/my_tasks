from itertools import product

c = 0
for i in product('ABCDX', repeat=4):
    if i.count('X') == 1: c += 1
print(c)
