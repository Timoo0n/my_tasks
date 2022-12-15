l = [0]*26


for i in range(len(l)):
    n = i + 1
    if n == 1:
        l[i] = 1
    elif n % 2 == 0:
        l[i] = n + l[i-1]
    elif n % 2 == 1 and n > 1:
        l[i] = 2 * l[i-2]

print(*l, sep='\n')
