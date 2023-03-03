from itertools import product

print('X Y Z W')
for x, y, z, w in product(range(2), repeat=4):
    if ((((not x) and y) == z) and w):
        print(x, y, z, w)
