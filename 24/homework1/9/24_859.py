count = 0
for s in open('24_859.txt', 'r'):
    if s.count('S') == s.count('X'): count += 1
print(count)
