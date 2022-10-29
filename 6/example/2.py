from math import tan, radians


def f():
    count = 0
    for x in range(-20, 20):
        for y in range(-20, 20):
            if (y > -0.1*x-3.5) and (y < 6-2*x) and (y < (7/6)*x+(17/6)):
                count += 1

    print(count)


def main():
    f()


if __name__ == '__main__':
    main()