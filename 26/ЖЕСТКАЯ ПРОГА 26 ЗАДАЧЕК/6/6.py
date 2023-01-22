from bisect import *

with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file.read().split()])

    l1 = []
    
    for i in range(info):
        for j in range(i+1, info):
            avg = (l[i]+l[j])//2

            c = bisect_left(l, avg)
            #c = i+1   
            
            #for k in range(i+1, j):
            #    if avg > l[k]: c += 1
            #    else: break
            if c % 100 == 0 and c != 0: l1 += [c]
    print(len(l1), max(l1))
            
    
