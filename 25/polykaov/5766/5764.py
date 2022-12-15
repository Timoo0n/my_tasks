def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    c = 0
    for i in range(5917, 10_000):
        r = list(filter(lambda el: el % 2 == 1, div(i**2)))
        if len(r) == 5:
            print(i**2, max(r)); c += 1
        if c == 5: break

main()
