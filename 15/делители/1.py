def f(x, a):
    return (x % a != 0) or (x % 36 == 0) or (x % 12 != 0)


if __name__ == '__main__':
    for a in range(1, 101):
        if all(f(x, a) == 1 for x in range(1, 1001)):
            print(a)