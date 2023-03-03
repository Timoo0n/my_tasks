def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [int(i) for i in file]
        ln = 0
        for i in range(n):
            c1 = 0
            c2 = 0
            for j in range(i, n):
                if l[j] % 2 == 0: c2 += 1
                elif l[j] % 2 == 1: c1 += 1
                if c1 == c2: ln = max(c1+c2, ln)
        print(ln)

def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        mx = 0

        d = dict()
        k = k1 = 0
        for _ in range(n):
            num = int(file.readline())

            if num % 2 == 0: k += 1
            else: k1 += 1
            
            if k == k1: mx = k+k1
            if k-k1 in d: mx = max(mx, k+k1 - d[k-k1])

            if k-k1 not in d:
                d[k-k1] = k + k1
        print(mx)
taskB()
                
                
            
        
            
