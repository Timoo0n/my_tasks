def dividers(num):
    my_set = set()
    for i in range(2, int(num**2)+1):
        if num % i == 0:
            my_set |= {i, num // i}
    return sorted(my_set)


def main():
    my_list = []
    num = 1
    max_num = 973146286
    while num <= max_num:
        my_list.append(num)
        num += 2000

    for i in range(159264873, max_num):
        result = dividers(i)
        if i in my_list:
            if len(result) % 2 == 1:
                print(i, len(result))


if __name__ == '__main__':
    print(dividers(1000))