with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = [int(i) for i in file.read().split()]
    l1 = set(l)

    new_l = []
    
    for i in range(info):
        for j in range(i+1, info):
            if (l[i] + l[j]) % 2 == 0 and (l[i]+l[j])//2 in l1: new_l += [(l[i]+l[j])//2]
    print(len(new_l), max(new_l))
