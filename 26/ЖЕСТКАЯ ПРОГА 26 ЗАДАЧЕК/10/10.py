with open('26.txt', 'r', encoding='utf-8') as file:
    info = int(file.readline())
    l1 = [0]*2_000_000

    for i in range(info):
        st, end = map(int, file.readline().split())
        l1[st] += 1
        l1[end] -= 1
    k = 0

    street = ''
    for i in range(len(l1)):
        k += l1[i]
        if k == 0: street += '='
        elif k != 0: street += '-'

    street = list(map(lambda el: len(el), street.replace('-', ' ').split()))
         
    print(len(street), max(street))
    
