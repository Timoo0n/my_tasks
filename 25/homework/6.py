def div(x):
    s = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0: s |= {i, x // i}
    return sorted(s)


def main():
    for i in range(190_201, 190_261):
        l = sorted(list(filter(lambda el: el % 2 == 0, div(i))))
        if len(l) == 4:
            print(l[3], l[2])


main()
