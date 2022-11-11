def f3(num):
    num = str(bin(num))[2:]
    num += num[-1]
    for _ in range(2):
        if num.count('1') % 2 == 0:
            num = num + '0'
        elif num.count('1') % 2 != 0:
            num = num + '1'
    return int(num, 2)


def main3():
    for i in range(1, 1000):
        if f3(i) > 130:
            print(i)


if __name__ == '__main__':
    main3()