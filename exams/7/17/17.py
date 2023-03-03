with open('17.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file]
    value = len([i for i in l if abs(i) < 100])

    my_list = []
    
    for i in range(len(l)-1):
        if (l[i]+l[i+1])/2 > value:  
            my_list += [l[i]+l[i+1]]
    print(len(my_list), max(my_list))
            
        
