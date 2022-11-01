def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        return file.read().replace('STOCK', ' ').count('OCK')


def main():
    print(f())


if __name__ == '__main__':
    main()