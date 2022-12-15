

def f():
    my_list = []
    for i in '0123456789ABCDEF':
        for j in '0123456789ABCDEF':
            n = int(f'1{i}DED{j}CED', 16)
            if n % 121 == 0:
                my_list.append((n, n // 121))

    for i in sorted(my_list, key=lambda el: el[0], reverse=True):
        print(*i)


f()
