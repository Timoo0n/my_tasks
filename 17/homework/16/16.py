def f():
    with open('17.txt') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        list_11 = list(filter(lambda el: el % 11 == 0, my_list))
        list_17 = list(filter(lambda el: el % 17 == 0, my_list))
        if len(list_11) > len(list_17):
            return len(list_11), min(list_11)

        return len(list_17), max(list_17)


if __name__ == '__main__':
    print(*f())