with open('27A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    l = [0]

    for _ in range(n):
        num = int(file.readline())
        l += [num+num1 for num1 in l] + [num]
        l = list({num%17:num for num in sorted(l)}.values())
    print(max(i for i in l if i % 17 == 0 ))
        
