from itertools import product

print('X Y Z')
for x, y, z in product(range(2), repeat=3):
    value = ((not x) and y and z) or ((not x) and (not y) and z) or((not x) and (not y) and (not z))
    if value: print(x, y, z)
