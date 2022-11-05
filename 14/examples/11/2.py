def f():
    for n in range(1, 36):
        if 338 % n == 2 and n**2 <= 338 < n**3:
            print(n)


def f1():
    for n in range(2, 36):
        x = 338
        my_list = []
        while x > 0:
            my_list = [x % n] + my_list

            x //= n
        if my_list[-1] == 2 and len(my_list) == 3:
            print(n)


if __name__ == '__main__':
    f1()