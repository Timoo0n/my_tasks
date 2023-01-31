with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = [int(i) for i in file]

    set_l = set(l)

    my_l = []
    for i in range(info):
        for j in range(i+1, info):
            if l[i] % 2 == 1 and l[j] % 2 == 0 or l[i] % 2 == 0 and l[j] % 2 == 1:
                sum_value = l[i]+l[j]
                if sum_value in set_l:
                    my_l += [sum_value]
    print(len(my_l), max(my_l))
                    
                    
