with open('27B.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    q = [int(file.readline()) for _ in range(5)]

    ms = float('inf')

    for _ in range(n - 5):
        num = int(file.readline())

        value = q.pop(0)
        q.append(num)

        if value**2 + num**2 <= ms: ms = value**2 + num**2

    print(ms)
        
        
        
