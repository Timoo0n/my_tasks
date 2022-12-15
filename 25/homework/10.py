def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    n = 550_001
    c = 0
    while c != 5:
        r = list(filter(lambda el: el % 10 == 7 or el == 7, div(n)))
        if len(r) == 3:
            print(n, max(r)); c += 1
        n += 1


main()
