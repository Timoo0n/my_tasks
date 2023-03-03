
def f():  # Метод частичных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = []
            
            collection = []
            for _ in range(n):
                num = int(file.readline())
                l = [[num+summ,number+int(num%5==0)] for summ, number in l] + [ [num, int(num%5==0)] ]
                l = {s[1]%3:s for s in sorted(l)}
                if 0 in l.keys(): collection += [l[0][0]]
                l = list(l.values())
            print(max(collection))
        

def f1():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())

            l = [float('inf')]*3 # Сохраню минимальные хвостики префиксных сумм
            mx = float('-inf')
            k = 0
            s = 0

            for _ in range(n):
                num = int(file.readline())
                s += num

                if num % 5 == 0: k += 1
                if k % 3 == 0: mx = max(s, mx)
                mx = max(mx, s - l[k % 3])

                l[k%3] = min(l[k%3], s)
            print(mx)

