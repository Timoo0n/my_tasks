value = 2*729**1021 - 2*243**1022 + 81**1023 -2*27**1024 - 1025
l = []
while value:
    l = [value % 3] + l
    value //= 3
print(l.count(0))
