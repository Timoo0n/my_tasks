def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:

        info = int(file.readline())
        l = [int(i) for i in file]

        ms = float('-inf')

        for i in range(info):
            s = 0
            k = 0
            for j in range(i, info):
                s += l[j]
                if abs(l[j]) % 2 == 0 and l[j] > 0: k += 1
                if k % 30 == 0: ms = max(ms, s)
            
        print(ms)


def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        k = 0
        s = 0
        
        ms = float('-inf')
        l = [float('inf')] * 30
        
        for _ in range(info):

            num = int(file.readline())
            s += num

            if num % 2 == 0 and num > 0: k += 1
            if k % 30 == 0: ms = max(ms, s)

            
            s1 = s - l[k % 30]
            ms = max(s1, ms)
            
            l[k % 30] = min(l[k % 30], s)
        print(ms)

            


if __name__ == '__main__': taskA(); taskB()
