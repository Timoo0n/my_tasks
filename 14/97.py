num = 8**2018-4**1305+2**124-58
count = 0

while num != 0:
    if num % 2 == 1:
        count += 1

    num //= 2

print(count)