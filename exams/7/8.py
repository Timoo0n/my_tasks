from itertools import product

c = 0

for i in product('КАТЕР', repeat=3):
    if i.count('Р') >= 2: c += 1

print(c)
