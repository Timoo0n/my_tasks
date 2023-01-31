from itertools import combinations

def taskA():  # 85440
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 8
        #l = [95, 163, 5, 40, 15, 3, 85, 80]

        
        max_value = 0
        for x, y in combinations(l, 2):
            if abs(x-y) % 80 == 0 and abs(x-y) > max_value:
                max_value = abs(x-y)
        print(max_value)


def taskB():  # 99920
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        d = [[] for _ in range(80)]
        for _ in range(info):
            n = int(file.readline())
            d[n % 80] += [n]

        l = []
        for i in range(len(d)):
            d[i].sort()
            if len(d[i]) >= 2: l += [d[i][0], d[i][-1]]

        max_value = 0
        for i in range(len(l)):
            for j in range(len(l)):
                if abs(l[i]-l[j]) % 80 == 0 and abs(l[i]-l[j]) > max_value:
                    max_value = abs(l[i]-l[j])
        print(max_value)


if __name__ == '__main__': taskA(); taskB()

        
