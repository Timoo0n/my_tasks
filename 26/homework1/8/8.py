with open('26.txt', 'r', encoding='utf-8') as file:
    l, m, n = map(int, file.readline().split())
    my_l = ['0']*l

    for i in range(n):
        st, time = map(int, file.readline().split())
        for j in range(st, st+time):
            my_l[j] = '1'
    my_l = list(filter(lambda el: el >= m, list(map(lambda el: len(el), ''.join(my_l).replace('1', ' ').split()))))
    print(len(my_l), max(my_l))
    
        
        
