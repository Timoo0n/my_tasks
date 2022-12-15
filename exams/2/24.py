def f():
    with open('24.txt') as file:
        my_str = file.read().replace('2', '1').replace('B', 'A')
        count = 1
        while (count+1)*'11A' in my_str: count += 1
        print(count)

def f1():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        count = max_count = 0
        max_list = []
        for j in range(4):
            for i in range(j, len(my_str)-2, 3):
                if my_str[i].isdigit() and my_str[i+1].isdigit() and my_str[i+2].isalpha():
                    count += 1
                else:
                    max_count = max(count, max_count)
                    count = 0
            max_list += [max_count]
            max_count = count = 0
            
        print(max(max_list))
        


def main(): f(); f1()


if __name__ == '__main__': main()
