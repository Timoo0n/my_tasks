def dividers(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def main():
    for i in range(81234, 134690):
        result = dividers(i)
        if len(result) == 3:
            print(min(result), max(result))


if __name__ == '__main__':
    main()