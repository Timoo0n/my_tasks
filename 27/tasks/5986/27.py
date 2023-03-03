def f():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            length = float('-inf')
            l = dict()
            k = k1 = 0

            for _ in range(n):
                num = int(file.readline())
                if num % 2 == 0: k += 1
                if num % 2 == 1: k1 += 1
                if k == k1: length = max(k+k1, length)

                if k-k1 in l.keys():
                    length = max(length, k+k1-l[k-k1])

                if k-k1 not in l.keys():
                    l[k-k1] = k+k1
                else:
                    l[k-k1] = min(l[k-k1], k+k1)
            print(length)


def f1():  # Метод частичных сумм, для файла B прога работает 8 минут
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = []

            collection = []
            for _ in range(n):
                num = int(file.readline())

                l = [[length+1,k+int(num%2==0), k1+int(num%2==1), summ+num] for length,k,k1,summ in l]\
                    + [ [1,int(num%2==0), int(num%2==1), num]]

                l = {s[1]-s[2]: s for s in sorted(l)}
                if 0 in l.keys(): collection += [ l[0][0]]
                l = list(l.values())
            print(max(collection))
            
f1()
            
