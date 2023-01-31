def taskA():  # 21831874
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 10
        #l = [57, 96, 38, 93, 42, 10, 85, 44, 57, 29]
        
        min_value = 10*10**20
        
        for i in range(info):
            for j in range(i+1, info):
                if l[i]*l[j] % 31 == 0:
                    if l[i]*l[j] < min_value:
                        min_value = l[i]*l[j]
        print(min_value)

def taskB():  # 3472
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l_1 = []
        l_0 = []

        for _ in range(info):
            n = int(file.readline())
            if n % 31 == 0: l_1 += [n]
            else: l_0 += [n]

        l_1.sort()
        l_0.sort()
        value = min(l_0[0]*l_1[0], l_1[0]*l_1[1])
        print(value)
            
            
if __name__ == '__main__': taskB()
