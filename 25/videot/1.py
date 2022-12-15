

def f():
    for i in range(244143, 367822):
        if int(i**0.5)**2 == i:
            my_set = set()
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    my_set |= {j, i//j}

            my_list = sorted(my_set)

            if len(my_list) == 5:
                print(my_list[-2], my_list[-1])


# нечетное количество делитилей только у квадратов
if __name__ == '__main__':
    f()
    
    
