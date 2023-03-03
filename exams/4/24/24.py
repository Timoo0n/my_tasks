with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read().replace('D', 'C').replace('F', 'C').replace('O', 'A')

    #while "CAAC" in s:
    #    s = s.replace("CAAC", "СAA AAC")
    #s = [len(i) for i in s.split()]
    #print(max(s))
    c = 3
    value = []
    for i in range(len(s)-3):
        s1 = s[i]+s[i+1]+s[i+2]+s[i+3]
        if s1 != 'CAAC': c += 1
        else: value += [c];c = 3
    print(max(value))
    
     
