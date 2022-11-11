def f6(num):
    return int((str(bin(num))[2:])[::-1], 2)


def main6():
    for i in range(1, 1000):
        result = f6(i)
        if result == 13:
            print(i, result)


if __name__ == '__main__':
    main6()