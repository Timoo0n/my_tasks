def alg(n):
    n = bin(n)[2:]
    n = n + n[-1]
    for _ in range(2):
        if int(n, 2) % 2 == 0: n = n + '0'
        else: n = n + '1'
    return int(n, 2)

for n in range(100):
    if alg(n) > 97:
        print(n)
        break
