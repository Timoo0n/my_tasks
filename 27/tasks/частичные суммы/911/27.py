from itertools import permutations


with open('27-A.txt', 'r', encoding='utf-8') as file:
    n = int(file.readline())
    s = [ [0, 0, 0] ]
    for _ in range(n):
        tr = [int(i) for i in file.readline().split()]
        s = [[a1+b1, a2+b2, a3+b3] for a1, a2, a3 in s for b1, b2, b3 in permutations(tr)]
        s = {(x[0]%2, x[1]%2): x for x in sorted(s)}.values()
         
    for a1, a2, a3 in s:
        if a1 % 2 == 1 and a2 % 2 == 1:
            print(a3)
