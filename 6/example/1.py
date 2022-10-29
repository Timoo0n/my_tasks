from math import tan, radians


def f():
    count = 0
    for x in range(1, 11):
        for y in range(11):
            if (y > 0) and (y > (x*tan(radians(30)))) and (y < (-1 * tan(radians(30))*x + 10)):
                count += 1
    print(count)


def main():
    f()


if __name__ == '__main__':
    main()