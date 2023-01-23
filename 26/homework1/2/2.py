with open('26.txt') as file:
    info = int(file.readline())
    l = [int(i) for i in file]
    #info = 5
    #l = sorted([80, 30, 10, 50, 45])

    max_l, min_l = [], []

    while l:
        if (not max_l) or sum(max_l) < sum(min_l): l = sorted(l, reverse=True); max_l += [l.pop(0)]
        if sum(max_l) >= sum(min_l):
            l = sorted(l)
            for i in range(len(l)):
                if sum(min_l) <= sum(max_l): min_l += [l.pop(0)]
        print(len(l))
        
    print(len(max_l), len(min_l))

     
     

    
