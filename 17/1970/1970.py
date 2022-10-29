

def f():  # 1970
    with open('17.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: int(el), file.read().split()))

        new_list = []
        count = 0
        for i in range(len(my_list)-1):
            if my_list[i] % 3 == 0 or my_list[i+1] % 3 == 0:
                new_list.append(my_list[i]+my_list[i+1])
                count += 1

        print(count, max(new_list))


if __name__ == '__main__':
    f()