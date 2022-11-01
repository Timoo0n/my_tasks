def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        return file.read().replace('TIK', '0').replace('TOK', '0').count('0')


def main():
    print(f())


if __name__ == '__main__':
    main()