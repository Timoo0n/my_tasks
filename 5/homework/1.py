def f1(num):
    n = str(bin(num))[2:]
    for _ in range(2):
        n += str(n.count('1') % 2)

    return int(n, 2)


def main1():
    for i in range(1, 1000):
        print(i, f1(i))


if __name__ == '__main__':
    main1()