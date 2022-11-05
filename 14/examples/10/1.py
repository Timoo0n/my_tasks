def f():
    for x in range(1, 20):
        try:
            if int('123', x) == int('93', x+2):
                return x
        except ValueError:
            continue


if __name__ == '__main__':
    print(f())