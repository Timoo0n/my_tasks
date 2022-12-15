def f():
    with open('24.txt', 'r') as file:
        my_str = file.read()
        while 'DD' in my_str:
            my_str = my_str.replace('DD', 'D D')

        print(min(len(i) for i in my_str.split() if len(i) > 2 and i[0] == 'D' and i[-1] == 'D'))
        

def f1():
    with open('24.txt', 'r') as file:
        print(len(min(list(filter(lambda el: len(el) > 2, file.read().split('D')[1:-1])), key=len))+2)


if __name__ == '__main__': f(); f1()
