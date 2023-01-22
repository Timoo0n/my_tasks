from bisect import *


with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l = sorted([int(i) for i in file])  

    avg_list = []
    for i in range(info):
        for j in range(i+1, info):
            sum_value = l[i]+l[j]

            if sum_value % 2 == 0:

                avg = sum_value // 2
                
                max_value = l[bisect_left(l, avg)]
                if abs(avg - max_value) == 5: avg_list += [avg]

                max_value = l[bisect_left(l, avg)-1]
                if abs(avg - max_value) == 5: avg_list += [avg]

                #coll = [abs(avg-k) for k in l[i:j+1]]

                #if min(coll) == 5: avg_list += [avg]

    print(avg_list)
    print(len(avg_list), min(avg_list))
                    
