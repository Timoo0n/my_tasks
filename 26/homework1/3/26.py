with open('26.txt', 'r', encoding='utf-8') as file:
    n, s = map(int, file.readline().split())
    l = sorted([int(i) for i in file])[::-1]

    place = []

    while l:
        flight = []  # наш рейс
        while l and sum(flight)+l[0] < s:  # заполняю сначала максимумами
            flight += [l.pop(0)]
            
        difference = s - sum(flight)
        
        for i in range(difference, 0, -1):  # ищу, есть ли подходящие грузы с оставшейся массой
            if i in l:
                flight += [i]
                l.remove(i)
                break
        
        place += [sum(flight)]

    print(len(place), place[-1])

         
        
    
         
            

        
        
        
