def alg(n):
    n = bin(2*n)[2:] 
    value = n.count('1')
    n = n + str(value % 2) + str(value % 2)
    return int(n, 2)

for n in range(1000):
    r = alg(n)
    if r > 249:
        print(n)
        break
