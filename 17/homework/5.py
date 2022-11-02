def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(filter(lambda el: (el % 16 == 11 or hex(el)[-1] == 'b') and el % 7 == 0 and all(el % i != 0  for i in (6, 13, 19)), list(map(lambda el: int(el), file.read().split()))))
        return sum(my_list), len(my_list)


def main():
    print(f())


if __name__ == '__main__':
    main()