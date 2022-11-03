def f():
    for x in range(1, 1000):
        num = 64**12-8**14+x
        my_list = []
        while num > 0:
            my_list = [num % 8] + my_list

            num //= 8

        if my_list.count(7) == 12 and my_list.count(1) == 1:
            return x


def f1():
    for x in range(1, 1000):
        result = oct(64**12-8**14+x)[2::]
        if result.count('7') == 12 and result.count('1') == 1:
            return x


if __name__ == '__main__':
    print(f1())