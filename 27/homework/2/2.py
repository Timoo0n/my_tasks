def taskA():  # 1209
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        c = 0
        
        for i in range(info):
            for j in range(i+1, info):
                if l[i]*l[j] % 7 == 0: c += 1
    print(c)


def taskB():  # 13831740
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        # 2 случая: либо оба кратны 7, либо 1 из 2 кратен 7
        k = k7 = 0
        for i in range(info):
            num = int(file.readline())
            if num % 7 == 0: k7 += 1
            else: k += 1
        value = (k7*(k7-1) // 2) + (k*k7)  # считаю комбинаторно случаи
        print(value)
            

if __name__ == '__main__': taskB()
