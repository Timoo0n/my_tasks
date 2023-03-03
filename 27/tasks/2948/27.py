with open('27-B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    d = {i: [] for i in range(100)}
    s = 0
    for num in file:
        num = int(num)
        d[num%100].append(num)
    print(d)
    
    for key in list(d.keys())[1:50]:
        key1 = 100 - key
        if d[key] and d[key1]:
            length = min(len(d[key]), len(d[key1]))
            l, l1 = sorted(d[key])[::-1], sorted(d[key1])[::-1]
            for i in range(length):
                s += l[i]+l1[i]
                d[key].remove(l[i])
                d[key1].remove(l1[i])
    for i in d.keys():
        print(i, d[i])
            
         
    
 
