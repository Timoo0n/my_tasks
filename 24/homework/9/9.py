def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 3
        for i in range(3, len(my_str)):
            if my_str[i-3]+my_str[i-2]+my_str[i-1]+my_str[i] != 'XZZY':
                count += 1
            else:
                max_count = max(count, max_count)
                count = 3
        print(max_count)


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('XZZY', 'XZZ ZZY')
        print(len(max(my_str.split(), key=len)))
        
    


if __name__ == '__main__': f()
