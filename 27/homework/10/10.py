
def taskA():  # 73319
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        #info = 10
        #l = [74, 90, 63, 55, 31, 28, 32, 99, 1, 81] 
        
        s = 0
        for i in range(info):
            for j in range(i+1, info):
                if s < (l[i]+l[j]) and (l[i]+l[j]) % 2 == 1:
                    s = l[i]+l[j]
        print(s)

def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        even = []  # четные числа
        odd = []  # нечетные числа

        for i in range(info):
            n = int(file.readline())
            if n % 2 == 0: even += [n]
            else: odd += [n]
        print(max(even)+max(odd))
            
        

if __name__ == '__main__': taskA(); taskB()
            
