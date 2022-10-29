def notation_5(num):
    my_str = ''

    while num != 0:
        my_str += str(num % 5)

        num //= 5

    return int(my_str[::-1])


def notation_9(num):
    my_str = ''

    while num != 0:
        my_str += str(num % 9)

        num //= 9

    return int(my_str[::-1])


def notation_8(num):
    my_str = ''

    while num != 0:
        my_str += str(num % 8)

        num //= 8

    return int(my_str[::-1])


def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))

        count = 0
        new_list = list()
        for num in my_list:
            #if str(notation_5(num))[-1] == '3' and str(notation_9(num))[-1] == '5' and str(notation_8(num))[-1] != '7':
            if num % 5 == 3 and num % 9 == 5 and num % 8 != 7:
                count += 1
                new_list.append(num)
        print(count, max(new_list))


if __name__ == '__main__':
    f()