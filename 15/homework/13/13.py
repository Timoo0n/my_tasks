def f(x, y, a):
    return ((x**2-10*x+16) > 0) or ((y**2-10*y+21) > 0) or (x*y < 2*a)


def main():
    for a in range(1000):
        if all(f(x, y, a) for x in range(100) for y in range(100)):
            print(a)


if __name__ == '__main__':
    main()