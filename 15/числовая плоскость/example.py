def f(x, y, a):
    return (x < a) and (y < a) and (x * y > 1200)


if __name__ == '__main__':
    for a in range(1, 1000):
        if all(f(x, y, a) == 0 for x in range(1, 100) for y in range(1, 100)):
            print(a)