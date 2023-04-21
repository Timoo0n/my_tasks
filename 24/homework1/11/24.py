from string import ascii_uppercase


count = 0
with open('24_2502.txt', 'r', encoding='utf-8') as file:
    s = file.read().split()
    for i in s:
        for word in set(ascii_uppercase):
            i = i.replace(f'K{word}GE', '*')
        if i.count('*') > 0: count += 1
print(count)
