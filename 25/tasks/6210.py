from fnmatch import fnmatch

for num in range(0, 10**7, 53):
    condition1 = fnmatch(str(num), '*2?2*')
    condition2 = str(num) == str(num)[::-1]
    l = set()
    for i in range(1, int(num**0.5)):
        if num % i == 0: l |= {i, num // i}
    condition3 = len(l) > 30
    if condition1 and condition2 and condition3:
        print(num, sum(l))
