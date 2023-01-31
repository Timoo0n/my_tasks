from itertools import product

c = 0

for number in product('01234567', repeat=5):
    if number[0] not in ('0', '1', '3', '5', '7', '9') \
       and number[-1] not in ('2', '6') and number.count('7') <= 2:
        c += 1
print(c)
