
def taskA():  # 4
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        c = 0

        for i in range(info):
            for j in range(i+1, info):
                for k in range(j+1, info):
                    if all(l[x] % 19 == 0 for x in (i, j, k)): c += 1
        print(c)


def taskB():  # 25808936
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        k = 0
        for i in range(info):
            n = int(file.readline())
            if n % 19 == 0: k += 1
        print(k*(k-1)*(k-2)//6)
            
            
if __name__ == '__main__': taskA(); taskB()
