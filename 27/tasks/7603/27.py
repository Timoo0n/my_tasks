def f():
    with open('27A_7603.txt', 'r', encoding='utf-8') as file:
        n, k = [int(file.readline()) for _ in range(2)]
        l = [int(i) for i in file]
        mx = float('-inf')
        for i in range(n):
            for j in range(k+i, n):
                if abs(j-i) >= k: mx = max(mx, l[i]+l[j])
        print(mx)


def f1():
    with open('27B_7603.txt', 'r', encoding='utf-8') as file:
        n, k = [int(file.readline()) for _ in range(2)]
        l = [int(i) for i in file]
        mx = float('-inf')
        num_before = l[0]
        mx = float('-inf')
        for i in range(k, n):
            num_before = max(num_before, l[i-k])
            mx = max(mx, num_before+l[i])
    print(mx)
f1()
