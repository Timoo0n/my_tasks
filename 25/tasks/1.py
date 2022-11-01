def dividers(num):
    my_set = set()
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num//i}

    return sorted(my_set)


def main():
    for i in range(193136, 193224):
        result = dividers(i)
        if len(result) == 6:
            print(*result)


if __name__ == '__main__':
    main()