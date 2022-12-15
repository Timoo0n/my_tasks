def f():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('C', ' ').replace('D', ' ').split()
        print(len(max(my_str, key=len)))


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        for i in my_str:
            if i not in ('C', 'D'):
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        print(max_count)
        


if __name__ == '__main__':
    f()
