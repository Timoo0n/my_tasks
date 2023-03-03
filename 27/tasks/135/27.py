for word in 'ab':
    with open(f'27-135{word}.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        value = 2310
        value1 = 11
        divs = [i for i in range(2, value+1) if value % i == 0]
        l = [{i:0 for i in [0] + divs} for _ in range(value1)]
        count = 0

        for _ in range(n):
            num = int(file.readline())
            ind1 = 0 if num % 11 == 0 else 11 - (num % 11)
            max_divider = 0
            for i in divs:
                if num % i == 0: max_divider = i

            ind2 = 0
            if max_divider == 0: ind2 = value
            elif max_divider == value: ind2 = 0
            else: ind2 = value // max_divider

            count += l[ind1][ind2]
            l[num%11][0] += 1
            for i in divs:
                if num % i == 0: l[num%11][i] += 1
        print(count)
            
        
        
        
            
