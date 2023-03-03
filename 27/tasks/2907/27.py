def f():  # Метод частичных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = []
            collection = []
            for _ in range(n):
                num = int(file.readline())
                l = [[num+summ, k+int(num>0 and abs(num) % 2 == 0)] for summ, k in l] \
                    + [[num, int(num>0 and abs(num) % 2 == 0)]]
                l = {s[1]%30:s for s in sorted(l)}
                if 0 in l.keys(): collection += [l[0][0]]
                l = list(l.values())
            print(max(collection))

def f1():  # Метод префиксных сумм
    for word in 'AB':
        with open('27B.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = [float('inf')]*30  # Складываю МИНИМАЛЬНЫЕ префиксные суммы по остатку количеств положительных четных элементов

            max_summ = float('-inf')
            k = 0
            s = 0
            
            for _ in range(n):
                num = int(file.readline())
                s +=num
                if num > 0 and num % 2 == 0: k += 1
                if k % 30 == 0: max_summ = max(max_summ, s)

                max_summ = max(max_summ, s - l[k%30])
                l[k%30] = min(s, l[k%30])
            print(max_summ)
f1()
            
            
            
