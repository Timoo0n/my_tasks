
def f():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            q = []  # Очередь
            s = 0

            for _ in range(4):
                s += int(file.readline())
                q += [s]
                
            l = [0]*117  # Количество префиксных сумм у которых остаток-это их индекс списка
            count = 0
            
            for _ in range(n-4):
                num = int(file.readline())
                s += num
                if s % 117 == 0: count += 1
                count += l[s%117]

                s1 = q.pop(0)
                l[s1%117] += 1
                q += [s]
            print(count)


def f1():  # хз как методом частичных сумм ускорить, но файл А работает
    with open('27A.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = [ ]
        count = 0
        for _ in range(n):
            num = int(file.readline())
            l = [[num+summ, length+1] for summ, length in l] + [ [num, 1] ]
            count += len([i for i in l if i[0] % 117 == 0 and i[1] >= 5])
        print(count)


         
        
        
