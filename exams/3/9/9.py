with open('9.txt', 'r', encoding='utf-8') as file:
    my_l = [sorted([ int(j) for j in i.split()]) for i in file.read().strip().split('\n')]
    c = 0
    
    for l in my_l:
        if len(l) != len(set(l)): c += 1
        else:
            l_set = {l[i]-l[i-1] for i in range(1, len(l))}
            if len(l_set) == 1: c += 1
    print(c)
