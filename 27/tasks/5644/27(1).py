for word in 'AB':
    with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [int(i) for i in file]
        s = mx = 0
        value = sum(l)
        l1 = []
        for i in range(n):
            s += l[i]
            l1.append(s)
        s = 0

        for i in range(n):
            s += i*l[i]

        for i in range(1, n):
            #s = s - sum(l[i:]) + sum(l[:i]) - ПОЯВИЛАСЬ ПРОБЛЕМА, ФАЙЛ B РАБОТАЕТ МЕДЛЕННО
            # А ДАВАЙ-КА НЕ БУДЕМ МИЛЛИАРД РАЗ СЧИТАТЬ МИЛЛИОНЫ ЧИСЕЛ
            # ПРОСТО СДЕЛАЕМ ПРЕФИКСНЫЕ СУММЫ И БУДЕМ КАЙФОВАТЬ
            s = s + l1[i-1] - (value-l1[i-1])
            mx = max(mx, s)
        print(mx)
            
    
