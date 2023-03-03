def f():  # НЕЭФФЕКТИВНОЕ
    with open('27A.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [int(i) for i in file]
        mx = 0
        for i in range(n):
            s = 0
            for j in range(n):
                s += abs(j-i)*l[j]
            mx = max(mx, s)
        print(mx)


def f1():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [int(i) for i in file]
        value = sum(l)
        l1 = []
        s = 0
        for i in range(n):
            s += l[i]
            l1.append(s)
        s = mx = 0
        for i in range(n):
            s += l[i]*i
            
        for i in range(1, n):
            s = s + l1[i-1] - (value - l1[i-1])
            mx = max(s, mx)
        print(mx)

f(); f1()
       
 
