def div(x):
    my_set = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            my_set |= {i, x // i}
    return sorted(my_set)


def main():
    my_list = []
    for i in range(174457, 174506):
        r = div(i)
        if len(r) == 2:
            my_list += [r]
    sorted_list = sorted(my_list, key=lambda el: el[0]*el[1])
    for i in sorted_list:
        print(*i)


if __name__ == '__main__': main()
