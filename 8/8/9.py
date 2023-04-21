from itertools import *
k = 0

for x in set(permutations('СГСГСГС')):
    s = ''.join(x)
    if 'ГГ' not in s: k += 36
print(k)
