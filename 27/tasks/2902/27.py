def f():  # Метод частичных сумм
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [0]*11

        count = 0
        k = 0
        for _ in range(n):
            num = int(file.readline())
            if num % 5 == 0: k += 1
            if k % 11 == 0: count += 1
            count += l[k%11]

            l[k%11] += 1
        print(count)


def f1():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            count = 0
            k = 0
            l = [0]*11
            
            for _ in range(n):
                num = int(file.readline())
                if num % 5 == 0: k += 1
                if k % 11 == 0: count += 1
                count += l[k%11]

                l[k%11] += 1
            print(count)

