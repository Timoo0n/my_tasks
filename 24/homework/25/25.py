def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = 1
        while (count+1)* 'DBAC' in my_str: count += 1
        print(23*'DBAC'+'DBA' in my_str)


if __name__ == '__main__': f()
