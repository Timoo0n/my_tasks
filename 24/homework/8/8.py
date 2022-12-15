def f():
    with open('24.txt', 'r') as file:
        count = max_count = 1
        my_str = file.read()
        for i in range(1, len(my_str)):
            if my_str[i-1] + my_str[i] != 'PP': count += 1
            else: max_count = max(count, max_count); count = 1
        print(max_count)

def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        while 'PP' in my_str: my_str = my_str.replace('PP', 'P P')
        print(len(max(my_str.split(), key=len)))


if __name__ == '__main__': f1()
