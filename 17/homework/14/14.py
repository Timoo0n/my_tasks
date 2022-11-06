def f():
    with open('17.txt') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        sr = sum(my_list)/len(my_list)
        new_list = []
        for i in range(2, len(my_list)):
            num, num1, num2 = my_list[i-2], my_list[i-1], my_list[i]
            result = sum([1 for i in (num, num1, num2) if i > sr])
            if result >= 2:
                new_list.append(num+num1+num2)
        return len(new_list), max(new_list)


if __name__ == '__main__':
    print(*f())