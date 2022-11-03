def f():
    for i in range(1, 100):
        num = 81**20 - 9**i + 50
        my_list = []
        while num > 0:
            my_list = [num % 9] + my_list

            num //= 9

        if sum(my_list) == 138:
            return i


if __name__ == '__main__':
    print(f())