
def task():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [int(i) for i in file]
        count = 0

        for i in range(info):
            for j in range(i+1, info):
                if j - i <= 7:
                    if (l[i] + l[j]) % 8 != 0: count += 1
                else: break
        print(count)



            
            
