def algoritm(n):
    n = str(bin(n))[2:]
    my_sum = sum(list(map(int, list(n))))
    if my_sum % 2 == 0: n = '10' + n[2:] + '1'
    elif my_sum % 2 == 1: n = '11' + n[2:] + '0'
    return int(n, 2)
        

def main():
    my_list = list()
    for i in range(1, 16):
        my_list += [algoritm(i)]
    print(max(my_list))
    


if __name__ == '__main__': main()
