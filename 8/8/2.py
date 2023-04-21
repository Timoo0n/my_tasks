from itertools import product

k = 0

for i in product('01234567', repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('6') == 1:
        s = s.replace('3', '1').replace('5', '1').replace('7', '1')
        if '16' not in s and '61' not in s: k += 1
print(k)
