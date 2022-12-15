def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        for i in set(my_str):
            if i.isalpha(): my_str = my_str.replace(i, ' ')
        print(len(max(my_str.split(), key=len)))


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        for i in my_str:
            if i.isdigit():
                count += 1
                continue
            max_count = max(count, max_count)
            count = 0
        print(max_count)
        
        

if __name__ == '__main__': f1()
