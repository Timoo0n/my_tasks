
def f():  # Неэффективное решение
    with open('27A.txt', 'r', encoding='utf-8') as file:
        n, m = map(int, file.readline().split())
        l = [int(i) for i in file]
        ms = float('-inf')
         
        for i in range(n):
            s = 0
            for j in range(n):
                if abs(j-i) <= m:
                    s += l[j]
            ms = max(ms, s)
        print(ms)


def f1():  # Эффективное
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n, m = list(map(int, file.readline().split()))
        l = [int(i) for i in file]
        ms = s = sum(l[:2*m+1]) 
        for i in range(m+1, n-m):
            s = s+l[m+i]-l[i-m-1]
            ms = max(ms, s)
        print(ms)
f1(); f()
