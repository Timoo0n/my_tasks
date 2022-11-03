def f():
    for x in '123456789abcdefghijkl':
        for y in '0123456789abc':
            num = int(f'{x}23{x}5', 22) - int(f'67{y}9{y}', 13)
            if num % 57 == 0:
                print(int(x, 22) + int(y, 13), num // 57)


def f1():
    for x in range(1, 22):
        for y in range(13):
            num = x*22**4 + 2*22**3 + 3*22**2 + 22*x + 5 - 6*13**4 - 7*13**3 - y*13**2 - 9*13 - y
            if num % 57 == 0:
                print(x+y, num // 57)


if __name__ == '__main__':
    f()