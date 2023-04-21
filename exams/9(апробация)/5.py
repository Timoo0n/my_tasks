def f(n):
    k = bin(n)[2:]
    if n % 2 == 0: k = '10' + k
    else: k = '1' + k + '01'

    return int(k, 2)

mx = 0
for n in range(9):
    mx = max(mx, f(n))
print(mx)
