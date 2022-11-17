def read_csv():
    with open('18.csv') as csvfile:
        return [list(map(lambda el: int(el), i.strip().split(';'))) for i in csvfile]


def main():
    my_list, count = read_csv(), 0
    for i in my_list:
        x0, y0, x, y = i
        if x*x0 > 0 >= y*y0:
            count += 1
        elif x*x0 <= 0 < y*y0:
            count += 1

    print(count)


def main1():
    my_list, count1 = read_csv(), 0
    for i in my_list:
        x0, y0, x, y = i
        if (x0 == 0 or y0 == 0) and (x == 0 or x0 == 0):
            count1 += 1
    print(count1)


if __name__ == '__main__':
    main1()