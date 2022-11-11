def f8(num):
    str_num = str(bin(num*2))[2:]
    str_num += str(str_num.count('1') % 2) + str(str_num.count('1') % 2)
    return int(str_num, 2)


def main8():
    my_list = []
    for i in range(1, 1000):
        my_list.append(f8(i))
        print(i, f8(i))
    my_list = list(filter(lambda el: el > 1017, my_list))
    print(min(my_list))


if __name__ == '__main__':
    main8()