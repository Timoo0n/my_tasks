def f():
    with open('17.txt') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))
        new_list = []
        for i in range(3, len(my_list)):
            num, num1, num2, num3 = my_list[i-3], my_list[i-2], my_list[i-1], my_list[i]
            if [num, num1, num2, num3] == sorted([num, num1, num2, num3], reverse=True) and (max(num, num1, num2, num3) - min(num, num1, num2, num3)) > 1000:
                new_list.append(sum([num, num1, num2, num3]))
        return len(new_list), min(new_list)


if __name__ == '__main__':
    print(*f())
