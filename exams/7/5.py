def alg(n):
    n = str(n)
    return int(''.join(sorted([str(int(n[0])*int(n[1])), str(int(n[2])*int(n[3]))], key=lambda el: int(el))))

for n in range(1000, 10_000):
    if alg(n) == 1214:
        print(n)
