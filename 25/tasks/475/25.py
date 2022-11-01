def dividers(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def main():
    for i in range(224466, 664422+1):
        result = dividers(i)
        my_tuple = (5, 7, 13)
        if all(j in result for j in my_tuple) and all(j**2 not in result for j in my_tuple) and (max(result) <= 100_000) and str(max(result))[-2:] == '19':
            print(i, max(result))


if __name__ == '__main__':
    main()