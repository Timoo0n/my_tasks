def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 1
        for i in range(1, len(my_str)):
            if my_str[i-1] != my_str[i]: count += 1
            else: max_count = max(count, max_count); count = 1
        print(max_count)

def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        while all(i in my_str for i in ('XX', 'YY', 'ZZ')):
            for j in ('XX', 'YY', 'ZZ'): my_str = my_str.replace(j, f'{j[0]} {j[1]}')
        print(len(max(my_str.split(), key=len)))


if __name__ == '__main__': f1(); f()
