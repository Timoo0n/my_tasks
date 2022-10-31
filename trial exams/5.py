def f(num):
    num = str(bin(num))[2:]
    num += num[-1]
    if len(num) % 2 == 0:
        num += '0'
    else:
        num += '1'
    num += '1'
    return int(num, 2)


def main():
    for i in range(1, 100):
        result = f(i)
        if result > 105:
            print(result)
            break


if __name__ == '__main__':
    main()