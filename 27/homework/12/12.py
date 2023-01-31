def taskA():  # 65406
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 10
        #l = [37, 45, 61, 50, 55, 98, 79, 49, 60, 69]
        
        max_value = 0
        for i in range(info):
            for j in range(i+1, info):
                if l[i]+l[j] > max_value and (l[i]+l[j]) % 2 == 0 and l[i]*l[j]% 23 == 0: max_value = l[i]+l[j]
        print(max_value)


def taskB():
    with open('27B.txt', encoding='utf-8') as file:
        info = int(file.readline())

        even_l_23_1 = []  # четное, кратное 23
        even_l_23_0 = []  # четное, не кратное 23
        odd_l_23_1 = []  # нечетное, кратное 23
        odd_l_23_0 = []  # нечетное, некратное 23

        for _ in range(info):
            n = int(file.readline())
            if n % 2 == 0 and n % 23 == 0: even_l_23_1 += [n]
            elif n % 2 == 0 and n % 23 != 0: even_l_23_0 += [n]
            elif n % 2  != 0 and n % 23 == 0: odd_l_23_1 += [n]
            elif n % 2 != 0 and n % 23 != 0: odd_l_23_0 += [n]

        even_l_23_1.sort(reverse=1)
        even_l_23_0.sort(reverse=1)
        odd_l_23_1.sort(reverse=1)
        odd_l_23_0.sort(reverse=1)

        end_l = even_l_23_1[:2] + even_l_23_0[:2] + odd_l_23_1[:2] + odd_l_23_0[:2]  # здесь наша заветная максимальная сумма
        max_value = 0
        for i in range(len(end_l)):
            for j in range(i+1, len(end_l)):
                if (end_l[i]+end_l[j]) % 2 == 0 and (end_l[i]+end_l[j]) > max_value and end_l[i]*end_l[j] % 23 == 0:
                    max_value = end_l[i]+end_l[j]
        print(max_value)
                
                
        
        
if __name__ == '__main__': taskA(); taskB()
