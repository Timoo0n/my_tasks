def f():
    num = 7**2+49**4-21
    my_list = []
    while num > 0:
        my_list = [num % 14] + my_list

        num //= 14

    return my_list


if __name__ == '__main__':
    result = f()
    print(result.count(10) + result.count(0)) 