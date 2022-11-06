def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        new_list = []
        for i in range(2, len(my_list)):
            if my_list[i-1] > 0 and str(my_list[i-1])[-1] == '9' and not (my_list[i] > 0 and str(my_list[i])[-1] == '9') and not (my_list[i-2] > 0 and str(my_list[i-2])[-1] == '9'):
                new_list.append(my_list[i-2] + my_list[i-1] + my_list[i])
        return len(new_list), max(new_list)


if __name__ == '__main__':
    print(*f())