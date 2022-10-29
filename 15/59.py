def f(x, a):
    return ((x % a == 0) and (x % 24 == 0) and (x % 16 != 0)) <= (x % a != 0)


if __name__ == '__main__':
    for a in range(1, 300):
        if all(f(x, a) for x in range(1, 3000)):
            print(a)