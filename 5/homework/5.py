def f5(n):
    num, my_list = n, []
    while num > 0:
        my_list = [str(num % 3)] + my_list
        num //= 3
    return int(''.join(my_list) + str(n % 3), 3)


def main5():
    for i in range(1, 1000):
        print(f5(i))


if __name__ == '__main__':
    main5()