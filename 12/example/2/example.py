def f(my_str):

    while '25' in my_str or '355' in my_str or '4555' in my_str:
        if '25' in my_str:
            my_str = my_str.replace('25', '4', 1)
        elif '355' in my_str:
            my_str = my_str.replace('355', '2', 1)
        elif '4555' in my_str:
            my_str = my_str.replace('4555', '3', 1)

    return my_str


if __name__ == '__main__':
    print(f('3' + '5' * 100 + '3'))