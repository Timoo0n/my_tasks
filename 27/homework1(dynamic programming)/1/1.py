with open('27A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    count = 0
    k = 0  # кол-во ВСЕХ предыдущих чисел
    k7 = 0  # кол-во предыдущих чисел, делящихся на 7

    for i in range(n):
        x = int(file.readline())

        # учитываю пары на основе прошлой статистики
        if x % 7 == 0: count += k
        if x % 7 != 0: count += k7

        # учитываю это число в статистику
        k += 1
        if x % 7 == 0: k7 += 1
        
    print(count)
    
