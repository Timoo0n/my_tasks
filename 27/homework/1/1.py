def taskA():  # 2459
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        c = 0
        
        for i in range(info):
            for j in range(i+1, info):
                if (l[i] + l[j]) % 2 == 0: c += 1
        print(c)


def taskB():  # 24995121
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        # Сумма будет четной, если числа будут четными или нечетными
        k = k1 = 0
        for i in range(info):
            num = int(file.readline())
            if num % 2 == 0: k += 1
            else: k1 += 1
        value = (k*(k-1) // 2) + (k1*(k1-1) // 2) # считаем количество пар комбинаторно
        print(value)


if __name__ == '__main__': taskB()
