def f():  # Метод частичных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = []

            collection = []
            for _ in range(n):
                num = int(file.readline())
                l = [[num+num1, length+1] for num1, length in l] \
                    + [ [num, 1] ]
                l = {s[0]%69:s for s in sorted(l)}
                if 0 in l.keys(): collection += [l[0]]
                l = list(l.values())

            mx = max(i[0] for i in collection)
            length = float('inf')
            for sum1, length1 in sorted(collection,key=lambda el: el[0], reverse=True):
                if sum1 == mx: length = min(length, length1)
                if mx > sum1: break
            print(length)

def f1():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = [[float('inf'), 0] for _ in range(69)]

            mx = float('-inf')
            length = 0
            s = 0

            for i in range(n):
                num = int(file.readline())
                s += num

                if s % 69 == 0 and s > mx:
                    mx, length = s, i+1

                s1 = s - l[s%69][0]
                length1 = i+1-l[s%69][1]

                if (s1 == mx and length1 < length) or s1 > mx:
                    length, mx = length1, s1

                if l[s%69][0] > s:
                    l[s%69][0] = s
                    l[s%69][1] = i+1
            print(length)
f1()

            
            



            
