def alg(n):
    n = bin(n)[2:]
    n = '1' + n[:-2] + '10' if n.count('1') % 2 == 0 else '10' + n[2:] + '1'
    return int(n, 2)

for i in range(1000):
    r = alg(i)
    if r > 202: print(i); break
