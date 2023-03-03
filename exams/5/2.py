from itertools import product

print("A B C")
for a, b, c in product(range(2), repeat=3):
    value = (a and (not c)) or ((not b) and (not c))
    if value:
        print(a, b, c)
