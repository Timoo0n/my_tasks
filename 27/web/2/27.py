def f():  # НЕЭФФЕКТИВНОЕ РЕШЕНИЕ
    with open('27A.txt', 'r', encoding='utf-8') as file:
        n, m = map(int, file.readline().split())
        for _ in range(n):
            num = int(file.readline())
            num = num//6 if num % 6 == 0 else num // 6 + 1
            l += [num]
        mx = float('-inf')
        for i in range(n):
            s = 0
            for j in range(n):
                if min(abs(j-i), n-abs(j-i)) <= m:
                    s += l[j]
            mx = max(mx, s)
        print(mx)


def f1(): # ЭФФЕКТИВНОЕ РЕШЕНИЕ
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n, m = map(int, file.readline().split())
        l = [int(i) for i in file]
        for _ in range(n):
            num = int(file.readline())
            num = num // 6 if num % 6 == 0 else num // 6 + 1
            l += [num]
        l = l*2
        mx = s = sum(l[:2*m+1])
        for i in range(m+1, n+m):
            s = s - l[i-m-1] + l[m+i]
            mx = max(mx, s)
        print(mx)

