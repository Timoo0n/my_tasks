with open('test.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    l = [[10**20]*107 for _ in range(5)]
    ms = 10**20

    for i in range(info):
        num = int(file.readline())

        ind = i % 5
        ind1 = 0 if num % 107 == 0 else 107 - (num % 107)

        if l[ind][ind1] != 10**20:
            ms = min(ms, num + l[ind][ind1])
            
        l[ind][num % 107] = min(num,  l[ind][num % 107])

    print(ms)
        
        
