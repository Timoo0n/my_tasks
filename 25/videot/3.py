
my_list = []
num = 850_001

while len(my_list) != 6:

    my_set = set()
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            my_set |= {i, num // i}

    if len(my_set) != 0:
        value = max(my_set) - min(my_set)
        if value != 0 and value % 3 == 0:
            my_list.append((num, value))

    num += 1

print(*my_list, sep='\n')
