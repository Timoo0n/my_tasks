def f():
    num = 17**5+85**8-10
    my_list = []
    while num > 0:
        my_list = [num % 17] + my_list
        num //= 17

    return my_list.count(16)


if __name__ == '__main__':
    print(f())