def f():
    num = 6**203+5*6**405-3*6**144+76
    my_list = []
    while num > 0:
        my_list = [num % 6] + my_list

        num //= 6

    return my_list


if __name__ == '__main__':
    result = f()
    print(abs(result.count(5)-result.count(0)))