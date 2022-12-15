def f():
    with open('24.txt') as file:
        my_str = file.read()
        count = max_count = 1
        for i in range(len(my_str)-1):
            if my_str[i] + my_str[i+1] not in ('XY', 'XZ'): count += 1
            else: max_count = max(count, max_count); count = 1
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('XY', 'X Y').replace('XZ', 'X Z').split()
        print(len(max(my_str, key=len)))


if __name__ == '__main__': f()
