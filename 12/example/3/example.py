def f(my_str):

    while '111' in my_str:
        my_str = my_str.replace('111', '2', 1).replace('222', '1', 1)

    return my_str


if __name__ == '__main__':
    for i in range(51, 101):
        result = f(i*'1')
        if result == '22':
            print(i, result)