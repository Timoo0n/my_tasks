
def taskA():  # 31
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        count = 0
        
        for i in range(info):
            for j in range(i+1, info):
                if (l[i]+l[j]) % 131 == 0:
                    count += 1
                    
        print(count)


def taskB():  # 381543
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [0]*131  # кидаем сюда количества разных остатков
         
        for i in range(info):
            n = int(file.readline())
            l[n%131] += 1

        c = l[0]*(l[0]-1) // 2  # считаем комбинаторно
        for i in range(1, 66):  # сложна
            c += l[i]*l[131-i]
        print(c)
             
            
if __name__ == '__main__': taskB()
