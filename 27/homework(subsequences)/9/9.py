def taskA():
    with open('27_A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        count = 0

        for i in range(info):
            s = 0
            k = 0
            for j in range(i, info):
                s += l[j]
                k += 1
                if k >= 5 and s % 117 == 0: count += 1
        print(count)


def taskB():
    with open('27_B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        q = []
        s = 0
        for i in range(4):
            num = int(file.readline())
            s += num
            q += [s]
        
        l = [0] * 117

        count = 0
        
        for _ in range(info-4):
            num = int(file.readline())
            s += num

            if s % 117 == 0: count += 1
            count += l[s % 117]

            value = q.pop(0)
            l[value % 117] += 1
            q.append(s)
        print(count)

taskA(); taskB()

            
            
            
            
         
