def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        ms = float('-inf')

        for i in range(info):
            s = 0
            k = 0
            k7 = 0
            for j in range(i, info):
                if l[j] > 0 and l[j] % 7 == 0: k7 += 1
                s += l[j]
                k += 1
                if k >= 7 and k7 % 7 == 0:
                    ms = max(ms, s)
        print(ms)

def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        k7 = 0
        s = 0
        ms = float('-inf')
        q = []

        for _ in range(6):
            num = int(file.readline())
            s += num
            if num > 0 and num % 7 == 0: k7 += 1
            q.append([s, k7])

        l = [float('inf')]*7

        for _ in range(info-6):
            num = int(file.readline())

            s += num
            if num > 0 and num % 7 == 0: k7 += 1
            if k7 % 7 == 0: ms = max(ms, s)

            s1 = s - l[k7 % 7]
            ms = max(s1, ms)

            s1, k7_1 = q.pop(0)
            l[k7_1 % 7] = min(s1, l[k7_1 % 7])
            q.append([s, k7])
            
        print(ms)

taskA(); taskB()
            
            
            
        
