def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def main():
    c = 0
    for i in range(500_000, 0, -1):
        s = sum(list(filter(lambda el: p(el), div(i))))
        if s != 0 and s % 10 == 0:
            print(i, s); c += 1
        if c == 7: break


main()
