with open('2500_24.txt', 'r', encoding='utf-8') as file:
    s = file.read()
    count = 0
    for word in set(s):
        if word: count += s.count(f'G{word}ME')
    print(count)
