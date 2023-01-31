with open('27A.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    q = [int(file.readline()) for _ in range(6)]

    l_23_3 = [10**20]*23
    l_23_2 = [10**20]*23
    l_23_6 = [10**20]*23
    l_23 = [10**20]*23

    min_value = 10**20

    for _ in range(info-6):
        num = int(file.readline())

        ind = 0 if num % 23 == 0 else 23 - (num % 23)
        if num % 6 == 0 and l_23[ind] != 10**20:

            min_value = min(min_value, num + l_23[ind])
             

        elif num % 2 == 0 and l_23_3[ind] != 10**20:

            min_value = min(min_value, num + l_23_3[ind])
            

        elif num % 3 == 0 and l_23_2[ind] != 10**20:

            min_value = min(min_value, num + l_23_2[ind])
            

        elif l_23_6[ind] != 10**20:

            min_value = min(min_value, num + l_23_6[ind])
            
        value = q.pop(0)
        l_23[value % 23] = min(l_23[value % 23], value)
        if value % 6 == 0: l_23_6[value % 23] = min(l_23_6[value % 23], value)
        if value % 2 == 0: l_23_2[value % 23] = min(l_23_2[value % 23], value)
        if value % 3 == 0: l_23_3[value % 23] = min(l_23_3[value % 23], value)
        q.append(num)

    print(min_value)
            
    
