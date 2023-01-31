with open('27A.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())

    l = [0]*100 # остатки на сто
    sum_value = 0

    for _ in range(info):
        num = int(file.readline())
        value1 = num % 100

        if value1 > 12 and l[112 - value1]:
            if l[112 - value1] > num:
                sum_value = max(sum_value, l[112 - value1]+num )

        l[num % 100] = max(l[num % 100], num)
    print(sum_value)
             
        
