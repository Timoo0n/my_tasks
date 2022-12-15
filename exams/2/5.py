def f(num):
    n = str(bin(num))[2:]
    
    if sum(list(map(int, list(n)))) % 2 == 0: n = '10' + n[:-2] + '00'
    elif sum(list(map(int, list(n)))) % 2 == 1: n = '11' + n[:-2] + '11'

    return int(n, 2)


def main():
    my_list = []
    for i in range(30):
        result = f(i)
        my_list += [result]
    print(max(my_list))
    

if __name__ == '__main__': main()
