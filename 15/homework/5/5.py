def f(x, a):
    return (a % 7 == 0) and ((240 % x == 0) <= ((a % x != 0) <= (780 % x != 0)))


def main():
    for a in range(500):
        if all(f(x, a) for x in range(1, 5000)):
            print(a)


if __name__ == '__main__':
    main()