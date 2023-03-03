from itertools import product

for a, b, c in product(range(10), repeat=3):
    n = int(f'2{a}34{b}56{c}8')
    if n % 151 == 0:
        print(n, n // 151)
