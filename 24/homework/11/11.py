def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 1
        for i in range(1, len(my_str)):
            if ord(my_str[i-1]) <= ord(my_str[i]): count += 1
            else: max_count = max(count, max_count); count = 1
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 1
        for i in range(1, len(my_str)):
            new_str = my_str[i-1] + my_str[i]
            if new_str == ''.join(sorted(new_str)): count += 1
            else: max_count = max(count, max_count); count = 1
        print(max_count)


def f2():
    with open('24.txt', 'r', encoding='utf-8') as file:
        my_str = file.read()
        my_tuple = ('YX', 'ZX', 'ZY')

        while all(i in my_str for i in my_tuple):
            for i in my_tuple: my_str = my_str.replace(i, f'{i[0]} {i[1]}')
        print(len(max(my_str.split(), key=len)))
            

if __name__ == '__main__': f(); f1(); f2()
