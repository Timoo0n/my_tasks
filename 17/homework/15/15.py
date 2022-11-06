def f():
    with open('17.txt') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        max_value = max(list(filter(lambda el: el % 19 == 0, my_list)))
        new_list = []
        for i in range(1, len(my_list)):
            num, num1 = my_list[i-1], my_list[i]
            if num > max_value or num1 > max_value:
                new_list.append(num+num1)
        return len(new_list), min(new_list)


if __name__ == '__main__':
    print(*f())