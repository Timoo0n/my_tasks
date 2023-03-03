with open('27-B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    div = [i for i in range(2,59050) if 59049 % i == 0]
    
    my_list = [{i: 0 for i in [0] + div} for _ in range(4)]
    count = 0

    for _ in range(n):
        num = int(file.readline())
        ind = 0 if num % 4 == 0 else 4 - (num % 4)
        ind1 = 0
        for i in div:
            if num % i == 0: ind1 = i

        if ind1 == 59049: ind1 = 0
        elif ind1 == 0: ind1 = 59049
        else: ind1 = 59049 // ind1
        count += my_list[ind][ind1]

        my_list[num % 4][0] += 1
        for i in div:
            if num % i == 0:
                my_list[num % 4][i] += 1
    print(count)
        
        
