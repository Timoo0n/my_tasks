def f():
    with open('17.txt') as file:
        new_list = []
        my_list = list(map(lambda el: int(el), file.read().split()))
        for i in range(2, len(my_list)):
            num, num1, num2 = my_list[i], my_list[i-1], my_list[i-2]
            if any(i % 3 == 2 for i in (num, num1, num2)):
                new_list.append(min(num, num1, num2))

        return len(new_list), sum(new_list)


if __name__ == '__main__':
    print(*f())