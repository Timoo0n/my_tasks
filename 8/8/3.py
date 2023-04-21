from itertools import permutations

k = 0

for i in set(permutations('АББАТИСА', r=8)):
    s = ''.join(i)
    s = s.replace('Т', 'Б').replace('С', 'Б')
    s = s.replace('И', 'А')
    if 'АА' not in s and 'ББ' not in s: k += 1
print(k)
