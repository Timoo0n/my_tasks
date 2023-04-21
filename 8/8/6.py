from itertools import permutations
k0 = 0

for i in permutations('ХЛЕБНЫЙМЯКИШ', r=7):
    s = ''.join(i)
    if s[0] == 'Х' and s[3] in 'БЫКИШ':
        for k in 'ЙЛБНМКШ': s = s.replace(k, 'Х')
        if 'ХХ' not in s: k0 += 1
print(k0)
