

def taskA():  # 412920
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        k = 0
        
        for i in range(info):
            s = 0
            for j in range(i, info):
                s += l[j]
                if s % 666 == 0: k += 1
        print(k)


def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        l = [0]*666

        value = k = 0
        
        for _ in range(info):
            num = int(file.readline())

            value += num
            if value % 666 == 0:k += 1
            k += l[value % 666]

            l[value % 666] += 1
        print(k)
            
        

if __name__ == '__main__': taskA(); taskB()
