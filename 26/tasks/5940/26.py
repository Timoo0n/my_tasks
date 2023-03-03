with open('26.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = sorted([s for s in file], key=lambda el: int(el.split()[0]))
    my_dict = dict()
    for i in l:
        s = i.split()
        my_dict[int(s[0])] = sorted([int(s[1]), int(s[2])])
    
    s = 0
    id0 = min(my_dict.keys())

    while True:
        if (id0 + 1) in my_dict.keys() and (id0 + 2) in my_dict.keys():
            if min(my_dict[id0+1]) > min(my_dict[id0+2]):
                s += min(my_dict[id0])
                id0 += 2
            else:
                s += min(my_dict[id0])
                id0 += 1
        elif (id0 + 1) in my_dict.keys():
            s += min(my_dict[id0])
            id0 += 1
        elif (id0 + 2) in my_dict.keys():
            s += min(my_dict[id0])
            id0 += 2
                
        else: break
    print(id0, s)
