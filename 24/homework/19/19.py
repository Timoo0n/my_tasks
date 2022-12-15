def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        for i in set(my_str):
            if i in ('A', 'O'): my_str = my_str.replace(i, '1')
            else: my_str = my_str.replace(i, '0')
        count = 1
        while (count+1)*'01' in my_str: count += 1
        print(count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        for i in set(my_str):
            if i in ('A', 'O'): my_str = my_str.replace(i, '1')
            else: my_str = my_str.replace(i, '0')
    
        my_str = my_str.replace('01', '*').replace('0', ' ').replace('1', ' ')
        print(max(len(i) for i in my_str.split()))


def f2():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = list()
        for j in range(1, 3):
            for i in range(j, len(my_str)-1, 2):
                if my_str[i] in ('B', 'C', 'D') and my_str[i+1] in ('A', 'O'): count += 1
                else: max_count = max(count, max_count); count = 0
            max_list += [max_count]
            count = max_count = 0
        print(max(max_list))        

        

if __name__ == '__main__': f1(); f(); f2()
