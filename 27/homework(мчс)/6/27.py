with open('27-A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    s = [0]*10
    for _ in range(n):
        num = int(file.readline())
        s1 = s.copy()
        s1[num%10] += 1
        for i in range(10):
            s1[(i+num)%10] += s[i]
        s = s1
    print(s[5])
