with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    l = [10**20]*144 # храню минимумы
    ms = 10**20
    
    for _ in range(info):
        num = int(file.readline())

        remainder = 0 if num % 144 == 0 else 144 - (num % 144)

        if l[remainder] < num:
            ms = min(ms,l[remainder] + num)

        l[num % 144] = min(l[num % 144], num)

    print(ms)
        
        
