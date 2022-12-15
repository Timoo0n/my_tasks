from itertools import product
from string import digits


def f():
    with open('24.txt', 'r') as file:
        my_str = file.read().strip()
        count = max_count = 1
        for i in range(1, len(my_str)):
            if ord(my_str[i-1]) < ord(my_str[i]): count += 1
            else: max_count = max(count, max_count); count = 1
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().strip()
        my_list = [''.join(i) for i in product(digits, repeat=2) if int(i[0]) >= int(i[1])]
        while all(i in my_str for i in my_list):
            for i in my_list:
                my_str = my_str.replace(i, f'{i[0]} {i[1]}')
        print(len(max(my_str.split(), key=len)))


if __name__ == '__main__': f1(); f()
