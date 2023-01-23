with open('26.txt', 'r', encoding='utf-8') as file:
    s, n = map(int, file.readline().split())
    l = sorted([int(i) for i in file])

    my_files = []

    mistake_c = 0
    
    for i in range(n):
        value = i + 1

        if value % 2 == 1 and mistake_c == 0 and (max(l)+sum(my_files)) <= s: my_value = max(l)
        elif value % 2 == 0 and mistake_c == 0 and (min(l)+sum(my_files))<=s: my_value = min(l)
        else: mistake_c += 1

        if mistake_c == 0: my_files += [my_value]; l.remove(my_value)
        else:
            if value % 2 == 0 and (sum(my_files)+min(l)) <= s: my_value = min(l)
            elif value % 2 == 1:
                difference = s - sum(my_files)
                for j in range(difference, 0, -1):
                    if j in l: my_value = j; break

            if (sum(my_files)+my_value) <= s: my_files += [my_value]; l.remove(my_value)
            else: break

    print(len(my_files), my_files[-1])

             
                
            

    
    


     
    
