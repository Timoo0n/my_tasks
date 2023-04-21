def fileA():
    with open('27A_7879.txt', 'r', encoding='utf-8') as file:
        n,k = [int(file.readline()) for _ in range(2)]
        l = [int(file.readline()) for _ in range(n)]
        mx = float('-inf')
        for i in range(n):
            for j in range(i+1,n):
                if (l[i]+l[j]) % 2023 == 0 and (((l[i] % 47 == 0) and (l[j] % 47 != 0) ) or ((l[i] % 47 != 0) and (l[j] % 47 == 0) )) and abs(j-i) >= k:
                    mx = max(mx, l[i]+l[j])
        print(mx)


def fileB():
    with open('27B_7879.txt', 'r', encoding='utf-8') as file:
        n,k = [int(file.readline()) for _ in range(2)]
        mx = float('-inf')
        l_47 = [[0,0] for _ in range(2023)]
        l_not_47 = [[0,0] for _ in range(2023)]
        for i in range(n):
            num = int(file.readline())
            if num % 47 == 0:
                length = l_not_47[(2023-(num%2023))%2023][0] 
                num1 = l_not_47[(2023-(num%2023))%2023][1]
            else:
                length = l_47[(2023-(num%2023))%2023][0] 
                num1 = l_47[(2023-(num%2023))%2023][1]
            if length and num1 and abs(length-i) >= k:
                mx = max(mx, num1+num)
            if num % 47 == 0:
                if num > l_47[num%2023][1]:
                    l_47[num%2023][1] = num
                    l_47[num%2023][0] = i                    
            else:
                if num > l_not_47[num%2023][1]:
                    l_not_47[num%2023][1] = num
                    l_not_47[num%2023][0] = i
        print(mx)
fileA()
fileB()
