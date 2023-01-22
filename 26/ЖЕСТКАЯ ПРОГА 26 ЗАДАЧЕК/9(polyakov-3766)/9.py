with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file])

    values_l = []
    for i in range(info):
        for j in range(i+1, info):
            if (l[i] + l[j]) % 2 == 0:
                avg = (l[i]+l[j]) // 2

                if l[2499] < avg < l[3750]:
                    values_l += [avg]
    print(len(values_l), min(values_l))
                
            
    
