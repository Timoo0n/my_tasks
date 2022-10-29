
def f():
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))

        count = 0
        new_list = []
        for i in range(1, len(my_list)-1):
            if my_list[i-1] > my_list[i] and my_list[i+1] > my_list[i]:
                count += 1
                new_list.append(max(my_list[i-1]-my_list[i], my_list[i+1]-my_list[i]))

        if my_list[-1] < my_list[-2]: count += 1; new_list.append(my_list[-2]-my_list[-1])
        elif my_list[0] < my_list[1]: count += 1; new_list.append(my_list[1]-my_list[0])

        print(count, max(new_list))


if __name__ == '__main__':
    f()