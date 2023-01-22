with open('26.txt') as file:
    volume = list(map(int, file.readline().split()))[0]
    my_list = sorted([int(i) for i in file.read().split()])
    
    l = []
    for i in my_list:
        if sum(l) + i <= volume: l += [i]
        else: break
        

    value = volume-sum(l)
    other_list = my_list[len(l):]
    for i in range(value, 0, -1):
        if i + max(l) in other_list: l[-1] = max(l)+i; break
    print(len(l), max(l))
    print(l)
     
    
