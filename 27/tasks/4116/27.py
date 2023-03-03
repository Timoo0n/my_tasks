from bisect import *


with open('27A.txt', 'r', encoding='utf-8') as file:
    n, k = map(int, file.readline().split())
    l = [int(file.readline()) for _ in range(n)]
    l1, s = [], 0
    for i in range(n):
        s += l[i]
        l1.append(s)

    s = 0
    length = float('-inf')
    for i in range(n):
        s += l[i]
        value = k - s
        ind = bisect_right(l1, value)
        length = max(length, ind-i)
    print(length)
        
