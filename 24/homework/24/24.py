def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = 1
        while (count+1)* 'CA' in my_str: count += 1

        print(27*'CA'+'C' in my_str)


if __name__ == '__main__': f()
