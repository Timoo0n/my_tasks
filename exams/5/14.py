value = 49**7+7**21-7
l = []
while value:
    l += [value % 7]
    value //= 7
print(l.count(6))
