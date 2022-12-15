def f():
    with open('24.txt') as file:
        my_str = file.read()
        for i in set(my_str):
            if i.isdigit(): my_str = my_str.replace(i, '!')
            else: my_str = my_str.replace(i, '@')
        my_str = my_str.replace('@!', '*').replace('@', ' ').replace('!', ' ')
        print(max(len(i) for i in my_str.split()))


def f1():
    with open('24.txt') as file:
        my_str = file.read()
        for i in set(my_str):
            if i.isdigit(): my_str = my_str.replace(i, '!')
            else: my_str = my_str.replace(i, '@')
        count = 1
        while (count+1)*'@!' in my_str: count += 1
        print(count)


def f2():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = []
        for j in range(3):
            for i in range(j, len(my_str)-1, 2):
                if my_str[i].isalpha() and my_str[i+1].isdigit(): count += 1
                else: max_count = max(max_count, count); count = 0
            max_list += [max_count]
            count = max_count = 0
        print(max(max_list))
            

if __name__ == '__main__': f(); f1(); f2()
