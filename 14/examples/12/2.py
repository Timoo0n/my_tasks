def f():
    for i in range(2, 51):
        if i % 3 == 1 and i // 3 % 3 == 2:
            print(i)


if __name__ == '__main__':
    f()