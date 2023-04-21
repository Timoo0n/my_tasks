from itertools import *
k = 0

for x in product('ЧН', repeat=8):
    s = ''.join(x)
    if s.count('Ч') == 3:
        if s[0] == 'Ч': k +=7*8**7
        else: k += 8**8
print(k)
