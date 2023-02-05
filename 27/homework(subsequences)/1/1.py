
def taskA():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        max_value = 0

        for i in range(info):
            value = 0
            for j in range(i, info):
                value += l[j]
                if value % 1000 == 0: max_value = max(value, max_value)
        
        print(max_value)


def taskB():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [float('inf')]*1_000  # минимальные хвостики

        max_value = 0
        value = 0
        
        for _ in range(info):
            num = int(file.readline())

            value += num
            if value % 1000 == 0: max_value = max(max_value, value)

            value1 = value - l[value % 1000]
            max_value = max(max_value, value1)
             
            l[value % 1000] = min(l[value % 1000], value)

        print(max_value)
        

if __name__ == '__main__':  taskA()
