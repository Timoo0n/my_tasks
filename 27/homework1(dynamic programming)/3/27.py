with open('27B.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    
    count = 0
    k5_0 = k5_1 = k_0 = k_1 = 0
    for _ in range(info):
        num = int(file.readline())

        if num % 5 == 0 and num % 2 == 1: count += k_0 
        elif num % 5 == 0 and num % 2 == 0: count += k_1
        elif num % 2 == 1: count += k5_0
        elif num % 2 == 0: count += k5_1

        if num % 2 == 0: k_0 += 1
        if num % 2 == 1: k_1 += 1
        if num % 5 == 0 and num % 2 == 0: k5_0 += 1
        if num % 5 == 0 and num % 2 == 1: k5_1 += 1
    print(count)

# 1) 1056
# 2) 8863690
