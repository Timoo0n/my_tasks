"""Поразрядная конъюкция-это конъюкция для всех чисел кроме 0, 1"""


def f(x, a):
    return (x & 56 != 0) <= ((x & 48 == 0) <= (x & a != 0))


if __name__ == '__main__':
    for a in range(1, 1000):
        if all(f(x, a) == 1 for x in range(1, 10000)):
            print(a)