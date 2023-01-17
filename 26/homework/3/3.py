with open('26.txt', 'r', encoding='utf-8') as file:

    s = file.read().strip().split('\n')
    n = int(s[0].split()[1])

    k_l = []
    v_l = []
    
    for i in sorted(s[1:]):
        i = int(i)
        if i <= 100: k_l += [i]
        elif i >= 101: v_l += [i]

    """        """
    my_k = [] # здесь хранятся картинки
    # сохранию максимальное значение картинок
    for j in sorted(k_l):
        if sum(my_k) + j <= n//2: my_k += [j]
     
    
    other_k = k_l[len(my_k)+1:]
    my_k = my_k[::-1]

    # забиваю объемом файла по-максимому
    for i in other_k:
        for j in range(len(my_k)):
            if my_k[j] < i and sum(my_k)+(i-my_k[j]) <= n // 2: my_k[j] = i
            else: break

    """        """
    my_v = [] # здесь хранятся видео
    for j in sorted(v_l):
        if sum(my_v) + j <= n//2: my_v += [j]

    other_v = v_l[len(my_v)+1:]
    my_v = my_v[::-1]
    
    for i in other_v:
        for j in range(len(my_v)):
            if my_v[j] < i and sum(my_v)+(i-my_v[j]) <= n // 2: my_v[j] = i
            else: break

    print(n-sum(my_v)-sum(my_k))
    print(sorted(my_k))
     
    

     
    
     
        
     

    
