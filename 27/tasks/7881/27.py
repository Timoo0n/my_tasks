with open("27A_7881.txt", "r", encoding="utf-8") as file:
    n, k = [int(file.readline()) for _ in range(2)]
    l = [int(file.readline()) for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(i-j) <= k and abs(l[i]-l[j]) % 100 == 0 and ((l[i] % 37 == 0 and l[j] % 37 !=0) or (l[i] % 37 != 0 and l[j] % 37 ==0)):
                count += 1
    print(count)
