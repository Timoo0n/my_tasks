def div(x):
    my_set = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            my_set |= {i, x // i}
    return sorted(my_set)


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def main():
    num = 450_001
    for i in range(num, num+50):
        r = div(i)
        if r:
            value = max(r)
            if not p(value):
                print(i, value)


if __name__ == '__main__': main()
