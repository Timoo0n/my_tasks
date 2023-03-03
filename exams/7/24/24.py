with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read()
    # X Y Z
    c = 1
    mc = 0
    for i in range(len(s)-1):
        if s[i] <= s[i+1]: c += 1
        else: mc = max(mc, c); c = 1
    print(mc)
