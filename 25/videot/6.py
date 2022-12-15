def div(num):
    my_set = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def main():
    for i in range(250_000, 250_201):
        r = list(filter(lambda el: el % 2 == 0, div(i)))
        if len(r) == 6:
            print(r[4], r[5])


if __name__ == '__main__': main()
