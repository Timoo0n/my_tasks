def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        for i in range(len(my_str)):
            if my_str[i] not in ('C', 'F'):
                count += 1
                continue
            max_count = max(count, max_count)
            count = 0
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('C', ' ').replace('F', ' ').split()
        print(len(max(my_str, key=len)))
    

if __name__ == '__main__':
    f()
