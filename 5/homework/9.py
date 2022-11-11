def f9(num):
    str_num = str(bin(num))[2:]
    if num % 2 == 0:
        str_num = '1' + str_num + '0'
    elif num % 2 != 0:
        str_num = '11' + str_num + '11'
    return int(str_num, 2)


def main9():
    my_list = []
    for i in range(1, 1000):
        my_list.append(f9(i))
        print(i, f9(i))
    print(min(list(filter(lambda el: el > 52, my_list))))


if __name__ == '__main__':
    main9()