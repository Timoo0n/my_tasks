def f4(num):
    num = str(bin(num))[2:]
    num += num[-1]
    for _ in range(2):
        if num.count('1') % 2 == 0:
            num = num + '0'
        elif num.count('1') % 2 != 0:
            num = num + '1'
    return int(num, 2)


def main4():
    for i in range(1, 1000):
        print(i, f4(i))


if __name__ == '__main__':
    main4()