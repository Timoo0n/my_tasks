def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = a_count = 0
        for i in my_str:
            if a_count == 2: max_count = max(count, max_count); count = 0; a_count = 0
            elif i == 'A': a_count += 1; count += 1
            else: count += 1
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_list = file.read().split('A')
        max_count = 0
        for i in range(len(my_list)-1):
            max_count = max(max_count, len(my_list[i])+len(my_list[i+1])+1)
        print(max_count)



if __name__ == '__main__': f1(); f()
