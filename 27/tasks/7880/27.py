def fileA():
    with open('27A_7880.txt', 'r', encoding='utf-8') as file:
        n, k = [int(file.readline()) for _ in range(2)]
        l = [int(file.readline()) for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if (l[i]+l[j])%17 == 0 and abs(j-i) <= k: count += 1
                if abs(j-i) > k: break
        print(count)

fileA()
