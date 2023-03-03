from itertools import product

print('W Z Y X')
for x, y, w, z in product(range(2), repeat=4):
    value = (not (w <= z)) or (x <= y) or (not x)
    if not value:
        print(w, z, y, x)
