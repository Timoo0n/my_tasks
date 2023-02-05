def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        count = 0
        
        for i in range(info):
            k = 0
            for j in range(i, info):
                if l[j] % 5 == 0: k += 1
                if k % 11 == 0: count += 1
        print(count)


def taskB():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [0]*11  # отбор по количеству таких чисел, которые кратны 5

        s = 0
        count = 0
        k = 0
        for i in range(info):
            num = int(file.readline())

            if num % 5 == 0: k += 1
            if k % 11 == 0: count += 1
            count += l[k % 11]

            l[k % 11] += 1
        print(count)


if __name__ == '__main__': taskA(); taskB()
