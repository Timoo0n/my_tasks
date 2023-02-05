def taskA():
    with open('27_A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        max_s = 0
        
        for i in range(info):
            k = 0
            s = 0
            for j in range(i, info):
                s += l[j]
                if l[j] % 5 == 0: k += 1
                if k % 3 == 0:   max_s = max(max_s, s)
        print(max_s)


def taskB():
    with open('27_B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [float('inf') for _ in range(3)]

        ms = float('-inf')
        k = 0
        s = 0

        for i in range(info):
            num = int(file.readline())

            s += num
            if num % 5 == 0: k += 1
            if k % 3 == 0: ms = max(ms, s)

            ms = max(ms, s - l[k % 3])

            l[k % 3] = min(l[k % 3], s)
        print(ms)
         
            
if __name__ == '__main__': taskA(); taskB()
