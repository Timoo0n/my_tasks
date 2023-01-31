from itertools import combinations


def taskA():  # 144001
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 10
        #l = [30, 6, 23, 13, 39, 21, 85, 3, 17, 59]
            
        max_value = 0
        
        for i in range(info):
            for j in range(i+1, info):
                for k in range(j+1, info):
                    for h in range(k+1, info):
                        if l[i]*l[j]*l[k]*l[h] % 12 == 0 and (l[i]+l[j]+l[k]+l[h]) > max_value:
                            max_value = l[i]+l[j]+l[k]+l[h]
        print(max_value)


def taskB():  # 267927
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [[] for _ in range(12)]

        for _ in range(info):
            n = int(file.readline())
            l[n % 12] += [n]

        d = []
        for i in range(len(l)):
            l[i].sort(reverse=1)
            d += l[i][:4]

        max_value = 0
        for x, y, z, w in combinations(d, 4):
            if x*y*z*w % 12 == 0 and max_value < x+y+z+w:
                max_value = x+y+z+w
        print(max_value)

        
            

if __name__ == '__main__': taskA(); taskB()
