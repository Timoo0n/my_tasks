with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for _ in range(10)]
    min_v = 10**30
    
    for _ in range(info-10):
        num = int(file.readline())
        l_0 = [10**20]*1071
        l_1 = [10**20]*1071

        for i in q:
            if i % 2 == 0:
                l_0[i % 1071] = min(l_0[i % 1071], i)
            else:
                l_1[i%1071] = min(l_1[i%1071], i)

        ind = 0 if num % 1071 == 0 else 1071 - (num % 1071)
        if num % 2 == 0 and l_0[ind] != 10**20:
            min_v = min(min_v, l_0[ind]+num)

        elif num % 2 == 1 and l_1[ind] != 10**20:
            min_v = min(min_v, l_1[ind]+num)

        q.pop(0)
        q.append(num)

    print(min_v)
            
            
            
            
        
     
