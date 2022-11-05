def main():
    for i in range(1, 1000):
        if 27 <= i < 81 and 49 <= i < 343 and i % 8 == 7 and i // 8 % 8 == 1:
            print(i)


if __name__ == '__main__':
    main()
