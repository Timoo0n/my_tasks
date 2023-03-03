
def f():  # Метод префиксных сумм
    for word in 'AB':
        with open(f'27{word}.txt', 'r', encoding='utf-8') as file:
            n = int(file.readline())
            q = []
            s = 0
            k = 0
            for _ in range(6):
                num = int(file.readline())
                s += num
                if num % 7 == 0 and num > 0: k += 1
                q += [ [s, k] ]
            mx = float('-inf')
            l = [float('inf')]*7
            
            for _ in range(n-6):
                num = int(file.readline())
                s += num
                
                if num % 7 == 0 and num > 0: k += 1
                if k % 7 == 0: mx = max(mx, s)
                mx = max(mx, s - l[k%7])

                s1, k1 = q.pop(0)
                l[k1%7] = min(l[k1%7], s1)
                q += [[s, k]]
                
            print(mx)

def f1():  # Метод частичных сумм
    with open('27B.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline())
        l = []
        collection = []
        for _ in range(n):
            num = int(file.readline())
            l = [[num+summ,k+int(abs(num)%7==0 and num > 0), length+1] for summ,k,length in l] \
                + [ [num, int(abs(num)%7==0 and num > 0), 1] ]
            l = {(int(s[2]>=7), int(s[1]%7==0)):s for s in sorted(l)}
            if (1, 1) in l: collection += [l[(1,1)][0]]
            l = list(l.values())
        print(max(collection))
         
f1()
            
        
         
