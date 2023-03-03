def alg(n1):
    n = bin(n1)[2:]

    for _ in range(2):
        if int(n, 2) % 2 == 0: n = n + '1'
        else: n = n + '0'

    return int(n,2)

for n in range(100):
    if alg(n) < 171:
        print(n)
