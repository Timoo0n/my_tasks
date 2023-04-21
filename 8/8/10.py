from itertools import *
k = 0

for x in set(product('ЧН70', repeat=10)):
    s = ''.join(x)
    if s[0] != '0' and s.count('7') == 5 and 'Н7' not in s\
       and '7Н' not in s and '77' not in s:
        k += 3**(s.count('Ч')+s.count('Н'))
print(k)
