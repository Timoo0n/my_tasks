def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        ms = float('inf')
        count = float('inf')
        
        for i in range(info):
            s = 0
            k = 0
            for j in range(i, info):
                s += l[j]
                k += 1
                if (s < ms or (s == ms and k > count)) and s % 2077 == 0:
                    count = k
                    ms = s
        print(count, ms)

def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        l_s = [float('-inf')]*2077  # Суммы
        l_k = [0]*2077  # Количества

        s = 0
        
        mk = float('-inf')
        ms = float('inf')

        for i in range(info):
            num = int(file.readline())

            s += num
            if s % 2077 == 0 and (ms > s or (s == ms and mk < i+1)):
                mk = i+1
                ms = s

            s1 = s - l_s[s % 2077]
            k1 = i+1 - l_k[s % 2077]

            if s1 < ms or (s1 == ms and mk < k1):
                ms = s1
                mk = k1

            if s > l_s[s % 2077]:
                l_s[s % 2077] = s
                l_k[s % 2077] = i+1
        print(mk, ms)

taskB(); taskA()
                    
