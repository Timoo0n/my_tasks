def f10(num):
    str_num = str(bin(num))[2:]
    if str_num.count('1') % 2 == 0:
        str_num = '10' + str_num[2:] + '0'
    elif str_num.count('1') % 2 != 0:
        str_num = '11' + str_num[2:] + '1'

    return int(str_num, 2)


def main10():
    for i in range(1, 1000):
        if f10(i) < 35:
            print(i)


if __name__ == '__main__':
    main10()