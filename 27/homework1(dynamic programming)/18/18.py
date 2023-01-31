with open('27A.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    k = [[] for _ in range(134)]
    count = 0
    
    for _ in range(info):
        num = int(file.readline())

        if num < 134:
            value = 134 - num
            for i in range(1, value+1):
                for j in k[i]:
                    if num < j: count += 1
            print(num, count)
                    
            k[num].append(num)
            
    print(count)
            
