def f(x, y, a):
    return (x > 39) or (y > 26) or (2*x + 4*y < a)


def main():
    for a in range(1000):
        if all(f(x, y, a) for x in range(100) for y in range(100)):
            print(a)


if __name__ == '__main__':
    main()