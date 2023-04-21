with open('26_7709.txt', 'r', encoding='utf-8') as file:
    k, n = [int(file.readline()) for _ in range(2)]
    visitors = sorted([[int(time) for time in info.split()] for info in file], key=lambda el: el[0])
    salon = [0]*k
    master_info = []
    
    for i in range(k):
        salon[i] = visitors[0][1]
        master_info.append(i+1)
        visitors.pop(0)
        
    while visitors:
        first_time, end_time = visitors[0][0], visitors[0][1]
        for i in range(k):
            if first_time >= salon[i]+1:
                salon[i] = end_time
                master_info.append(i+1)
                visitors.pop(0)
                break
        else:
            visitors.pop(0)
    
    print(len(master_info), master_info[-1])
