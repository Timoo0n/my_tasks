def taskA():  # 61
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        c = 0
        for i in range(info):
            for j in range(i+1, info):
                if abs(l[i]-l[j]) % 69 == 0: c += 1
        print(c)


def taskB():  # 725088
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [0]*69

        for i in range(info):
            n = int(file.readline())
            l[n%69] += 1

        c = 0
        for i in range(len(l)):
            c += (l[i]*(l[i]-1)) // 2
            
        print(c)


if __name__ == '__main__': taskA(); taskB()
