def dividers(num):
    my_set = set()
    for i in range(1, int(num**0.5)):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def main():
    for i in range(326496, 649633):
        result = dividers(i)
        list0 = [i for i in result if i % 2 == 0]
        list1 = [i for i in result if i % 2 == 1]
        if (len(list1) >= 70 and len(list0) >= 70) and (len(list1) == len(list0)):
            result = list(filter(lambda el: el > 1000, result))
            print(i, min(result))


if __name__ == '__main__':
    main()
