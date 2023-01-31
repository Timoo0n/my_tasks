
def task():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        min_value = 10**20

        for i in range(info):
            for j in range(i+5, info, 5):
                if (l[i]+l[j]) % 107 == 0:
                    min_value = min(min_value, l[i]+l[j])           
        print(min_value)

        
task()
