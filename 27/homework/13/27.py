from itertools import combinations


def taskA():  # 17424
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 10
        #l = [30, 83, 17, 54, 71, 23, 15, 83, 19, 58]

        min_value = 10**20
        
        for x, y, z in combinations(l, 3):
            if (x+y+z) % 11 == 0 and (x+y+z) < min_value:
                min_value = x + y + z
        print(min_value)


def taskB():  # 88
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        
        l = [[] for _ in range(11)]
        for i in range(info):
            n = int(file.readline())
            l[n % 11] += [n]

        min_l = []
        for i in range(len(l)):
            l[i].sort()
            min_l += l[i][:3]

        min_value = 10**20
        for i in range(len(min_l)):
            for j in range(i+1, len(min_l)):
                for k in range(j+1, len(min_l)):
                    if (min_l[i] + min_l[j] + min_l[k]) < min_value and (min_l[i] + min_l[j] + min_l[k]) % 11 == 0:
                        min_value = min_l[i] + min_l[j] + min_l[k]
        print(min_value)

if __name__ == '__main__': taskA(); taskB()
