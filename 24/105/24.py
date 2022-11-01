def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        my_str = file.read()
        count = max_count = 1
        my_list = [[] for _ in range(4)]
        for i in range(1, len(my_str)):
            if my_str[i] == my_str[i-1]:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1

        return max_count


def main():
    print(f())


if __name__ == '__main__':
    main()