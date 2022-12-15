def f():  # хурь
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = d_count = 0
        for i in my_str:
            if i == 'D' and d_count == 2: max_count = max(count, max_count); count = 0; d_count = 0
            elif i == 'D' and d_count != 2: d_count += 1; count += 1
            else: count += 1
        
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().split('D')
        max_count = 1
        for i in range(2, len(my_str)):
            max_count = max(max_count, len(my_str[i-2])+len(my_str[i-1])+len(my_str[i])+2)
        print(max_count)


def f_1():  # хурь
    with open('24.txt', 'r') as file:
        my_str = file.read()
        symbol = max_symbol = ''
        d_count = 0
        for i in my_str:
            if i == 'D' and d_count == 2: max_symbol = max(symbol, max_symbol, key=len); d_count = 0; symbol = ''
            elif i == 'D': d_count += 1; symbol += i
            else: symbol += i
        
        print(len(max_symbol))


def f1_1(): 
    with open('24.txt', 'r') as file:
        my_str = file.read().split('D')
        my_list = list()
        for i in range(2, len(my_str)):
             my_list += [my_str[i-2] + 'D' + my_str[i-1] + 'D' + my_str[i]]
        print(len(max(my_list, key=len)))


if __name__ == '__main__': f2()
