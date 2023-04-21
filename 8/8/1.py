from itertools import product

k = 0

for x in product('012345', repeat=5):
    s = ''.join(x)
    if s[0] != '0':
        s = s.replace('2', '0').replace('4', '0')
        s = s.replace('3', '1').replace('5', '1')
        if '00' not in s and '11' not in s: k += 1
print(k)
