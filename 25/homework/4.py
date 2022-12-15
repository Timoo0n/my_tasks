def div(x):
    my_set = set()
    for i in range(2, int(x**0.5)):
        if x % i == 0: my_set |= {i, x // i}
    return sorted(my_set)


def main():
    n = 550_001
    c = 0
    while c != 50:
        r = div(n)
        if len(r) != 0:
            v = sum(r) // len(r)
            if v % 31 == 13:
                print(n, v); c += 1
        n += 1


if __name__ == '__main__': main()
