def f():
    for i in range(1, 100):
        if 56 % i == 1 and 45 % i == 1:
            return i


if __name__ == '__main__':
    print(f())