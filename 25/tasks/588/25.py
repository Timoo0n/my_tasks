def dividers(num):
    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def main():
    max_value, value = 973146286, 0
    for i in range(159264873, max_value):
        result = dividers(i)
        if len(result) % 2 == 1:
            value = i
            break

    while value <= max_value:
        result = dividers(value)
        if len(result) % 2 == 1 and len(result) > 1:
            print(value, len(result))
        value += 2000


if __name__ == '__main__':
    main()