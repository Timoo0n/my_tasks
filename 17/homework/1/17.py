def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(filter(lambda el: el % 3 == 0 and all(el % i != 0 for i in (7, 17, 19, 27)), list(map(lambda el: int(el), file.read().split()))))
        return len(my_list), max(my_list)


def main():
    print(f())


if __name__ == '__main__':
    main()