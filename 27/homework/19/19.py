
def all_tasks():
    with open('27A.txt', 'r', encoding='utf-8') as file:
        info = int(file.readline())
        x_max, x_min, y_max = 0, 0, 0

        for i in range(info):
            x, y = map(int, file.readline().split())

            if x_max < x and y == 0: x_max = x
            elif x_min > x and y == 0: x_min = x
            elif abs(y_max) < abs(y): y_max = abs(y)
        S = abs(x_max-x_min) * y_max / 2
        print(S)


if __name__ == '__main__': all_tasks()
        
