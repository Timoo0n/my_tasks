with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    p_road = ['0']*2_000_000

    for i in range(info):
        s, e = map(int, file.readline().split())
        for j in range(s, e):
            p_road[j] = '1'
    p_road = list(map(lambda el: len(el), ''.join(p_road).replace('0', ' ').split()))
    print(len(p_road), sum(p_road))
    
    
    
    
