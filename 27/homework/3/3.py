from itertools import combinations


def taskA():  # 168
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        l = [int(i) for i in file]
        c = 0
        
        for i, j in combinations(l, 2):
            if (i * j) % 65 == 0: c += 1
        print(c)

def taskB():  # 2503584
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        # 65 = 5*13 => что у нас возможны несколько случаев:
        # 1) оба кратны 65
        # 2) один из чисел кратен 65
        # 3) когда 1 кратен 13, а другой 5

        k65 = k13 = k5 = k = 0
        for i in range(info):
            n = int(file.readline())
            if n % 65 == 0: k65 += 1
            elif n % 13 == 0: k13 += 1
            elif n % 5 == 0: k5 += 1
            else: k += 1
        value = (k65*(k65-1) // 2) + k65 * (k13+k+k5) + k13 * k5

        print(value)
             
        

if __name__ == '__main__': taskA(); taskB()
