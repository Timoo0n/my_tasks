from itertools import product
count = 1

for word in product('АЙКОС', repeat=5):
    if word.count('О') <= 1 and 'СС' not in ''.join(word):
        print(''.join(word), count)
    count += 1
