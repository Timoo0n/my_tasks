with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    k5 = k13 = k65 = k = 0
    count = 0
    
    for i in range(info):
        num = int(file.readline())
        # Здесь получается инь и ян
        if num % 65 == 0: count += k
        elif num % 5 == 0: count += k13
        elif num % 13 == 0: count += k5
        else: count += k65

        # Здесь вообще песня, учитываем ВСЕ!!!!!!
        k += 1
        if num % 65 == 0: k65 += 1
        if num % 13 == 0: k13 += 1 
        if num % 5 == 0: k5 += 1
    print(count)

#  1) 168
#  2) 2503584
