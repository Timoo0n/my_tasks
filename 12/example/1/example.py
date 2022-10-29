def f(my_str: str):
    while '222' in my_str or '888' in my_str:
        my_str = my_str.replace('222', '8', 1) if '222' in my_str else my_str.replace('888', '2', 1)

    return my_str


if __name__ == '__main__':
    print(f('8' * 72))