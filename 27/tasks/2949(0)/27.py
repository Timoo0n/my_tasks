with open('27-A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [0]*10
    count = 0
    s = 0

    for _ in range(n):
        num = int(file.readline())
        s += num
        if s % 10 == 5: count += 1
        count += l[((s%10)+5)%10]

        l[s%10] += 1
    print(l)
    print(count)
    
