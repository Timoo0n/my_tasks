def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(filter(lambda el: any(el % 10 == i for i in (2, 7)) and all(el % i == 0 for i in (3, 11)), list(map(lambda el: int(el), file.read().split()))))
        return len(my_list), min(my_list)


def main():
    print(f())


if __name__ == '__main__':
    main()