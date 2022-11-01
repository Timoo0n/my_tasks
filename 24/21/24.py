def f():
    with open('24.txt', 'r', encoding='utf-8') as file:
        my_str = file.read()
        count = max_count = 1
        for i in range(1, len(my_str)):
            if my_str[i-1] != my_str[i]:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
        print(max_count)


def main():
    f()


if __name__ == '__main__':
    main()