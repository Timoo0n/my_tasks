with open('24_587.txt', 'r', encoding='utf-8') as file:
    s = file.read().split()
    count = 0
    for i in s:
        numB = i.count('B')
        numA = i.count('A')
        if numB/numA >= 1.05: count += 1
print(count)
        
