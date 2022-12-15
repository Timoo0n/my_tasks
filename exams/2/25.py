from itertools import product


def f():
    for i in range(100):
        num = int(f'123{i}890')
        if num % 27 == 0 and num <= 10**8:
            print(num, num // 27)


if __name__ == '__main__': f()
