from itertools import product


def f():
    return len(list(filter(lambda el: 'X' in el[:2], [''.join(i) for i in product('ABCX', repeat=5) if i[-1] == 'X'])))


def main():
    print(f())


if __name__ == '__main__':
    main()