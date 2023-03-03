def f():  # Метод частичных сумм
   for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = []

            collection = []
            for _ in range(n):
                num = int(file.readline())
                l = [[num+num1, length+1] for num1, length in l] \
                    + [[num, 1]]
                l = {s[0]%2077:s for s in sorted(l, reverse=True)}
                if 0 in l.keys(): collection += [l[0]]
                l = list(l.values())
            min_summ = min(i[0] for i in collection)
            max_length = float('-inf')
            for summ, length in sorted(collection):
                if summ == min_summ: max_length = max(max_length, length)
                if min_summ < summ: break
            print(max_length)


def f1():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())

            min_summ = float('inf')
            max_length = float('-inf')
            l = [[float('-inf'), 0] for _ in range(2077)]
            s = 0
            
            for i in range(n):
                num = int(file.readline())
                s += num
                if s % 2077 == 0 and s < min_summ:
                    min_summ = s
                    max_length = i+1

                s1 = s - l[s%2077][0]
                length1 = i+1 - l[s%2077][1]
                if (s1 < min_summ) or (s1 == min_summ and length1 > max_length):
                    min_summ, max_length = s1, length1

                if l[s%2077][0] < s:
                    l[s%2077][0] = s
                    l[s%2077][1] = i+1
            print(max_length)

                

            
            
