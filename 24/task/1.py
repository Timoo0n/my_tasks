def f():
    with open('24-d12.txt', 'r', encoding='utf-8') as file:
        s = file.read()
        
        for i in set(s) - {str(i) for i in range(10)}: s = s.replace(i, ' ')

        s = [i for i in s.split() if len(i) == 11 and i[1] == i[-2] and i[0] == '8']
        print(len(s))

f()

            
