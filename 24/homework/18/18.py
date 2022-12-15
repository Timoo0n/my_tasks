def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = 0
        while 'КОТ' * count in my_str:
            count +=1
        print(count-1)

def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('КОТ', '*')
        for i in set(my_str) - {'*'}:
            my_str = my_str.replace(i, ' ')
        print(max(len(i) for i in my_str.split()))
    

def f2():
    with open('24.txt') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = []
        for j in range(1, 10):
            for i in range(j, len(my_str)-2, 3):
                if my_str[i]+my_str[i+1]+my_str[i+2] == 'КОТ': count += 1
                else: max_count = max(count, max_count); count = 0
            max_list.append(max_count)
            count = max_count = 0
        print(max(max_list))
        

if __name__ == '__main__': f2(); f1(); f()
