
def all_tasks():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        
        l = [0]*10
        for _ in range(info):
            n = file.readline()
            l[int(n[0])] += 1
        l = [i for i in l if i != 0]
        print(min(l))

# 1) 7
# 2)1064


if __name__ == '__main__': all_tasks()
            
            
