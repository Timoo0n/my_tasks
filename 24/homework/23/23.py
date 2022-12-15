def f():  # хурь
    with open('24.txt') as file:
        my_str = file.read()
        for i in ('A', 'C'):
            for j in set(my_str):
                my_str = my_str.replace(f'{i}{j}{i}', '*')
        my_str = my_str.replace('A', ' ').replace('B', ' ').replace('C', ' ')
        print(max(len(i) for i in my_str.split()))


def f1():  # хурь
    with open('24.txt', 'r') as file:
        my_str = file.read()
        for i in ('A', 'C'):
            for j in set(my_str):
                my_str = my_str.replace(f'{i}{j}{i}', '*')
        count = 1
        while (count+1)*'*' in my_str: count += 1
        print(count)


def f2():  # правильно
    with open('24.txt') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = []

        for j in range(3):
            for i in range(j, len(my_str)-2, 3):
                if my_str[i] == 'A' and my_str[i+2] == 'A' or my_str[i] == 'C' and my_str[i+2] == 'C': count += 1
                else: max_count = max(count, max_count); count = 0
            max_list += [max_count]
            count = max_count = 0
        print(max_count)
    

if __name__ == '__main__': f2()
