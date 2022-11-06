def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        list_4 = list(filter(lambda el: str(el)[-1] == '4', my_list))
        value = max(list_4) + min(list_4)
        new_list = []
        for i in range(1, len(my_list)):
            if (my_list[i-1] + my_list[i]) < value:
                new_list.append(my_list[i-1]+my_list[i])

        return len(new_list), max(new_list)


if __name__ == '__main__':
    print(*f())