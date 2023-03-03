with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    l = [0]*666
    count = 0
    s = 0

    for _ in range(n):
        num = int(file.readline())
        s += num
        
        if s % 666 == 0: count += 1
        count += l[s % 666]
        
        l[s % 666] += 1
    print(count)
    print(l)
