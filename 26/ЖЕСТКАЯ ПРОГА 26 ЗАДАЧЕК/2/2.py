with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline().split()[1])
    my_list = sorted([int(i) for i in file.read().split()])

    my_list1 = list(filter(lambda el: 180 <= el <= 200, my_list)) # Первая погрузка
    my_list = sorted(list(filter(lambda el: el > 200 or el < 180, my_list)))

    # Вторая погрузка
    my_list2 = []

    for i in my_list:
        if sum(my_list2) + i <= (info - sum(my_list1)): my_list2 += [i]
        else: break

    other = info-sum(my_list2)-sum(my_list1) # сколько осталось

    # Отбираем
    for i in range(len(my_list2)):
        if i != 0:
            if other != 0:
                for j in range(other, 0, -1):  # тот случай, когда впихиваем как можно больше
                    if my_list2[i]+j in my_list:  
                        if sum(my_list2) + j + sum(my_list1) <= info:
                            my_list2[i] = my_list2[i]+j
                            other = other-j
                            break
            else: break
    print(len(my_list1)+len(my_list2), sum(my_list1)+sum(my_list2))
        
    

     
       
