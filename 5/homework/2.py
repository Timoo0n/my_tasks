def f2(num):
    num_2n = str(bin(num))[2:]
    if num % 2 == 0:
        num_2n += '01'
    elif num % 2 == 1:
        num_2n += '10'
    return int(num_2n, 2)


def main2():
    for i in range(1, 1000):
        print(i, f2(i))


if __name__ == '__main__':
    main2()