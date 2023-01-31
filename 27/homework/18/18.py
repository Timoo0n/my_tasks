

def all_tasks():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        l = [0] * 10
        
        for _ in range(info):
            n = file.readline().strip()
            for i in n: l[int(i)] += 1
            
        print(min(i for i in l if i != 0))
# 1) 37
# 2) 3863

if __name__ == '__main__': all_tasks()
            
