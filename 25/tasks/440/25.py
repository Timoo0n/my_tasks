def dividers(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}

    return sorted(my_set)


def main():
    for i in range(321654, 654321):
        result = dividers(i)
        if len(result) > 70:
            if all(j % 2 == 1 for j in result):  # list(map(lambda el: True if el % 2 == 1 else False, result))
                print(i, max(result))


if __name__ == '__main__':
    main()