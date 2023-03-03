def q(p,n,num):
    return num if p % 2 == n else 0


def f():  # Метод частичных сумм, для B сложна
    with open('27-B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        print(n)
        l = []
        collection = []
        for i in range(n):
            num = int(file.readline())
            l = [[summ+num,summ_1+q(i+1,1,num),summ_2+q(i+1,0,num)] for summ, summ_1, summ_2 in l]\
                + [[num,q(i+1,1,num),q(i+1,0,num)]]
            l = {s[2]-s[1]:s for s in sorted(l)}
            if 0 in l.keys(): collection += [l[0][0]]
            l = list(l.values())
        print(max(collection))

        
def f1():  # Префиксные суммы
    with open('27-B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = dict()
        mx = float('-inf')
        k = k1 = 0

        for i in range(n):
            num = int(file.readline())
            if (i+1)%2 == 0: k += num
            if (i+1)%2 == 1: k1 += num
            if k == k1: mx = max(mx, k+k1)
            if k-k1 in l.keys():
                mx = max(mx, k+k1-l[k-k1])
            if k-k1 not in l.keys():
                l[k-k1] = k+k1
            else:
                l[k-k1] = min(l[k-k1], k+k1)
        print(mx)
f1()
                
            
