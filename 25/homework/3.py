def div(x):
    my_set = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: my_set |= {i, x // i}
    return sorted(my_set)


def main():
    count = 0
    n = 250_201

    while count != 50:
        r = div(n)
        if len(r) != 0 and (max(r)+min(r)) % 123 == 17:
            print(n, max(r)+min(r)); count += 1
        n += 1


if __name__ == '__main__': main()
