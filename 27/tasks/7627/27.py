def fileA():
    with open('27_A_7627.txt', 'r', encoding='utf-8') as file:
        k, n = [int(file.readline()) for _ in range(2)]
        l = [int(file.readline()) for _ in range(n)]
        mx = float('-inf')
        for i in range(n):
            for j in range(k+i, n):
                if abs(j-i) >= k:
                    mx = max(mx, l[i]+l[j])
        print(mx)

def fileB():
    with open('27_B_7627.txt', 'r', encoding='utf-8') as file:
        k, n = [int(file.readline()) for _ in range(2)]
        l = [int(file.readline()) for _ in range(n)]
        mx, first_num = float('-inf'), l[0]

        for i in range(k, n):
            first_num = max(first_num, l[i-k])
            mx = max(mx, first_num+l[i])
        print(mx)

#19974
#18469835
