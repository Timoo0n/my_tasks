def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        min_s = float('inf')
        
        for i in range(info):
            k = 0
            s = 0
            for j in range(i, info):
                s += l[j]
                if l[j] % 3 == 0: k += 1
                if k == 10: min_s = min(s, min_s)
        print(min_s)


def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        l = [-10**20]*info

        ms = 10**20
        k = 0
        s = 0
        
        for _ in range(info):
            num = int(file.readline())
            s += num

            if num % 3 == 0: k += 1
            if k == 10: ms = min(s, ms)

            s1 = s - l[k - 10]

            ms = min(ms, s1)

            l[k] = max(l[k], s)
        print(ms)


taskA(); taskB()
            
            
            

            
