from itertools import combinations

def taskA():  # 1056
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]

        c = 0
        for i, j in combinations(l, 2):
            if (i+j) % 2 == 1 and i*j % 5 == 0:
                c += 1
        print(c)


def taskB():  # 8863690
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        #Случаи:
        #1) кратно 5 и нечетное = k1
        #2) кратно 5 и четное = k2
        #3) не кратно 5 и четное = k3
        #4) не кратно 5 и нечетное = k4
        # нам нужно, чтобы была такая штука:
        # k1*k2+k1*k3+k2*k4

        k1 = k2 = k3 = k4 = 0
        for i in range(info):
            num = int(file.readline())
            if num % 5 == 0 and num % 2 == 1: k1 += 1
            if num % 5 == 0 and num % 2 == 0: k2 += 1
            if num % 5 != 0 and num % 2 == 0: k3 += 1
            if num % 5 != 0 and num % 2 == 1: k4 += 1
        value = k1*k2 + k1*k3 + k2*k4
        print(value)
             
         

if __name__ == '__main__': taskA(); taskB()
