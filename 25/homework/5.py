from functools import reduce


def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    n = 400_000_001
    c = 0
    while c != 10:
        r = div(n)
        if len(r) >= 5:
            p = reduce(lambda x, y: x*y, r[:5], 1)
            if p % 100 == 17 and p <= n:
                print(p, r[4]); c += 1
        n += 1

main()
