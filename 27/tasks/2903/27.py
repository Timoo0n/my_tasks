
def f():  # Метод частичных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())

            l = []

            collection = []
            for _ in range(n):
                num = int(file.readline())
                l = [[num+num1, number+int(num%3==0)] for num1, number in l]\
                    + [ [num, int(num%3==0)] ]
                l = {s[1]-10:s for s in sorted(l, reverse=True)}
                if 0 in l: collection += [l[0][0]]
                l = list(l.values())
            print(min(collection))


def f1():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = {i:float('-inf') for i in range(n)} # Сохраняем максимальные префиксные суммы по кол-ву чисел кратных 3

            mx = float('inf')
            k = 0
            s = 0
            
            for _ in range(n):
                num = int(file.readline())
                s += num

                if num % 3 == 0: k += 1
                if k == 10: mx = min(mx, s)

                if k > 10: mx = min(mx, s - l[k-10])

                l[k] = max(s, l[k])
            print(mx)

f1()
