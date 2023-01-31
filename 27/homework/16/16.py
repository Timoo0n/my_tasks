from itertools import combinations


def all_tasks():
    with open('27B.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        
        info_l = [0]*(9*6+1)
        for _ in range(info):
            n = file.readline().strip()
            info_l[sum(int(i) for i in n)] += 1
        print(max(info_l))

#  1) 10
#  2) 621

if __name__ == '__main__': all_tasks()
