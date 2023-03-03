def f():  # Метод частичных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = []

            collection = []
            for _ in range(n):
                num = int(file.readline())
                l = [num+num1 for num1 in l] + [num]
                l = {s%1000:s for s in sorted(l)}
                if 0 in l: collection += [l[0]]
                l = list(l.values())
            print(max(collection))


def f1(): # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())

            l = [float('inf')]*1000
            mx = float('-inf')
            s = 0

            for _ in range(n):
                num = int(file.readline())
                s += num
                if s % 1000 == 0: mx = max(s, mx)
                mx = max(mx, s-l[s%1000])
                l[s%1000] = min(l[s%1000], s)
            print(mx)

