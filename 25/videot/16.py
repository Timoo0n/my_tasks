def div(x):
    my_set = set()
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            my_set |= {i, x // i}

    return sorted(my_set)


print(len(div(2**81*3**9)))
