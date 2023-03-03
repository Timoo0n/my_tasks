def f():  # Метод частичных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
             
            l = []
            count = 0
            for _ in range(n):
                num = int(file.readline())
                l = [num+num1 for num1 in l] + [num]
                count += len([1 for i in l if i%666 == 0])
                
            print(count)

         
def f1():  # Метод префиксных сумм
    for word 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            l = [0]*666
            count = 0
            s = 0
            for _ in range(n):
                num = int(file.readline())
                s += num
                if s % 666 == 0: count += 1
                count += l[s%666]

                l[s%666] += 1
            print(count)

