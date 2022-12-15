def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    n = 500_001
    c = 0
    while c != 5:
        r = list(filter(lambda el: el % 10 == 8 and el != 8, div(n)))
        if len(r) != 0:
            print(n, min(r)); c += 1
        n += 1


if __name__ == '__main__': main()
