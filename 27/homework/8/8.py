def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        c = 0
        
        for i in range(info):
            for j in range(i+1, info):
                if (l[i]+l[j]) % 80 == 0 and (l[i] > 50_000 or l[j] > 50_000): c += 1
        print(c)


def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
         
        l_max = [0]*80
        l_min = [0]*80
        
        for i in range(info):
            n = int(file.readline())
            remainder = n % 80
            if n > 50_000: l_max[remainder] += 1
            else: l_min[remainder] += 1
         
        count = (l_max[40]*(l_max[40]-1) // 2) + (l_max[0]*(l_max[0]-1) // 2)  # проверяем делящиеся на 0 и на 40
        count += l_max[0]*l_min[0] + l_max[40]*l_min[40]  # берем максимальные и минимальные

        for i in range(1, 39+1):  # тут вообще песня
            count += l_max[i]*l_max[80-i]
            count += l_max[i]*l_min[80-i]
            count += l_min[i]*l_max[80-i]
        print(count)
         

if __name__ == '__main__': taskA(); taskB()
