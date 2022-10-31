def f():
    with open('3.txt', 'r', encoding='utf-8') as file:
        my_list = list(map(lambda el: [int(el[0].rstrip(',00')), el[1]], [i.split() for i in file.read().split('\n')]))
        my_dict = dict()
        for my_list1 in my_list:
            if my_list1[1] not in my_dict:
                my_dict[my_list1[1]] = []
            my_dict[my_list1[1]].append(my_list1[0])

        my_dict = {s: sum(my_list) for s, my_list in my_dict.items()}
        print(max(my_dict.values()))


def main():
    f()


if __name__ == '__main__':
    main()