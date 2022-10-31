def dividers(num):
    my_set = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def dividers_1(num):
    return sorted({j for i in range(1, int(num**0.5)+1) if num % i == 0 for j in (i, num // i)})


def main():
    num = 120_000_000_000_000
    print(dividers_1(num))


if __name__ == '__main__':
    main()