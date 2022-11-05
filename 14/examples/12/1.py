def f():
    for i in range(2, 51):
        my_list = []
        num = i
        while num > 0:
            my_list = [num % 2] + my_list

            num //= 2

        if ''.join(list(map(lambda el: str(el), my_list)))[-3:] == '011':
            print(i)


if __name__ == '__main__':
    f()