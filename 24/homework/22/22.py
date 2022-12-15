def f():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('B', 'A').replace('2', '1')
        count = 1
        while (count + 1)*'11A' in my_str: count += 1
        print(count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        my_str = my_str.replace('B', 'A').replace('2', '1').replace('11A', '*').replace('1', ' ').replace('A', ' ')
        print(max(len(i) for i in my_str.split()))


def f2():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = list()
        for j in range(4):
            for i in range(j, len(my_str), 3):
                if my_str[i-2].isdigit() and my_str[i-1].isdigit() and my_str[i].isalpha(): count += 1
                else: max_count = max(count, max_count); count = 0
            max_list.append(max_count)
            count = max_count = 0
        print(max(max_list))
            

if __name__ == '__main__': f1(); f(); f2()
