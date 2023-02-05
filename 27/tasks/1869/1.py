def taskA():
    with open('27_A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        ml = 0
        ms = -10**20
        l = [int(i) for i in file.read().split()]

        for i in range(info):
            s = 0
            k = 0
            for j in range(i, info):
                k += 1
                s += l[j]
                if s % 89 == 0:
                    if s > ms or (s == ms and k < ml):
                        ms = s
                        ml = k
        print(ml)

def taskB():
    with open('27_B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        ml = 0
        ms = -10**20

        m = [10**20]* 89
        l = [0]* 89
        
        s = 0

        for i in range(info):
            num = int(file.readline())
            s += num

            if s % 89 == 0:
                if s > ms or (s == ms and (i+1) < ml):
                    ms, ml = s, i+1
                
            s1 = s - m[s % 89]
            l1 = i+1 - l[s % 89]

            if s1 > ms or (s1 == ms and l1 < ml):
                ms, ml = s1, l1
                
            ms = max(ms, s1)
            if s < m[s % 89]: m[s % 89], l[s % 89] = s, i + 1
             
        print(ml)


taskB()
