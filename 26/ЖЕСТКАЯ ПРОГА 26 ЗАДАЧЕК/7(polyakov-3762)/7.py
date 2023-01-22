
with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = [int(i) for i in file.read().split()]
    l_set = set(l)
    
    values_list = []
    for i in range(info):
        for j in range(i+1, info):
            for k in range(j+1, info):
                sum_value = l[i]+l[j]+l[k]
                if sum_value % 3 == 0:
                    avg = sum_value // 3
                    if avg in l_set: values_list += [avg]
    print(len(values_list), min(values_list))
                        
                
    
