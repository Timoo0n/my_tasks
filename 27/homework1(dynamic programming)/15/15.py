with open('27.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for _ in range(4)]
    max_l = [0]*137
    min_l = [10**20]*137
    value = 0
    
    for _ in range(info-4):
        num = int(file.readline())

        if max_l[num%137] != 0: value = max(value, abs(max_l[num%137]-num))
        if min_l[num%137] != 10**20: value = max(value, abs(min_l[num%137]-num))

        value1 = q.pop(0)
        max_l[value1 % 137] = max(max_l[value1 % 137], value1)
        min_l[value1 % 137] = min(min_l[value1 % 137], value1)
        q.append(num)
    print(value)
