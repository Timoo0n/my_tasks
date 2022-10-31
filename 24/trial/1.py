def f():
    with open('24 (1).txt', 'r', encoding='utf-8') as file:
        my_str = file.read()
        count = count_old = m = 0
        for i in my_str:
            if i == "A":
                m = max(m, count + count_old + 1)
                count_old = count
                count = 0
            else:
                count += 1
        m = max(m, count + count_old + 1)
        return m


def main():
    print(f())


if __name__ == '__main__':
    main()