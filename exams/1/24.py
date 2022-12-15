def f2():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        while 'DD' in my_str:
            my_str = my_str.replace('DD', 'D D')
        my_list = my_str.split()
        max_value = max(len(i) for i in my_list if 'FE' in i)
        print(max_value)


if __name__ == '__main__': f2()
