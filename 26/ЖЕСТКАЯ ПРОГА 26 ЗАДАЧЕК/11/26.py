with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file])

    length = 150_000
    l1 = [0] * length

    for i in range(info):
        value = l[i]
        if value < 20:
            for j in range(value):
               l1[j] = 1
            for j in range(20):
                l1[j+value] = 1
            
        elif length - value < 20:
            for j in range(20):
                l1[value-1-j] = 1
                if value-1+j < length:
                    l1[value-1+j] = 1
        else:
            for j in range(20):
                l1[value-j-1], l1[value+j] = 1, 1
         
    road = ''.join(list(map(lambda el: str(el), l1)))  # сгенерировали такую дорогу
    
    #1)
    c0 = 1
    for i in range(length):
        if road[i] == '0' and road[i-1] == '1': c0 += 1
        if c0 == 500: print(i); break
            
    #2)
    list_info = list(map(lambda el: len(el), road.replace('1', ' ').split()))
    print(list_info[500-1]) 
     
     
    
        
     
    
    

     
     
            
     
