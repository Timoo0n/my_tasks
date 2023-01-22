with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file.read().split()])
    
    set_l = set(l)
    value = l[2500]
    avg_list = []
    
    for i in range(info):
        for j in range(i+1, info):
            if (l[i]+l[j]) % 2 == 0:
                avg_value = (l[i]+l[j])//2
                if avg_value < value: avg_list += [avg_value]
    print(len(avg_list), max(avg_list))
            
    
