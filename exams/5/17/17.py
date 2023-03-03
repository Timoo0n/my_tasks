with open('17.txt', 'r', encoding='utf-8') as file:
    l = [int(i) for i in file]

    l1 = []
    for i in range(len(l)-1):
        if l[i]+l[i+1] >= 100 and (l[i] < 0 or l[i+1] < 0):
            l1 += [l[i]*l[i+1]]
    print(len(l1), max(l1))
            
