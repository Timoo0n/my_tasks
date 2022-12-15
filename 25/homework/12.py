def div(x):
    s = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def main():
    for i in range(25317, 51237+1):
        r = list(filter(lambda el: p(el), div(i)))
        if len(r) >= 6:
            print(i, max(r))


main()
