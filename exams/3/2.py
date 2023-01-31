from itertools import product

print("X Y W Z")
for x, y, w, z in product(range(2), repeat=4):
    value = (not (z <= x)) or (y == w) or w
    if not value:
        print(x, y, w, z)
