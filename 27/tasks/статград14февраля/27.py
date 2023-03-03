with open('27-B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())

    temp_l = [int(file.readline()) for _ in range(13)]

    dividers = sorted([i for i in range(2, 19683+1) if 19683 % i == 0])
    l = [{i: 0 for i in [0] + [1] + dividers} for _ in range(8)]

    count = 0

    for _ in range(n-13):
        num = int(file.readline())

        ind = 0 if num % 8 == 0 else 8 - (num % 8)

        if num % 19683 == 0: ind1 = 1  # если число делится на все
        else:
            max_value = float('-inf')
            for div in dividers:
                if num % div == 0:
                    max_value = max(max_value, div)
            if max_value == float('-inf'): ind1 = 0  # если число не делится
            else: ind1 = 19683 // max_value  # если число делится на часть

        count += l[ind][ind1]

        num1 = temp_l.pop(0)

        l[num1 % 8][1] += 1
        if num1 % 19683 == 0: l[num1 % 8][0] += 1
        for i in dividers:
            if num1 % i == 0: l[num1 % 8][i] += 1

        temp_l += [num]
    print(count)
            
         
        
