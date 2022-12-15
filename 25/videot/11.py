from functools import reduce


def div(x):
    my_set = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            my_set |= {i, x // i}
    return sorted(my_set)


def p(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x**0.5)+1))


def main():
    count = 0
    for i in range(158928, 345293+1):
        my_list = list(filter(lambda el: p(el), div(i)))
        if len(my_list) == 3:
            value = reduce(lambda x, y: x*y, my_list, 1)
            if value == i:
                num_list += [i]
    print(len(num_list), min(num_list))


if __name__ == '__main__':
    main()
        
        
