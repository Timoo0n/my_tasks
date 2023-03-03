from itertools import product
c = 0
for word in product('РУСЛАН', repeat=5):
    if word.count('У') <= 1 and word.count('А') <= 1: c += 1
print(c)
