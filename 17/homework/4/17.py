def f():
    with open('../5/17.txt', 'r', encoding='utf-8') as file:
        my_list = list(filter(lambda el: el % 13 == 7 and all(el % i != 0 for i in (7, 11)), list(map(lambda el: int(el), file.read().split()))))
        return max(my_list)-min(my_list), len(my_list)


def main():
    print(f())


if __name__ == '__main__':
    main()