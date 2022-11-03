def f():
    num = 7**103+6*7**104-3*7**57+98
    my_list = []
    while num > 0:
        my_list.append(num % 7)
        num //= 7

    return sum(my_list)


if __name__ == '__main__':
    print(f())