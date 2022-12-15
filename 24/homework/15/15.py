def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        for i in set(my_str) - {'D'}:
            my_str = my_str.replace(i, ' ')
        print(len(min(my_str.split(), key=len)))


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        s, my_list = '', []
        for i in my_str:
            if i == 'D':
                s += i
            elif s:
                my_list += [s]
                s = ''
        print(len(min(my_list, key=len)))
        


if __name__ == '__main__': f(); f1()
