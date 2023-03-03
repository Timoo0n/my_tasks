from itertools import product
c = 0
for i in product('ЛЕТО', repeat=4):
    if i[0] in ('Л', 'Т'):
        c += 1
print(c)
