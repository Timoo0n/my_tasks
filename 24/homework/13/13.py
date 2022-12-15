from itertools import product


def f():
    with open('24.txt', 'r') as file:
        my_str = file.read().strip()
        s = max_str = my_str[0]
        for i in range(1, len(my_str)):
            if ord(my_str[i-1]) > ord(my_str[i]): s += my_str[i]; max_str = max(max_str, s, key=len)
            else: s = my_str[i]

        print(max_str)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().strip()
        my_list = [''.join(i) for i in product(set(my_str), repeat=2) if i[0] <= i[1]]

        while any(i in my_str for i in my_list):
            for i in my_list:
                my_str = my_str.replace(i, f'{i[0]} {i[1]}')
        print(max(my_str.split(), key=len))


if __name__ == '__main__': f(); f1()
