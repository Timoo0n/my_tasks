

l = [0] * 1900

for i in range(len(l)):
    n = i + 1
    if n == 1: l[i] = 2
    elif n > 1: l[i] = 2 * l[i - 1]

print(l[1900-1]/2**1890)
