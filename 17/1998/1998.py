
def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()[1:]))

        new_list = list()
        count = 0
        for i in range(len(my_list)-2):
            if (my_list[i]*my_list[i+1]*my_list[i+2]) % 7 == 0 and str(my_list[i]+my_list[i+1]+my_list[i+2])[-1] == '5':
                new_list.append(my_list[i]+my_list[i+1]+my_list[i+2])
                count += 1
        print(count, max(new_list))


if __name__ == '__main__':
    f()