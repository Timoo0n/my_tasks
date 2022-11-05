def f():
    for i in range(10, 100):
        if i % 16 == 10 and i % 5 == 3:
            return i


if __name__ == '__main__':
    print(f())