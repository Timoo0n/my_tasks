
# 5067 КЕГЭ

def taskA():
    with open('27-A.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [int(i) for i in file]
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if (l[i]+l[j]) % 3 == 0 and (l[i]*l[j]) % 4096 == 0: count += 1
        print(count)
        

def taskB():
    with open('27-B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())

        div = [i for i in range(2, 4097) if 4096 % i == 0]
        l = [{i: 0 for i in div + [0]} for _ in range(3)]
        count = 0
        
        for _ in range(info):

            num = int(file.readline())
            ind = 0 if num % 3 == 0 else 3 - (num % 3)
            ind1 = 0
            
            for i in div:
                if num % i == 0:  ind1 = i
            
            if ind1 == 0: ind1 = 4096
            elif ind1 == 4096: ind1 = 0
            else:
                ind1 = (4096 // ind1)

            count += l[ind][ind1]
                     
            ind_1 = num % 3
            l[ind_1][0] += 1
            for i in div:
                if num % i == 0:
                    l[ind_1][i] += 1
        print(count)
                
if __name__ == '__main__': taskB()
            
        
        
        
