def taskA():
    with open('27_A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]

        l_min = 10**20
        ms = 0
        
        for i in range(info):
            s = 0
            k = 0
            for j in range(i, info):
                s += l[j]
                k += 1
                if (s > ms or (s == ms and k < l_min)) and s % 69 == 0: ms = s; l_min = k
        print(l_min)


def taskB():
    with open('27_B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [float('inf')] * 69  # Мои префиксные суммы
        k  = [0] * 69  # Количества чисел скрывающиеся под суммами
        
        s = 0
        ms = float('-inf')
        kmin = float('inf')

        for i in range(info):
            num = int(file.readline())

            s += num
            if s % 69 == 0 and s > ms: ms = s; kmin = min(i+1, kmin)

            s1 = s - l[s % 69]  # Сумма
            k1 = (i + 1) - k[s % 69]  # Количество

            if s1 > ms or (ms == s1 and k1 < kmin):  # ПроверОЧКА
                ms, kmin = s1, k1

            if s < l[s % 69]:  # Стремимся сохранять как можно меньшую сумму
                l[s % 69] = s
                k[s % 69] = i + 1

        print(kmin)
                

if __name__ == '__main__': taskA(); taskB()
                
