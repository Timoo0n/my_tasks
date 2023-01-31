

def taskA():  # 1
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 6
        #l = [400, 100, 1600, 1200, 100, 800]
        c = 0
        
        for i in range(info):
            for j in range(i+1, info):
                if (l[i]+l[j]) == 2000: c += 1
        print(c)


def taskB():  # 2
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        l = [0]*2000
        for i in range(info):
            n = int(file.readline())
            if n < 2000: l[n] += 1

        count = l[1000]*(l[1000]-1) // 2

        for i in range(1, 999+1):
            count += l[i]*l[2000-i]
        print(count)
        
        

if __name__ == '__main__': taskA(); taskB()
