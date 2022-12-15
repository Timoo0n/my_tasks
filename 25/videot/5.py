from functools import reduce


def div(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}

    return sorted(my_set)

    
def main():
    for i in range(300_000_001, 300_015_000):
        res = div(i)
        if len(res) >= 5:
            value = reduce(lambda x, y: x*y, res[:5], 1)
            if str(value)[-2:] == '31' and value <= i:
                print(value, max(res[:5]))


if __name__ == '__main__':
    main()
