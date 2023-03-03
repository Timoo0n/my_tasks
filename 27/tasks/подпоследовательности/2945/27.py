with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    max_sum = 0
    s = 0
    l = [float('inf')] * 67 # минимальные хвостики
    for i in range(n):
        num = int(file.readline())
        s += num
        if s % 67 == 0: max_sum = max(max_sum, s)
        max_sum = max(s-l[s%67], max_sum)  # вычли минимальный хвост с тем же остатком

        l[s % 67] = min(s, l[s % 67])
        
    print(max_sum)
     
