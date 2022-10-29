

def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))[1:]

        count = 0
        new_list = list()
        for i in range(len(my_list)-1):
            if (my_list[i]+my_list[i+1]) % 3 == 0 and (my_list[i]+my_list[i+1]) % 6 != 0 and str((my_list[i]*my_list[i+1]))[-1] == '8':
                count += 1
                new_list.append(my_list[i]+my_list[i+1])

        print(count, max(new_list))


if __name__ == '__main__':
    f()