def f():
    with open('24.txt', 'r') as file:
        my_str = file.read().replace('PNO', '*').replace('NPO', '*').replace('P', ' ').replace('N', ' ').replace('O', ' ')
        print(max(len(i) for i in my_str.split()))


def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = []
        for j in range(4):
            for i in range(j, len(my_str)-2, 3):
                if my_str[i]+my_str[i+1]+my_str[i+2] in ('NPO', 'PNO'): count += 1
                else: max_count = max(count, max_count); count = 0
            max_list += [max_count]
            count = max_count = 0
        print(max(max_list))
 

if __name__ == '__main__': f(); f1()
