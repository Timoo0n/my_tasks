from time import time


def f():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            q = []
            s = 0
            for i in range(50):
                num = int(file.readline())
                s += num
                q += [s]
            l = [float('-inf')]*777
            min_s = float('inf')
            
            for _ in range(n-50):
                num = int(file.readline())
                s += num
                if s % 777 == 0: min_s = min(min_s, s)
                min_s = min(min_s, s-l[s%777])

                s1 = q.pop(0)
                l[s1%777] = max(l[s1%777], s1)
                q += [s]
            print(min_s)


def f1():  # Частичные суммы, файл B работал 10 минут
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        start = time()
        l = []
        collection = []
        for _ in range(n):
            num = int(file.readline())
            l = [ [summ+num, length+1] for summ, length in l]\
                + [ [num, 1] ]
            l = {s[0]%777:s for s in sorted(l, reverse=True)}
            if 0 in l and l[0][1] > 50: collection += [l[0][0]]
            l = list(l.values())
        end = time()
        print(end-start)
        print(min(collection))
f1()
