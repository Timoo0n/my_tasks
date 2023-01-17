
def f():
    with open('24.txt') as file:
        s = file.read()
        my_dict ={i: s.count(i) for i in set(s) if i}
         
        print(my_dict)


def f1():
    for n in range(1, 10000000):
        value = 2 + 4*(n-1)
        if value == 1251300: print(n)
        if value > 1251300: print('NO'); break

f()
f1()
