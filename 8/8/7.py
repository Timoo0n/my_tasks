from itertools import *
k = 0

for x in product('ЧН', repeat=11):
    s = ''.join(x)
    if x.count('Н') == 4 and 'НН' not in s:
        if s[0] == 'Ч': k += 3*4**10
        else: k += 4**11
print(k)
