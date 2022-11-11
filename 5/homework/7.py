def f7(num):
    str_num = str(bin(num))[2:]
    str_num += str((str_num.count('1') % 2)) + str((str_num.count('1') % 2))

    return int(str_num, 2)


def main7():
    count = 0
    for i in range(1, 1000):
        result = f7(i)
        if result < 80:
            count += 1
        print(i, f7(i))
    print(count)


if __name__ == '__main__':
    main7()