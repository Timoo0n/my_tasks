from bisect import *

with open('26.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = sorted([int(i) for i in file])
    
    collection = []
    for i in range(n):
        for j in range(i+1, n):
            if (l[i]+l[j])% 2 == 0:
                avg = (l[i]+l[j])//2
                 
                if l[2499] < avg < l[3750]:
                    collection += [avg]

                
    print(len(collection), min(collection))
      
    
    
