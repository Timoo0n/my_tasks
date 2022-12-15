def div(x):
    my_set = set()
    for i in range(2, int(x**0.5)+1):
        if x % i == 0: my_set |= {i, x // i}
    return sorted(my_set)


def main():
    num = 150_001
    count = 0

    while count != 100:
        r = div(num)
        if len(r) != 0 and sum(r) % 13 == 10:
            print(num, sum(r)); count += 1
        num += 1


if __name__ == '__main__': main()
