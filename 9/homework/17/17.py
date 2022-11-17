def read_csv():
    with open('17.csv', 'r', encoding='utf-8') as csvfile:
        return [list(map(lambda el: int(el), i.strip().split(';'))) for i in csvfile.readlines()]


def main():
    my_list, count = read_csv(), 0

    for my_list1 in my_list:
        x0, y0, x, y = my_list1
        if all(i > 0 for i in my_list1) or all(i < 0 for i in my_list1):
            count += 1
        elif x0 < 0 < y and x < 0 < y0:
            count += 1
        elif x0 > 0 > y and x > 0 > y0:
            count += 1
    print(count)


if __name__ == '__main__':
    main()