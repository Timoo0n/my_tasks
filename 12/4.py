
my_set = set()
for i in range(1, 100):
    s = '5' * i
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    my_set |= {s}

print(len(my_set))
