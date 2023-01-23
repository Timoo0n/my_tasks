with open('26.txt', 'r', encoding='utf-8') as file:
    s = file.read().strip().split('\n')
    n = int(s[0].split()[1])

    my_v, my_p = [], []  # разделим на типы файлов

    s = list(map(int, s[1:]))
    for i in s:
        if i <= 100: my_p += [i]
        elif i >= 101: my_v += [i]
    
    # 1)

    saved_v = []  # сохраним по условию видео, пока не займут половину или более
    for i in sorted(my_v):
        if sum(saved_v) <= n // 2: saved_v += [i]
        else: break

    # 2)
    n1 = n - sum(saved_v)

    saved_p = []  # сохраняю картинки
    for i in sorted(my_p):
        if sum(saved_p) + i <= n1: saved_p += [i]

    other_p = my_p[len(saved_p)+1:]  # срезаю с полного количества файлов сохраненные
    saved_p = saved_p[::-1]  # начинаю с конца

    for i in other_p:
        for j in range(len(saved_p)):
            if saved_p[j] <= i and sum(saved_p)+(i-saved_p[j]) <= n1: saved_p[j] = i  # заполняю диск на фулл
            else: break  # чтобы не было долгого бесмысленного перебора)

    print(n-sum(saved_p)-sum(saved_v))
    print(len(saved_p)+len(saved_v))
            
    
