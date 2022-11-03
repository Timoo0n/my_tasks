
def f():
    num = 7**103+20*7**204-3*7**57+97
    my_list = list()
    while num > 0:
        my_list.append(num % 7)
        num //= 7
    return my_list.count(6)


if __name__ == '__main__':
    print(f())