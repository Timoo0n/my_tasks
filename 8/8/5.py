from itertools import product

k = 0

for i in product('ТИМАШЕВСК', repeat=5):
    s = ''.join(i)
    for x in 'МВСК': s = s.replace(x, 'Т')
    s = s.replace('А', 'И').replace('Е', 'И')
    if s.count('И') > s.count('Т') + s.count('Ш'):
        if 'ШИ' not in s and 'ИШ' not in s: k += 1

print(k)
