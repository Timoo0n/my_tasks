def fileA():
    with open("27A_7874.txt", "r", encoding="utf-8") as file:
        n, k = [int(file.readline()) for _ in range(2)]
        l = [int(file.readline()) for _ in range(n)]
        count = 0

        for i in range(n):
            for j in range(i+k, n):
                if abs(i-j) >= k and abs(l[i]+l[j]) % 25 == 0:
                    count += 1
        print(count)
fileA()

def fileB():
    with open("27B_7874.txt", "r", encoding="utf-8") as file:
        n, k = [int(file.readline()) for _ in range(2)]
        count = 0
        q = [int(file.readline()) for _ in range(k-1)]
        info = [0]*25
        for i in range(n-k+1):
            num = int(file.readline())
            count += info[(25-(num%25))%25]

            info[q.pop(0)%25] += 1
            q.append(num)
        print(count)
        
fileB()
