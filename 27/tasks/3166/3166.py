with open('27A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [int(i) for i in file]
    count = 0
    for i in range(n):
        k = 0
        for j in range(i, n):
            if l[j] % 5 == 0: k += 1
            if k > 0 and k % 11 == 0: count += 1
    print(count)
            
            
        
            
