
def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        count = max_count = 0
        my_str = file.read()
        for i in my_str:
            if i == 'C':
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        print(max_count)


def f1():
    with open('24.txt', 'r', encoding='utf-8') as file:
        my_str = file.read().strip().replace('A', ' ').replace('B', ' ').split()
        print(len(max(my_str, key=len)))


if __name__ == '__main__':
    f1()