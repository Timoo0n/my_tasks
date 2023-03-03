with open('24.txt', 'r', encoding='utf-8') as file:
    s = file.read()

    while 'XYZ' in s:
        s = s.replace('XYZ', 'XY YZ')
    print(max(len(i) for i in s.split()))
