def f():
    with open('24.txt') as file:
        s = file.read()
        c = max_count = 0

        max_list = []
        for j in range(5):
            for i in range(j, len(s)-4, 5):
                if s[i] + s[i+1] + s[i+2] + s[i+3] + s[i+4] == 'XVIII':
                    c += 1
                else:
                    max_count = max(max_count, c)
                    c = 0
            max_list.append(max_count)
            c = max_count = 0
        print(max(max_list))

def f1():
    with open('24.txt') as file:
        s = file.read()
        print(s.count('XVIII'))

f1()
